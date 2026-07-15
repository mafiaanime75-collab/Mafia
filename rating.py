from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database import top_global, top_group, get_or_create_user
from config import CURRENCY_NAME, CURRENCY_SYMBOL, GEM_NAME, GEM_SYMBOL

router = Router(name="rating")


@router.message(Command("rating"))
async def cmd_rating(message: Message):
    """Global reyting — faqat Kizuna/ELO asosida. Sehirli Tosh reytingga ta'sir qilmaydi."""
    rows = await top_global(10)
    if not rows:
        await message.answer("Hali hech kim o'ynamagan 😅")
        return
    lines = ["🏆 <b>Global Reyting (TOP-10)</b>\n"]
    for i, r in enumerate(rows, start=1):
        name = r["full_name"] or r["username"] or str(r["user_id"])
        lines.append(f"{i}. {name} — {r['elo']} ELO ({r['wins']}W/{r['losses']}L)")
    await message.answer("\n".join(lines))


@router.message(Command("grouprating"))
async def cmd_group_rating(message: Message):
    if message.chat.type not in ("group", "supergroup"):
        await message.answer("Bu buyruq faqat guruhlarda ishlaydi.")
        return
    rows = await top_group(message.chat.id, 10)
    if not rows:
        await message.answer("Bu guruhda hali o'yin o'ynalmagan 😅")
        return
    lines = [f"🏅 <b>{message.chat.title} — Guruh Reytingi</b>\n"]
    for i, r in enumerate(rows, start=1):
        lines.append(f"{i}. ID {r['user_id']} — {r['elo']} ELO ({r['wins']}W/{r['losses']}L)")
    await message.answer("\n".join(lines))


@router.message(Command("profile"))
async def cmd_profile(message: Message):
    u = await get_or_create_user(
        message.from_user.id, message.from_user.username or "", message.from_user.full_name
    )
    title = f" «{u['title']}»" if u["title"] else ""
    await message.answer(
        f"👤 <b>{u['full_name']}{title}</b>\n"
        f"⭐ ELO (reyting): {u['elo']}\n"
        f"🎮 O'yinlar: {u['games_played']} (G'alaba: {u['wins']}, Mag'lubiyat: {u['losses']})\n\n"
        f"{CURRENCY_SYMBOL} {CURRENCY_NAME}: {u['balance']} <i>(o'yin natijasidan, reytingga bog'liq)</i>\n"
        f"{GEM_SYMBOL} {GEM_NAME}: {u['gems']} <i>(kunlik bonus, reytingga ta'sir qilmaydi)</i>"
    )
