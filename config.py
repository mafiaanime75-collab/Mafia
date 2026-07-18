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

_admin_ids_raw = os.getenv("6060306988", "")
# Vergul, bo'sh joy yoki qator ko'chirish bilan ajratilgan bo'lishi mumkin
_admin_ids_from_env = {
    int(tok) for tok in _admin_ids_raw.replace(",", " ").replace(";", " ").split()
    if tok.strip().lstrip("-").isdigit()
}

# AGAR .env bilan ishlash noqulay bo'lsa — ID'ingizni to'g'ridan-to'g'ri
# shu yerga, qavs ichiga yozishingiz ham mumkin (masalan: {123456789}):
ADMIN_IDS_HARDCODED: set[int] = set()

ADMIN_IDS = _admin_ids_from_env | ADMIN_IDS_HARDCODED

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
