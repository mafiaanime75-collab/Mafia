# ============ REYTING ============
from telegram import Update
from telegram.ext import ContextTypes
from database import db
from keyboards import rating_keyboard, back_to_main
from config import LEAGUES

async def rating_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Reyting sahifasi"""
    query = update.callback_query
    await query.answer()

    text = """
📊 <b>REYTING</b> 📊

<b>Qaysi reytingni ko'rmoqchisiz?</b>

🌍 <b>Global reyting</b>
Butun dunyo bo'ylab eng yaxshi o'yinchilar

👥 <b>Do'stlar reytingi</b>
Sizning do'stlaringiz orasida eng yaxshilar

👇 Tanlang:
    """

    await query.edit_message_text(text, reply_markup=rating_keyboard(), parse_mode="HTML")

async def global_rating_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Global reyting"""
    query = update.callback_query
    await query.answer()

    top_users = db.get_top_users(20)

    if not top_users:
        await query.edit_message_text(
            "📊 <b>Global reyting bo'sh!</b>\n\n"
            "Hali hech kim o'yin o'namagan. Birinchi bo'lib o'ynang!",
            reply_markup=back_to_main(),
            parse_mode="HTML"
        )
        return

    rating_text = ""
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    for i, user in enumerate(top_users[:20]):
        medal = medals[i] if i < 10 else f"{i+1}."
        name = user[2] or user[1] or "Noma\'lum"
        league_info = LEAGUES.get(user[5], LEAGUES[1])
        rating_text += f"\n{medal} <b>{name}</b> - {user[3]} ⭐ ({league_info['name']})"

    text = f"""
🌍 <b>GLOBAL REYTING</b> 🌍

<b>Top 20 eng yaxshi o'yinchii:</b>
{rating_text}

<b>💡 Maslahat:</b>
Ko'proq o'yin o'ynang va g'alaba qozoning - reytingingiz oshadi!
    """

    await query.edit_message_text(text, reply_markup=back_to_main(), parse_mode="HTML")

async def friends_rating_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Do'stlar reytingi"""
    query = update.callback_query
    await query.answer()

    text = """
👥 <b>DO'STLAR REYTINGI</b> 👥

Bu funksiya tez orada qo'shiladi! 📅

<b>💡 Hozircha:</b>
Global reytingni ko'rib, o'z o'rningizni bilib oling!
    """

    await query.edit_message_text(text, reply_markup=back_to_main(), parse_mode="HTML")
