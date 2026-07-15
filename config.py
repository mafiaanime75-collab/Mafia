"""
Sozlamalar. Alwaysdata kabi serverlarda .env fayl orqali yuklanadi.
"""
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "8613383536:AAFtxKbwkbo6jwpU_AI-oHdoHLstw-8DcjE")
MAIN_GROUP_ID = int(os.getenv("MAIN_GROUP_ID", "-5305326142"))
MAIN_GROUP_INVITE_LINK = os.getenv("MAIN_GROUP_INVITE_LINK", "https://t.me/+j5SvFE1hj75iNzUy")
DB_PATH = os.getenv("DB_PATH", "animafia.db")

# --- O'yin qoidalari ---
MIN_PLAYERS = 4
MAX_PLAYERS = 20
NIGHT_DURATION_SEC = 45
DAY_DISCUSSION_SEC = 90
VOTING_DURATION_SEC = 40

# --- Valyutalar ---
# 1) Kizuna - faqat o'yin natijasidan (g'alaba/mag'lubiyat/MVP) olinadi, reytingga bog'liq
CURRENCY_NAME = "Kizuna"
CURRENCY_SYMBOL = "🔗"

# 2) Sehirli Tosh - har kuni bepul bonus sifatida beriladi, alohida do'kon, reytingga kirmaydi
GEM_NAME = "Sehirli Tosh"
GEM_SYMBOL = "💎"
DAILY_GEM_REWARD = 15
