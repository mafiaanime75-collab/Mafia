"""
Bot konfiguratsiyasi.
Token va guruh linkini shu yerga (yoki muhit o'zgaruvchilariga) kiriting.
"""
import os

# Bot tokeningizni shu yerga yozing yoki BOT_TOKEN muhit o'zgaruvchisidan oling
BOT_TOKEN = os.getenv("BOT_TOKEN", "SIZNING_BOT_TOKENINGIZ_BU_YERGA")

# Asosiy o'yin o'ynaladigan guruh (lobby'dan keyin o'yinchilar shu yerga o'tadi)
MAIN_GROUP_ID = int(os.getenv("MAIN_GROUP_ID", "-1000000000000"))
MAIN_GROUP_INVITE_LINK = os.getenv("MAIN_GROUP_INVITE_LINK", "https://t.me/sizning_guruhingiz")

DB_PATH = os.getenv("DB_PATH", "anime_mafia.db")

# O'yin sozlamalari
MIN_PLAYERS = 5
MAX_PLAYERS = 20
NIGHT_DURATION_SEC = 45
DAY_DISCUSSION_SEC = 90
VOTING_DURATION_SEC = 40

# Valyuta nomi (o'zgaruvchan qilib chiqarildi - kerak bo'lsa almashtiring)
CURRENCY_NAME = "Kizuna"
CURRENCY_SYMBOL = "🔗"
