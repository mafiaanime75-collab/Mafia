"""
Sozlamalar. Alwaysdata kabi serverlarda .env fayl orqali yuklanadi.
DIQQAT: Bu loyihada HECH QANDAY subfolder (handlers/ va h.k.) ishlatilmaydi —
barcha .py fayllar bitta papkada, tekis (flat) joylashgan. GitHub'ga papkasiz
joylashtirilganda ham hech narsa buzilmaydi.
"""
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "8613383536:AAFtxKbwkbo6jwpU_AI-oHdoHLstw-8DcjE")
MAIN_GROUP_ID = int(os.getenv("MAIN_GROUP_ID", "-5305326142"))
MAIN_GROUP_INVITE_LINK = os.getenv("MAIN_GROUP_INVITE_LINK", "https://t.me/+j5SvFE1hj75iNzUy")
DB_PATH = os.getenv("DB_PATH", "animafia.db")

_admin_ids_raw = os.getenv("ADMIN_IDS", "")
ADMIN_IDS = {int(x.strip()) for x in _admin_ids_raw.split(",") if x.strip().isdigit()}

# --- O'yin qoidalari ---
MIN_PLAYERS = 4
MAX_PLAYERS = 20
NIGHT_DURATION_SEC = 45
DAY_DISCUSSION_SEC = 90
VOTING_DURATION_SEC = 40

# --- Valyutalar ---
CURRENCY_NAME = "Kizuna"
CURRENCY_SYMBOL = "🔗"

GEM_NAME = "Sehirli Tosh"
GEM_SYMBOL = "💎"
DAILY_GEM_REWARD = 15
