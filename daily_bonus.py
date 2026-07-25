# ============ KUNLIK BONUS ============
from telegram import Update
from telegram.ext import ContextTypes
from database import db
from keyboards import daily_bonus_keyboard, back_to_main
from config import DAILY_BONUS_LEVELS
from datetime import datetime, timedelta

async def daily_bonus_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Kunlik bonus sahifasi"""
    query = update.callback_query
    await query.answer()

    user_data = db.get_user(update.effective_user.id)

    if not user_data:
        await query.edit_message_text(
            "❌ Ma'lumot topilmadi! /start ni bosing.",
            reply_markup=back_to_main()
        )
        return

    # Bonus olish mumkinligini tekshirish
    can_claim = True
    last_bonus = user_data['last_daily_bonus']
    time_text = ""

    if last_bonus:
        last_date = datetime.fromisoformat(last_bonus)
        now = datetime.now()
        if (now - last_date).days < 1:
            can_claim = False
            time_left = last_date + timedelta(days=1) - now
            hours_left = int(time_left.total_seconds() // 3600)
            minutes_left = int((time_left.total_seconds() % 3600) // 60)
            time_text = f"⏳ Keyingi bonus: {hours_left} soat {minutes_left} daqiqa"
        else:
            time_text = "✅ Bonus olish mumkin!"
    else:
        time_text = "✅ Bonus olish mumkin!"

    current_level = user_data['daily_bonus_level']
    level_info = DAILY_BONUS_LEVELS.get(current_level, DAILY_BONUS_LEVELS[1])
    streak = user_data['daily_bonus_streak']

    # Keyingi daraja haqida
    next_level = DAILY_BONUS_LEVELS.get(current_level + 1)
    next_text = f"\n\n📈 Keyingi daraja: {next_level['name']} ({next_level['days']} kun ketma-ketlik)" if next_level else "\n\n🎉 Siz eng yuqori darajadasiz!"

    text = f"""
🎁 <b>KUNLIK BONUS</b> 🎁

<b>💎 Sizning darajangiz:</b> {level_info['name']}
<b>🔥 Ketma-ketlik:</b> {streak} kun
<b>💰 Har kuni:</b> {level_info['stones']} ta sehrli tosh

{time_text}
{next_text}

<b>📊 Darajalar:</b>
• 🥉 Bronza - 3 kun (10 tosh)
• 🥈 Kumush - 5 kun (25 tosh)
• 🥇 Oltin - 8 kun (50 tosh)
• 💎 Olmos - 12 kun (100 tosh)
• 👑 Qirol - 17 kun (200 tosh)
• 🔥 Afsona - 25 kun (500 tosh)
• ⚡ Xudo - 35 kun (1000 tosh)
• 🌌 Koinot - 50 kun (2500 tosh)

<b>💡 Maslahat:</b>
Har kuni bonus oling va darajangizni oshiring!
    """

    await query.edit_message_text(text, reply_markup=daily_bonus_keyboard(can_claim), parse_mode="HTML")

async def claim_bonus_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bonus olish"""
    query = update.callback_query
    await query.answer()

    user_data = db.get_user(update.effective_user.id)

    if not user_data:
        await query.answer("❌ Xatolik!", show_alert=True)
        return

    # Tekshirish
    last_bonus = user_data['last_daily_bonus']
    if last_bonus:
        last_date = datetime.fromisoformat(last_bonus)
        if (datetime.now() - last_date).days < 1:
            await query.answer("❌ Bonus allaqachon olingan!", show_alert=True)
            return

    # Bonus berish
    current_level = user_data['daily_bonus_level']
    level_info = DAILY_BONUS_LEVELS.get(current_level, DAILY_BONUS_LEVELS[1])

    # Ketma-ketlikni tekshirish
    streak = user_data['daily_bonus_streak'] + 1

    # Darajani tekshirish
    new_level = current_level
    next_level = DAILY_BONUS_LEVELS.get(current_level + 1)
    if next_level and streak >= next_level['days']:
        new_level = current_level + 1
        level_up_text = f"\n\n🎉 <b>Tabriklaymiz!</b> Siz {next_level['name']} darajasiga ko'tarildingiz!"
    else:
        level_up_text = ""

    stones = level_info['stones']

    # Bazaga yozish
    db.update_user(
        update.effective_user.id,
        stones=user_data['stones'] + stones,
        daily_bonus_streak=streak,
        last_daily_bonus=datetime.now().isoformat(),
        daily_bonus_level=new_level
    )

    text = f"""
✅ <b>Bonus olindi!</b>

💎 {stones} ta sehrli tosh qo'shildi
🔥 Ketma-ketlik: {streak} kun
{level_up_text}

<b>💰 Jami balans:</b> {user_data['stones'] + stones} ta sehrli tosh
    """

    await query.edit_message_text(text, reply_markup=back_to_main(), parse_mode="HTML")
