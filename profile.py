# ============ PROFIL ============
from telegram import Update
from telegram.ext import ContextTypes
from database import db
from keyboards import profile_keyboard, back_to_main
from config import LEAGUES

async def profile_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Foydalanuvchi profili"""
    query = update.callback_query
    await query.answer()

    user = update.effective_user
    user_data = db.get_user(user.id)

    if not user_data:
        await query.edit_message_text(
            "❌ Ma'lumot topilmadi! Iltimos, /start ni bosing.",
            reply_markup=back_to_main()
        )
        return

    league_info = LEAGUES.get(user_data['league'], LEAGUES[1])
    next_league = LEAGUES.get(user_data['league'] + 1)

    win_rate = 0
    if user_data['games_played'] > 0:
        win_rate = round((user_data['games_won'] / user_data['games_played']) * 100, 1)

    text = f"""
👤 <b>PROFIL</b> 👤

<b>📝 Ism:</b> {user_data['first_name']}
<b>🆔 ID:</b> <code>{user.id}</code>
<b>📛 Username:</b> @{user_data['username'] or 'yo\'q'}

<b>💎 Sehrli toshlar:</b> {user_data['stones']}
<b>🪙 Tangalar:</b> {user_data['coins']}

<b>🎮 Statistika:</b>
• O'ynalgan o'yinlar: {user_data['games_played']}
• G'alabalar: {user_data['games_won']} ✅
• Mag'lubiyatlar: {user_data['games_lost']} ❌
• G'alaba foizi: {win_rate}%
• Reyting: {user_data['rating']} ⭐

<b>🏆 Liga:</b> {league_info['name']}
{"• Keyingi liga: " + next_league['name'] + " (" + str(next_league['min_games']) + " o'yin)" if next_league else "• Siz eng yuqori ligadasiz! 🎉"}

<b>🎁 Kunlik bonus darajasi:</b> {user_data['daily_bonus_level']}
<b>🔥 Ketma-ketlik:</b> {user_data['daily_bonus_streak']} kun

<b>📦 Inventar:</b> {len(user_data['inventory'])} ta narsa
    """

    await query.edit_message_text(text, reply_markup=profile_keyboard(), parse_mode="HTML")

async def inventory_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Inventar ko'rish"""
    query = update.callback_query
    await query.answer()

    user_data = db.get_user(update.effective_user.id)

    if not user_data or not user_data['inventory']:
        await query.edit_message_text(
            "📦 <b>Inventar bo'sh!</b>\n\n"
            "Magazinga o'tib narsalar sotib oling!",
            reply_markup=back_to_main(),
            parse_mode="HTML"
        )
        return

    items_text = "\n".join([f"• {item}" for item in user_data['inventory']])

    text = f"""
📦 <b>INVENTAR</b> 📦

<b>Sizning narsalaringiz:</b>
{items_text}

<b>Jami:</b> {len(user_data['inventory'])} ta narsa
    """

    await query.edit_message_text(text, reply_markup=back_to_main(), parse_mode="HTML")

async def stats_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Batafsil statistika"""
    query = update.callback_query
    await query.answer()

    user_data = db.get_user(update.effective_user.id)

    if not user_data:
        await query.edit_message_text(
            "❌ Ma'lumot topilmadi!",
            reply_markup=back_to_main()
        )
        return

    win_rate = 0
    if user_data['games_played'] > 0:
        win_rate = round((user_data['games_won'] / user_data['games_played']) * 100, 1)

    text = f"""
📊 <b>BATAFSIL STATISTIKA</b> 📊

<b>🎮 O'yinlar:</b>
• Jami: {user_data['games_played']}
• G'alaba: {user_data['games_won']}
• Mag'lubiyat: {user_data['games_lost']}
• G'alaba foizi: {win_rate}%

<b>⭐ Reyting:</b> {user_data['rating']}

<b>💰 Boylik:</b>
• Sehrli toshlar: {user_data['stones']}
• Tangalar: {user_data['coins']}

<b>🎁 Bonus:</b>
• Daraja: {user_data['daily_bonus_level']}
• Ketma-ketlik: {user_data['daily_bonus_streak']} kun

<b>📅 Ro'yxatdan o'tgan:</b> {user_data['created_at'][:10] if user_data['created_at'] else 'Noma\'lum'}
    """

    await query.edit_message_text(text, reply_markup=back_to_main(), parse_mode="HTML")
