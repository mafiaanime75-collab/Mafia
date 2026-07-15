"""
aiosqlite ma'lumotlar bazasi.
Ikki valyuta:
  - balance (Kizuna 🔗)   -> faqat o'yin natijasidan (g'alaba/mag'lubiyat/MVP), reytingga bog'liq
  - gems (Sehirli Tosh 💎) -> kunlik bepul bonus, alohida do'kon, reytingga TA'SIR QILMAYDI
"""
import aiosqlite
import json
import time
from config import DB_PATH, DAILY_GEM_REWARD

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    full_name TEXT,
    elo INTEGER NOT NULL DEFAULT 1000,
    wins INTEGER NOT NULL DEFAULT 0,
    losses INTEGER NOT NULL DEFAULT 0,
    games_played INTEGER NOT NULL DEFAULT 0,
    balance INTEGER NOT NULL DEFAULT 100,
    gems INTEGER NOT NULL DEFAULT 0,
    last_daily INTEGER NOT NULL DEFAULT 0,
    title TEXT DEFAULT '',
    created_at INTEGER
);

CREATE TABLE IF NOT EXISTS group_ratings (
    group_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    elo INTEGER NOT NULL DEFAULT 1000,
    wins INTEGER NOT NULL DEFAULT 0,
    losses INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (group_id, user_id)
);

CREATE TABLE IF NOT EXISTS game_sessions (
    session_id TEXT PRIMARY KEY,
    group_id INTEGER NOT NULL,
    host_id INTEGER NOT NULL,
    world TEXT,
    status TEXT NOT NULL DEFAULT 'lobby',
    state_json TEXT,
    created_at INTEGER
);

CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    item_key TEXT NOT NULL,
    currency TEXT NOT NULL,   -- 'kizuna' | 'gem'
    purchased_at INTEGER
);
"""


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.executescript(SCHEMA)
        await db.commit()


async def get_or_create_user(user_id: int, username: str = "", full_name: str = "") -> dict:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cur = await db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        row = await cur.fetchone()
        if row:
            return dict(row)
        await db.execute(
            "INSERT INTO users (user_id, username, full_name, created_at) VALUES (?, ?, ?, ?)",
            (user_id, username, full_name, int(time.time())),
        )
        await db.commit()
        cur = await db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        return dict(await cur.fetchone())


async def update_user_after_game(user_id: int, won: bool, elo_delta: int, kizuna_reward: int):
    async with aiosqlite.connect(DB_PATH) as db:
        col = "wins" if won else "losses"
        await db.execute(
            f"UPDATE users SET {col} = {col} + 1, games_played = games_played + 1, "
            f"elo = elo + ?, balance = balance + ? WHERE user_id = ?",
            (elo_delta, kizuna_reward, user_id),
        )
        await db.commit()


async def update_group_rating(group_id: int, user_id: int, won: bool, elo_delta: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO group_ratings (group_id, user_id, elo, wins, losses) VALUES (?, ?, 1000, 0, 0) "
            "ON CONFLICT(group_id, user_id) DO NOTHING",
            (group_id, user_id),
        )
        col = "wins" if won else "losses"
        await db.execute(
            f"UPDATE group_ratings SET {col} = {col} + 1, elo = elo + ? WHERE group_id = ? AND user_id = ?",
            (elo_delta, group_id, user_id),
        )
        await db.commit()


async def top_global(limit: int = 10) -> list[dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cur = await db.execute("SELECT * FROM users ORDER BY elo DESC, wins DESC LIMIT ?", (limit,))
        return [dict(r) for r in await cur.fetchall()]


async def top_group(group_id: int, limit: int = 10) -> list[dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cur = await db.execute(
            "SELECT * FROM group_ratings WHERE group_id = ? ORDER BY elo DESC, wins DESC LIMIT ?",
            (group_id, limit),
        )
        return [dict(r) for r in await cur.fetchall()]


async def adjust_balance(user_id: int, amount: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET balance = balance + ? WHERE user_id = ?", (amount, user_id))
        await db.commit()


async def adjust_gems(user_id: int, amount: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET gems = gems + ? WHERE user_id = ?", (amount, user_id))
        await db.commit()


async def claim_daily_gems(user_id: int) -> tuple[bool, int]:
    """Kuniga bir marta Sehirli Tosh olish. (muvaffaqiyat, qolgan_soat) qaytaradi."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cur = await db.execute("SELECT last_daily FROM users WHERE user_id = ?", (user_id,))
        row = await cur.fetchone()
        now = int(time.time())
        last = row["last_daily"] if row else 0
        if now - last < 86400:
            remaining_h = (86400 - (now - last)) // 3600
            return False, remaining_h
        await db.execute(
            "UPDATE users SET gems = gems + ?, last_daily = ? WHERE user_id = ?",
            (DAILY_GEM_REWARD, now, user_id),
        )
        await db.commit()
        return True, 0


async def record_purchase(user_id: int, item_key: str, currency: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO purchases (user_id, item_key, currency, purchased_at) VALUES (?, ?, ?, ?)",
            (user_id, item_key, currency, int(time.time())),
        )
        await db.commit()


async def create_session(session_id: str, group_id: int, host_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO game_sessions (session_id, group_id, host_id, status, state_json, created_at) "
            "VALUES (?, ?, ?, 'lobby', '{}', ?)",
            (session_id, group_id, host_id, int(time.time())),
        )
        await db.commit()


async def save_session_state(session_id: str, state: dict, status: str | None = None):
    async with aiosqlite.connect(DB_PATH) as db:
        if status:
            await db.execute(
                "UPDATE game_sessions SET state_json = ?, status = ? WHERE session_id = ?",
                (json.dumps(state), status, session_id),
            )
        else:
            await db.execute(
                "UPDATE game_sessions SET state_json = ? WHERE session_id = ?",
                (json.dumps(state), session_id),
            )
        await db.commit()
