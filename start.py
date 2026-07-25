# ============ START VA ASOSIY MENU ============
from telegram import Update
from telegram.ext import ContextTypes
from database import db
from keyboards import main_menu_keyboard
from config import ADMIN_ID

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start komandasi"""
    user = update.effective_user

    # Foydalanuvchini bazaga qo'shish
    db.add_user(user.id, user.username, user.first_name, user.last_name)

    # Agar join parametr bo'lsa (o'yini qo'shilish)
    if context.args and len(context.args) > 0:
        arg = context.args[0]
        if arg.startswith("join_"):
            game_id = int(arg.split("_")[1])
            # O'yini qo'shilish logikasi (game.py da)
            from handlers.game import join_game
            await join_game(update, context, game_id)
            return

    # Asosiy xabar
    welcome_text = f"""
🎌 <b>Xush kelibsiz, {user.first_name}!</b> 🎌

<b>🎮 AniMafia</b> - anime uslubidagi eng zor Mafia o'yini!

<b>✨ Nimalar bor:</b>
• 🌸 30+ turli anime olami
• 🎭 Anime personajlari bilan o'ynash
• 🛒 Magazin va valyuta tizimi
• 🏆 Liga va reyting tizimi
• 🎁 Kunlik bonuslar
• 👥 Do'stlar bilan o'ynash

<b>🚀 Qanday boshlash:</b>
1. Botni o'z guruhigizga qo'shing
2. "Yangi o'yin boshlash" ni bosing
3. Sevimli anime olamingizni tanlang
4. Do'stlaringizni taklif qiling!

<b>💡 Maslahat:</b> O'yinni boshlash uchun pastdagi tugmalardan foydalaning!
    """

    # Admin uchun qo'shimcha
    if user.id == ADMIN_ID:
        welcome_text += "\n\n👑 <b>Siz admin sifatida tizimga kirdingiz!</b>"

    await update.message.reply_text(
        welcome_text,
        reply_markup=main_menu_keyboard(),
        parse_mode="HTML"
    )

async def main_menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Asosiy menyuga qaytish"""
    query = update.callback_query
    await query.answer()

    user = update.effective_user

    menu_text = f"""
🎌 <b>AniMafia - Asosiy Menyu</b> 🎌

Salom, {user.first_name}! 👋

<b>📊 Sizning ma'lumotlaringiz:</b>
• 🎮 O'ynalgan o'yinlar: Tekshirish uchun "Profil" ga o'ting
• 💎 Sehrli toshlar: Tekshirish uchun "Profil" ga o'ting
• 🪙 Tangalar: Tekshirish uchun "Profil" ga o'ting

<b>🎯 Tezkor harakatlar:</b>
👇 Pastdagi tugmalardan birini tanlang!
    """

    await query.edit_message_text(
        menu_text,
        reply_markup=main_menu_keyboard(),
        parse_mode="HTML"
    )
