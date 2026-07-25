# ============ TAKLIF VA SHIKOYAT ============
from telegram import Update
from telegram.ext import ContextTypes
from database import db
from keyboards import feedback_keyboard, back_to_main

# Conversation states
WAITING_FOR_FEEDBACK = 1

async def feedback_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Taklif va shikoyat sahifasi"""
    query = update.callback_query
    await query.answer()

    text = """
💬 <b>TAKLIF VA SHIKOYAT</b> 💬

<b>Nima xabar qilmoqchisiz?</b>

💡 <b>Taklif</b> - Botni yaxshilash uchun g'oyalar
⚠️ <b>Shikoyat</b> - Muammolar yoki xatolar haqida

👇 Turini tanlang:
    """

    await query.edit_message_text(text, reply_markup=feedback_keyboard(), parse_mode="HTML")

async def feedback_type_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Taklif yoki shikoyat turi"""
    query = update.callback_query
    await query.answer()

    feedback_type = "taklif" if "suggestion" in query.data else "shikoyat"
    context.user_data['feedback_type'] = feedback_type

    text = f"""
💬 <b>{feedback_type.upper()}</b>

Iltimos, xabaringizni yozib yuboring:

✍️ Matn kiriting...
    """

    await query.edit_message_text(text, parse_mode="HTML")

async def receive_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Xabarni qabul qilish"""
    user = update.effective_user
    message = update.message.text
    feedback_type = context.user_data.get('feedback_type', 'taklif')

    # Bazaga saqlash
    db.add_feedback(user.id, user.username, feedback_type, message)

    await update.message.reply_text(
        f"""
✅ <b>Xabaringiz qabul qilindi!</b>

<b>📋 Turi:</b> {feedback_type.capitalize()}
<b>💬 Xabar:</b> {message[:100]}{'...' if len(message) > 100 else ''}

<b>🙏 Rahmat! Bizning botimizni yaxshilashga yordam berganingiz uchun!</b>
        """,
        reply_markup=back_to_main(),
        parse_mode="HTML"
    )

    # Admin ga xabar
    from config import ADMIN_ID
    try:
        await context.bot.send_message(
            ADMIN_ID,
            f"""
📨 <b>YANGI XABAR!</b>

<b>👤 Foydalanuvchi:</b> @{user.username or 'Noma\'lum'} (ID: {user.id})
<b>📋 Turi:</b> {feedback_type.capitalize()}
<b>💬 Xabar:</b> {message}

<b>✅ O'qildi deb belgilash:</b> /read_ID
            """,
            parse_mode="HTML"
        )
    except:
        pass

async def cancel_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bekor qilish"""
    await update.message.reply_text(
        "❌ Bekor qilindi.",
        reply_markup=back_to_main()
    )
