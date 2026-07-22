
# Barcha fayllarni to'liq o'zbek tilida yaratamiz

# 1. config.py - Konfiguratsiya
config_content = '''# ============ ANIMAFIA BOT KONFIGURATSIYA ============
# ⚠️ BU YERGA O'ZGARTIRISH KIRITING!

# Bot token (BotFather'dan olingan)
BOT_TOKEN = "8613383536:AAFtxKbwkbo6jwpU_AI-oHdoHLstw-8DcjE"

# Admin ID (6060306988)
# @userinfobot dan olishingiz mumkin
ADMIN_ID = 6060306988

# Asosiy guruh havolasi
MAIN_GROUP_LINK = "https://t.me/+j5SvFE1hj75iNzUy"

# O'yin sozlamalari
MIN_PLAYERS = 4
MAX_PLAYERS = 20

# Kunlik bonus darajalari
DAILY_BONUS_LEVELS = {
    1: {"days": 3, "stones": 10, "name": "🥉 Bronza"},
    2: {"days": 5, "stones": 25, "name": "🥈 Kumush"},
    3: {"days": 8, "stones": 50, "name": "🥇 Oltin"},
    4: {"days": 12, "stones": 100, "name": "💎 Olmos"},
    5: {"days": 17, "stones": 200, "name": "👑 Qirol"},
    6: {"days": 25, "stones": 500, "name": "🔥 Afsona"},
    7: {"days": 35, "stones": 1000, "name": "⚡ Xudo"},
    8: {"days": 50, "stones": 2500, "name": "🌌 Koinot"},
}

# Liga darajalari
LEAGUES = {
    1: {"name": "🥉 Bronza Liga", "min_games": 0, "icon": "🥉"},
    2: {"name": "🥈 Kumush Liga", "min_games": 10, "icon": "🥈"},
    3: {"name": "🥇 Oltin Liga", "min_games": 30, "icon": "🥇"},
    4: {"name": "💎 Olmos Liga", "min_games": 60, "icon": "💎"},
    5: {"name": "👑 Qirol Liga", "min_games": 100, "icon": "👑"},
    6: {"name": "🔥 Afsona Liga", "min_games": 150, "icon": "🔥"},
    7: {"name": "⚡ Xudo Liga", "min_games": 220, "icon": "⚡"},
    8: {"name": "🌌 Koinot Liga", "min_games": 300, "icon": "🌌"},
}
'''

with open('/mnt/agents/output/animafia_bot/config.py', 'w', encoding='utf-8') as f:
    f.write(config_content)

print("✅ config.py yaratildi!")
