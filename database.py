# ============ MA'LUMOTLAR BAZASI ============
import sqlite3
import json
from datetime import datetime

DB_PATH = "animafia.db"

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                stones INTEGER DEFAULT 0,
                coins INTEGER DEFAULT 0,
                games_played INTEGER DEFAULT 0,
                games_won INTEGER DEFAULT 0,
                games_lost INTEGER DEFAULT 0,
                daily_bonus_level INTEGER DEFAULT 1,
                daily_bonus_streak INTEGER DEFAULT 0,
                last_daily_bonus TEXT,
                league INTEGER DEFAULT 1,
                rating INTEGER DEFAULT 0,
                created_at TEXT,
                inventory TEXT DEFAULT '[]'
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS groups (
                group_id INTEGER PRIMARY KEY,
                group_name TEXT,
                group_link TEXT,
                admin_id INTEGER,
                total_games INTEGER DEFAULT 0,
                created_at TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                username TEXT,
                type TEXT,
                message TEXT,
                status TEXT DEFAULT 'new',
                created_at TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS games (
                game_id INTEGER PRIMARY KEY AUTOINCREMENT,
                group_id INTEGER,
                anime_world TEXT,
                status TEXT DEFAULT 'waiting',
                players TEXT DEFAULT '[]',
                roles TEXT DEFAULT '{}',
                winner TEXT,
                created_at TEXT,
                finished_at TEXT
            )
        """)

        self.conn.commit()

    def add_user(self, user_id, username, first_name, last_name):
        now = datetime.now().isoformat()
        self.cursor.execute("""
            INSERT OR IGNORE INTO users 
            (user_id, username, first_name, last_name, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, username, first_name, last_name, now))
        self.conn.commit()

    def get_user(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        row = self.cursor.fetchone()
        if row:
            return {
                'user_id': row[0], 'username': row[1], 'first_name': row[2],
                'last_name': row[3], 'stones': row[4], 'coins': row[5],
                'games_played': row[6], 'games_won': row[7], 'games_lost': row[8],
                'daily_bonus_level': row[9], 'daily_bonus_streak': row[10],
                'last_daily_bonus': row[11], 'league': row[12], 'rating': row[13],
                'created_at': row[14], 'inventory': json.loads(row[15]) if row[15] else []
            }
        return None

    def update_user(self, user_id, **kwargs):
        fields = []
        values = []
        for key, value in kwargs.items():
            fields.append(f"{key} = ?")
            values.append(value)
        values.append(user_id)
        query = f"UPDATE users SET {', '.join(fields)} WHERE user_id = ?"
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_top_users(self, limit=20):
        self.cursor.execute("""
            SELECT user_id, username, first_name, rating, games_won, league
            FROM users ORDER BY rating DESC LIMIT ?
        """, (limit,))
        return self.cursor.fetchall()

    def add_feedback(self, user_id, username, feedback_type, message):
        now = datetime.now().isoformat()
        self.cursor.execute("""
            INSERT INTO feedback (user_id, username, type, message, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, username, feedback_type, message, now))
        self.conn.commit()

    def get_feedback(self, status='new'):
        self.cursor.execute("SELECT * FROM feedback WHERE status = ? ORDER BY created_at DESC", (status,))
        return self.cursor.fetchall()

    def mark_feedback_read(self, feedback_id):
        self.cursor.execute("UPDATE feedback SET status = 'read' WHERE id = ?", (feedback_id,))
        self.conn.commit()

    def delete_feedback(self, feedback_id):
        self.cursor.execute("DELETE FROM feedback WHERE id = ?", (feedback_id,))
        self.conn.commit()

    def create_game(self, group_id, anime_world):
        now = datetime.now().isoformat()
        self.cursor.execute("""
            INSERT INTO games (group_id, anime_world, created_at)
            VALUES (?, ?, ?)
        """, (group_id, anime_world, now))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_game(self, game_id, **kwargs):
        fields = []
        values = []
        for key, value in kwargs.items():
            if key in ['players', 'roles']:
                value = json.dumps(value)
            fields.append(f"{key} = ?")
            values.append(value)
        values.append(game_id)
        query = f"UPDATE games SET {', '.join(fields)} WHERE game_id = ?"
        self.cursor.execute(query, values)
        self.conn.commit()

db = Database()
