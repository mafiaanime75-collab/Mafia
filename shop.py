# ============ MAGAZIN ============
from telegram import Update
from telegram.ext import ContextTypes
from database import db
from keyboards import shop_categories_keyboard, stones_shop_keyboard, coins_shop_keyboard, back_to_main

async def shop_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Magazin kategoriyalari"""
    query = update.callback_query
    await query.answer()

    text = """
🛒 <b>MAGAZIN</b> 🛒

<b>Qaysi magazinga kirmoqchisiz?</b>

💎 <b>Sehrli toshlar magazini</b>
Kunlik bonus orqali olingan sehrli toshlarni maxsus narsalar sotib olish uchun ishlating!

🪙 <b>O'yin valyutasi magazini</b>
O'yinlarda g'alaba qozonib olingan tangalarni o'yin ichidagi kuchaytirgichlar sotib olish uchun ishlating!

👇 Kategoriyani tanlang:
    """

    await query.edit_message_text(text, reply_markup=shop_categories_keyboard(), parse_mode="HTML")

async def shop_stones_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sehrli toshlar magazini"""
    query = update.callback_query
    await query.answer()

    user = db.get_user(update.effective_user.id)
    user_level = user['daily_bonus_level'] if user else 1
    stones = user['stones'] if user else 0

    text = f"""
💎 <b>SEHRLI TOSHLAR MAGAZINI</b> 💎

<b>💰 Sizning balansingiz:</b> {stones} ta sehrli tosh

<b>📦 Mavjud tovarlar:</b>
(Pastdagi ro'yxatdan tanlang)

⚠️ Ba'zi tovarlar faqat ma'lum darajadan keyin ochiladi!
    """

    await query.edit_message_text(text, reply_markup=stones_shop_keyboard(user_level), parse_mode="HTML")

async def shop_coins_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """O'yin valyutasi magazini"""
    query = update.callback_query
    await query.answer()

    user = db.get_user(update.effective_user.id)
    user_level = user['daily_bonus_level'] if user else 1
    coins = user['coins'] if user else 0

    text = f"""
🪙 <b>O'YIN VALYUTASI MAGAZINI</b> 🪙

<b>💰 Sizning balansingiz:</b> {coins} ta tanga

<b>📦 Mavjud tovarlar:</b>
(Pastdagi ro'yxatdan tanlang)

⚠️ Ba'zi tovarlar faqat ma'lum darajadan keyin ochiladi!
    """

    await query.edit_message_text(text, reply_markup=coins_shop_keyboard(user_level), parse_mode="HTML")

async def buy_item_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Tovar sotib olish"""
    query = update.callback_query
    await query.answer()

    data = query.data
    parts = data.split("_")

    if len(parts) >= 4:
        currency = parts[1]  # stone yoki coin
        item_name = "_".join(parts[2:-1])
        try:
            price = int(parts[-1])
        except:
            price = 0

        user = db.get_user(update.effective_user.id)

        if currency == "stone":
            if user['stones'] >= price:
                # Sotib olish
                new_stones = user['stones'] - price
                inventory = user['inventory']
                inventory.append(item_name)

                db.update_user(update.effective_user.id, stones=new_stones, inventory=str(inventory))

                await query.edit_message_text(
                    f"✅ <b>Sotib olindi!</b>\n\n"
                    f"📦 {item_name}\n"
                    f"💎 {price} ta sehrli tosh sarflandi\n"
                    f"💰 Qolgan: {new_stones} ta sehrli tosh",
                    reply_markup=back_to_main(),
                    parse_mode="HTML"
                )
            else:
                await query.answer("❌ Yetarli sehrli tosh yo'q!", show_alert=True)

        elif currency == "coin":
            if user['coins'] >= price:
                # Sotib olish
                new_coins = user['coins'] - price
                inventory = user['inventory']
                inventory.append(item_name)

                db.update_user(update.effective_user.id, coins=new_coins, inventory=str(inventory))

                await query.edit_message_text(
                    f"✅ <b>Sotib olindi!</b>\n\n"
                    f"📦 {item_name}\n"
                    f"🪙 {price} ta tanga sarflandi\n"
                    f"💰 Qolgan: {new_coins} ta tanga",
                    reply_markup=back_to_main(),
                    parse_mode="HTML"
                )
            else:
                await query.answer("❌ Yetarli tanga yo'q!", show_alert=True)

async def locked_item_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bloklangan tovar"""
    query = update.callback_query
    await query.answer("🔒 Bu tovarni sotib olish uchun yuqori daraja kerak!", show_alert=True)
