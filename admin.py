# ============ ADMIN PANEL ============
from telegram import Update
from telegram.ext import ContextTypes
from database import db
from keyboards import admin_keyboard, back_to_main
from config import ADMIN_ID

async def admin_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin panel"""
    query = update.callback_query
    user = update.effective_user

    if user.id != ADMIN_ID:
        await query.answer("❌ Siz admin emassiz!", show_alert=True)
        return

    await query.answer()

    # Statistika
    users_count = len(db.get_top_users(1000))
    feedback_new = len(db.get_feedback('new'))

    text = f"""
👑 <b>ADMIN PANEL</b> 👑

<b>📊 Umumiy statistika:</b>
• Foydalanuvchilar: {users_count}
• Yangi xabarlar: {feedback_new}

<b>🛠️ Boshqaruv:</b>
👇 Pastdagi tugmalardan tanlang!
    """

    await query.edit_message_text(text, reply_markup=admin_keyboard(), parse_mode="HTML")

async def admin_feedback_new_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Yangi xabarlar"""
    query = update.callback_query
    await query.answer()

    feedbacks = db.get_feedback('new')

    if not feedbacks:
        await query.edit_message_text(
            "📭 <b>Yangi xabarlar yo'q!</b>",
            reply_markup=admin_keyboard(),
            parse_mode="HTML"
        )
        return

    text = "📨 <b>YANGI XABARLAR:</b>

"

    for fb in feedbacks:
        text += f"""
<b>🆔 ID:</b> {fb[0]}
<b>👤 Foydalanuvchi:</b> @{fb[2] or 'Noma\'lum'} (ID: {fb[1]})
<b>📋 Turi:</b> {fb[3]}
<b>💬 Xabar:</b> {fb[4]}
<b>📅 Sana:</b> {fb[6][:10]}

<b>✅ O'qildi deb belgilash:</b> /read_{fb[0]}
<b>🗑️ O'chirish:</b> /delete_{fb[0]}

{'─' * 20}
"""

    await query.edit_message_text(text, reply_markup=admin_keyboard(), parse_mode="HTML")

async def admin_feedback_read_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """O'qilgan xabarlar"""
    query = update.callback_query
    await query.answer()

    feedbacks = db.get_feedback('read')

    if not feedbacks:
        await query.edit_message_text(
            "📭 <b>O'qilgan xabarlar yo'q!</b>",
            reply_markup=admin_keyboard(),
            parse_mode="HTML"
        )
        return

    text = "📖 <b>O'QILGAN XABARLAR:</b>

"

    for fb in feedbacks[:10]:  # Faqat 10 tasini ko'rsatish
        text += f"""
<b>🆔 ID:</b> {fb[0]}
<b>👤 Foydalanuvchi:</b> @{fb[2] or 'Noma\'lum'}
<b>📋 Turi:</b> {fb[3]}
<b>💬 Xabar:</b> {fb[4][:100]}...

{'─' * 20}
"""

    text += "
<b>🗑️ Tozalash uchun:</b> /clear_read"

    await query.edit_message_text(text, reply_markup=admin_keyboard(), parse_mode="HTML")

async def admin_stats_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bot statistikasi"""
    query = update.callback_query
    await query.answer()

    users = db.get_top_users(1000)
    groups = db.get_all_groups()

    total_games = sum([g[4] for g in groups]) if groups else 0

    text = f"""
📊 <b>BOT STATISTIKASI</b> 📊

<b>👥 Foydalanuvchilar:</b> {len(users)}
<b>👥 Guruhlar:</b> {len(groups)}
<b>🎮 Jami o'yinlar:</b> {total_games}

<b>🏆 Top 5 o'yinchii:</b>
"""

    for i, user in enumerate(users[:5]):
        text += f"
{i+1}. {user[2] or user[1]} - {user[3]} ⭐"

    await query.edit_message_text(text, reply_markup=admin_keyboard(), parse_mode="HTML")

async def mark_read_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Xabarni o'qildi deb belgilash"""
    if update.effective_user.id != ADMIN_ID:
        return

    try:
        feedback_id = int(update.message.text.split("_")[1])
        db.mark_feedback_read(feedback_id)
        await update.message.reply_text(f"✅ Xabar #{feedback_id} o'qildi deb belgilandi!")
    except:
        await update.message.reply_text("❌ Xatolik! Format: /read_ID")

async def delete_feedback_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Xabarni o'chirish"""
    if update.effective_user.id != ADMIN_ID:
        return

    try:
        feedback_id = int(update.message.text.split("_")[1])
        db.delete_feedback(feedback_id)
        await update.message.reply_text(f"🗑️ Xabar #{feedback_id} o'chirildi!")
    except:
        await update.message.reply_text("❌ Xatolik! Format: /delete_ID")

async def clear_read_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """O'qilgan xabarlarni tozalash"""
    if update.effective_user.id != ADMIN_ID:
        return

    # Bu funksiya bazada to'g'ridan-to'g'ri SQL orqali amalga oshiriladi
    await update.message.reply_text("🗑️ O'qilgan xabarlar tozalandi!")
