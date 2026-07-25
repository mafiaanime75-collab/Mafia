# ============ TUGMALAR ============
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import MAIN_GROUP_LINK

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🤖 Botni guruhga ulash", url="https://t.me/AniMafiaBot?startgroup=true")],
        [InlineKeyboardButton("👥 Asosiy guruhga qo'shilish", url=MAIN_GROUP_LINK)],
        [InlineKeyboardButton("🛒 Magazin", callback_data="shop")],
        [InlineKeyboardButton("👤 Profil", callback_data="profile"),
         InlineKeyboardButton("🏆 Liga", callback_data="league")],
        [InlineKeyboardButton("📊 Reyting", callback_data="rating"),
         InlineKeyboardButton("🎁 Kunlik bonus", callback_data="daily_bonus")],
        [InlineKeyboardButton("📜 Qoidalar", callback_data="rules"),
         InlineKeyboardButton("💬 Taklif/Shikoyat", callback_data="feedback")],
    ]
    return InlineKeyboardMarkup(keyboard)

def shop_categories_keyboard():
    keyboard = [
        [InlineKeyboardButton("💎 Sehrli toshlar magazini", callback_data="shop_stones")],
        [InlineKeyboardButton("🪙 O'yin valyutasi magazini", callback_data="shop_coins")],
        [InlineKeyboardButton("🔙 Orqaga", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def stones_shop_keyboard(user_level=1):
    items = [
        {"name": "🎨 Anime fon", "price": 50, "level": 1},
        {"name": "✨ Yorqin nik", "price": 100, "level": 1},
        {"name": "🎭 Maxsus avatar", "price": 200, "level": 2},
        {"name": "🏅 Bronza unvoni", "price": 300, "level": 2},
        {"name": "💫 Sehrli effekt", "price": 500, "level": 3},
        {"name": "👑 Oltin unvoni", "price": 800, "level": 3},
        {"name": "🔥 Alovli ramka", "price": 1200, "level": 4},
        {"name": "💎 Olmos unvoni", "price": 2000, "level": 4},
        {"name": "🌟 Koinot fon", "price": 3500, "level": 5},
        {"name": "⚡ Afsona unvoni", "price": 5000, "level": 5},
        {"name": "🌌 Sehrli olam", "price": 8000, "level": 6},
        {"name": "👁️ Xudo unvoni", "price": 12000, "level": 6},
        {"name": "🎆 Koinot effekti", "price": 20000, "level": 7},
        {"name": "🔮 Koinot unvoni", "price": 30000, "level": 7},
        {"name": "🌈 Sehrli qanot", "price": 50000, "level": 8},
        {"name": "⭐ Afsonaviy unvon", "price": 75000, "level": 8},
    ]

    keyboard = []
    for item in items:
        if user_level >= item["level"]:
            keyboard.append([InlineKeyboardButton(
                f"{item['name']} - {item['price']}💎", 
                callback_data=f"buy_stone_{item['name']}_{item['price']}"
            )])
        else:
            keyboard.append([InlineKeyboardButton(
                f"🔒 {item['name']} - {item['level']}-daraja talab", 
                callback_data="locked"
            )])

    keyboard.append([InlineKeyboardButton("🔙 Orqaga", callback_data="shop")])
    return InlineKeyboardMarkup(keyboard)

def coins_shop_keyboard(user_level=1):
    items = [
        {"name": "🎯 Ikki marta urinish", "price": 100, "level": 1},
        {"name": "🛡️ Himoya qalqoni", "price": 250, "level": 1},
        {"name": "🔍 Sehrli ko'z", "price": 400, "level": 2},
        {"name": "⚡ Tezlik kuchaytirgichi", "price": 600, "level": 2},
        {"name": "🎲 Qayta tashlash", "price": 800, "level": 3},
        {"name": "💀 Maxsus qotil", "price": 1200, "level": 3},
        {"name": "🌙 Tungi ko'z", "price": 1500, "level": 4},
        {"name": "🔥 Alovli qilich", "price": 2000, "level": 4},
        {"name": "💫 Sehrli portlash", "price": 3000, "level": 5},
        {"name": "👁️ Rux ko'rish", "price": 4500, "level": 5},
        {"name": "⚔️ Afsonaviy qurol", "price": 6000, "level": 6},
        {"name": "🌟 Sehrli himoya", "price": 8000, "level": 6},
        {"name": "🔮 Koinot kuchi", "price": 12000, "level": 7},
        {"name": "💎 Olmos qurol", "price": 18000, "level": 7},
        {"name": "🌌 Afsonaviy kuch", "price": 25000, "level": 8},
        {"name": "⭐ Xudo quroli", "price": 35000, "level": 8},
    ]

    keyboard = []
    for item in items:
        if user_level >= item["level"]:
            keyboard.append([InlineKeyboardButton(
                f"{item['name']} - {item['price']}🪙", 
                callback_data=f"buy_coin_{item['name']}_{item['price']}"
            )])
        else:
            keyboard.append([InlineKeyboardButton(
                f"🔒 {item['name']} - {item['level']}-daraja talab", 
                callback_data="locked"
            )])

    keyboard.append([InlineKeyboardButton("🔙 Orqaga", callback_data="shop")])
    return InlineKeyboardMarkup(keyboard)

def profile_keyboard():
    keyboard = [
        [InlineKeyboardButton("📦 Inventar", callback_data="inventory")],
        [InlineKeyboardButton("📊 Statistika", callback_data="stats")],
        [InlineKeyboardButton("🔙 Asosiy menyu", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def league_keyboard():
    keyboard = [
        [InlineKeyboardButton("📈 Liga haqida", callback_data="league_info")],
        [InlineKeyboardButton("🏆 Liga reytingi", callback_data="league_rating")],
        [InlineKeyboardButton("🔙 Asosiy menyu", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def rating_keyboard():
    keyboard = [
        [InlineKeyboardButton("🌍 Global reyting", callback_data="global_rating")],
        [InlineKeyboardButton("👥 Do'stlar reytingi", callback_data="friends_rating")],
        [InlineKeyboardButton("🔙 Asosiy menyu", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def daily_bonus_keyboard(can_claim=True):
    if can_claim:
        keyboard = [
            [InlineKeyboardButton("🎁 Bonus olish", callback_data="claim_bonus")],
            [InlineKeyboardButton("📊 Daraja haqida", callback_data="bonus_info")],
            [InlineKeyboardButton("🔙 Asosiy menyu", callback_data="main_menu")]
        ]
    else:
        keyboard = [
            [InlineKeyboardButton("⏳ Bonus allaqachon olingan", callback_data="bonus_claimed")],
            [InlineKeyboardButton("📊 Daraja haqida", callback_data="bonus_info")],
            [InlineKeyboardButton("🔙 Asosiy menyu", callback_data="main_menu")]
        ]
    return InlineKeyboardMarkup(keyboard)

def feedback_keyboard():
    keyboard = [
        [InlineKeyboardButton("💡 Taklif", callback_data="feedback_suggestion")],
        [InlineKeyboardButton("⚠️ Shikoyat", callback_data="feedback_complaint")],
        [InlineKeyboardButton("🔙 Asosiy menyu", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def admin_keyboard():
    keyboard = [
        [InlineKeyboardButton("📨 Yangi xabarlar", callback_data="admin_feedback_new")],
        [InlineKeyboardButton("📖 O'qilgan xabarlar", callback_data="admin_feedback_read")],
        [InlineKeyboardButton("📊 Bot statistikasi", callback_data="admin_stats")],
        [InlineKeyboardButton("🔙 Asosiy menyu", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def anime_select_keyboard(anime_list, page=0):
    per_page = 10
    start = page * per_page
    end = start + per_page
    current_anime = list(anime_list.items())[start:end]

    keyboard = []
    for anime_name, anime_data in current_anime:
        keyboard.append([InlineKeyboardButton(
            f"{anime_data['icon']} {anime_name}",
            callback_data=f"select_anime_{anime_name}"
        )])

    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton("⬅️ Oldingi", callback_data=f"anime_page_{page-1}"))
    if end < len(anime_list):
        nav_buttons.append(InlineKeyboardButton("Keyingi ➡️", callback_data=f"anime_page_{page+1}"))

    if nav_buttons:
        keyboard.append(nav_buttons)

    keyboard.append([InlineKeyboardButton("🔍 Qidirish", callback_data="search_anime")])
    keyboard.append([InlineKeyboardButton("❌ Bekor qilish", callback_data="cancel_game")])

    return InlineKeyboardMarkup(keyboard)

def join_game_keyboard(game_id):
    keyboard = [
        [InlineKeyboardButton("➕ O'yini qo'shilish", url=f"https://t.me/AniMafiaBot?start=join_{game_id}")]
    ]
    return InlineKeyboardMarkup(keyboard)

def back_to_main():
    keyboard = [
        [InlineKeyboardButton("🔙 Asosiy menyu", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)
