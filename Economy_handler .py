from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from config import CURRENCY_NAME, CURRENCY_SYMBOL, GEM_NAME, GEM_SYMBOL, DAILY_GEM_REWARD
from database import get_or_create_user, adjust_balance, adjust_gems, claim_daily_gems, record_purchase
from keyboards import shop_list_kb, shop_item_kb

router = Router(name="economy_handler")

# --- 🔗 Kizuna do'koni: o'yin ichidagi effektli narsalar (arzonlashtirildi, ko'paytirildi) ---
KIZUNA_SHOP = {
    "tirilish_tumori": {"name": "🔮 Tirilish Tumori", "desc": "Tunda o'ldirilsangiz, bir marta tirilib qolasiz.", "price": 90},
    "soya_pardasi": {"name": "🌫 Soya Pardasi", "desc": "Bir kechaga Meitantei tekshiruvidan yashirinasiz.", "price": 70},
    "qosh_ovoz": {"name": "⚡ Qo'sh Ovoz", "desc": "Kunduzgi ovoz berishda ovozingiz 2 marta hisoblanadi.", "price": 60},
    "vaqtinchalik_alibi": {"name": "🕵️ Vaqtinchalik Alibi", "desc": "Ovoz natijasida chiqarilishdan bir marta qutulasiz.", "price": 80},
    "ittifoq_qasamyodi": {"name": "🤝 Ittifoq Qasamyodi", "desc": "(Faqat Mafia) — sherigingizni darhol bilib olasiz.", "price": 50},
    "chaqmoq_zarbasi": {"name": "⚔️ Chaqmoq Zarbasi", "desc": "O'zingizni bir tunga himoya qilasiz (shifokorsiz ham).", "price": 75},
    "sodiqlik_nishoni": {"name": "🎖 Sodiqlik Nishoni", "desc": "Profilingizga maxsus unvon qo'yish huquqi.", "price": 45},
    "yolgon_iz": {"name": "🎭 Yolg'on Iz", "desc": "Detektiv sizni tekshirsa, natija noto'g'ri chiqadi.", "price": 65},
    "jim_tun": {"name": "🤐 Jim Tun", "desc": "Boshqa bir o'yinchining tungi qobiliyatini bir kechaga o'chirasiz.", "price": 70},
    "ikkinchi_imkoniyat": {"name": "🔁 Ikkinchi Imkoniyat", "desc": "Kunduzgi ovoz natijasi qayta hisoblanadi.", "price": 85},
}

# --- 💎 Sehirli Tosh bozori: faqat kosmetik, reytingga ta'sir qilmaydi (arzonlashtirildi, ko'paytirildi) ---
GEM_SHOP = {
    "ism_ozgartirish": {"name": "✍️ Ism O'zgartirish Kartasi", "desc": "O'yin ichidagi anime-ismingizni o'zingiz tanlaysiz.", "price": 3},
    "nodir_ramka": {"name": "🖼 Nodir Avatar Ramka", "desc": "Profilingizga bezakli ramka.", "price": 4},
    "vip_unvon": {"name": "👑 VIP Unvon: Afsonaviy Otaku", "desc": "Profilda ko'rinadigan dekorativ unvon.", "price": 5},
    "signature_emoji": {"name": "✨ Signature Emoji To'plami", "desc": "O'yin xabarlaringizga maxsus emoji qo'shiladi.", "price": 3},
    "baxt_tumori": {"name": "🍀 Baxt Tumori", "desc": "Profilda ko'rinadigan kosmetik tumor.", "price": 3},
    "fon_rasmi": {"name": "🌆 Statistika Fon Rasmi", "desc": "/profile kartochkangiz uchun fon.", "price": 4},
    "duo_kartasi": {"name": "🎴 Duo Kartasi", "desc": "Do'stingizni taklif qilsangiz ikkalangizga +5 💎.", "price": 2},
    "profil_banneri": {"name": "🖌 Profil Banneri", "desc": "Profil kartochkangiz uchun rangli banner.", "price": 4},
    "maxsus_stiker": {"name": "🎨 Maxsus Stiker To'plami", "desc": "O'yin davomida ishlatsa bo'ladigan stikerlar.", "price": 3},
    "rang_belgisi": {"name": "🌈 Ism Rangini O'zgartirish", "desc": "Aholi ismingiz o'yin xabarlarida rangli chiqadi.", "price": 5},
}


def _render_item_card(item: dict, symbol: str, currency: str) -> str:
    return f"{item['name']}\n\n<i>{item['desc']}</i>\n\n💰 Narxi: <b>{item['price']} {symbol} {currency}</b>"


# ---------------- Kizuna do'koni ----------------

@router.message(Command("shop"))
async def cmd_shop(message: Message):
    await message.answer(
        f"🛍 <b>Kizuna Do'koni</b> ({CURRENCY_SYMBOL} {CURRENCY_NAME} — o'yin natijasidan)\n"
        f"Mahsulotni tanlang:",
        reply_markup=shop_list_kb(KIZUNA_SHOP, "buy", CURRENCY_SYMBOL),
    )


@router.callback_query(F.data == "menu_shop")
async def on_menu_shop(callback: CallbackQuery):
    text = f"🛍 <b>Kizuna Do'koni</b> ({CURRENCY_SYMBOL} {CURRENCY_NAME} — o'yin natijasidan)\nMahsulotni tanlang:"
    kb = shop_list_kb(KIZUNA_SHOP, "buy", CURRENCY_SYMBOL)
    try:
        await callback.message.edit_text(text, reply_markup=kb)
    except Exception:
        await callback.message.answer(text, reply_markup=kb)
    await callback.answer()


@router.callback_query(F.data.startswith("buy:"))
async def on_pick_kizuna_item(callback: CallbackQuery):
    key = callback.data.split("buy:", 1)[1]
    item = KIZUNA_SHOP.get(key)
    if not item:
        await callback.answer("Topilmadi.", show_alert=True)
        return
    await callback.message.edit_text(
        _render_item_card(item, CURRENCY_SYMBOL, CURRENCY_NAME),
        reply_markup=shop_item_kb(key, "buy", "menu_shop"),
    )
    await callback.answer()


@router.callback_query(F.data.startswith("buy_confirm:"))
async def on_confirm_kizuna(callback: CallbackQuery):
    key = callback.data.split("buy_confirm:", 1)[1]
    item = KIZUNA_SHOP.get(key)
    if not item:
        await callback.answer("Topilmadi.", show_alert=True)
        return
    u = await get_or_create_user(
        callback.from_user.id, callback.from_user.username or "", callback.from_user.full_name
    )
    if u["balance"] < item["price"]:
        await callback.answer(f"Yetarli {CURRENCY_NAME} yo'q! Kerak: {item['price']}, sizda: {u['balance']}", show_alert=True)
        return
    await adjust_balance(callback.from_user.id, -item["price"])
    await record_purchase(callback.from_user.id, key, "kizuna")
    await callback.message.edit_text(f"✅ Xarid muvaffaqiyatli: {item['name']}!")
    await callback.answer("Xarid amalga oshirildi ✅")


# ---------------- Sehirli Tosh bozori ----------------

@router.message(Command("gemshop"))
async def cmd_gemshop(message: Message):
    await message.answer(
        f"💎 <b>Sehirli Tosh Bozori</b> ({GEM_SYMBOL} {GEM_NAME} — kunlik bonusdan, reytingga ta'sir qilmaydi)\n"
        f"Mahsulotni tanlang:",
        reply_markup=shop_list_kb(GEM_SHOP, "gbuy", GEM_SYMBOL),
    )


@router.callback_query(F.data == "menu_gemshop")
async def on_menu_gemshop(callback: CallbackQuery):
    text = f"💎 <b>Sehirli Tosh Bozori</b> ({GEM_SYMBOL} {GEM_NAME} — kunlik bonusdan, reytingga ta'sir qilmaydi)\nMahsulotni tanlang:"
    kb = shop_list_kb(GEM_SHOP, "gbuy", GEM_SYMBOL)
    try:
        await callback.message.edit_text(text, reply_markup=kb)
    except Exception:
        await callback.message.answer(text, reply_markup=kb)
    await callback.answer()


@router.callback_query(F.data.startswith("gbuy:"))
async def on_pick_gem_item(callback: CallbackQuery):
    key = callback.data.split("gbuy:", 1)[1]
    item = GEM_SHOP.get(key)
    if not item:
        await callback.answer("Topilmadi.", show_alert=True)
        return
    await callback.message.edit_text(
        _render_item_card(item, GEM_SYMBOL, GEM_NAME),
        reply_markup=shop_item_kb(key, "gbuy", "menu_gemshop"),
    )
    await callback.answer()


@router.callback_query(F.data.startswith("gbuy_confirm:"))
async def on_confirm_gem(callback: CallbackQuery):
    key = callback.data.split("gbuy_confirm:", 1)[1]
    item = GEM_SHOP.get(key)
    if not item:
        await callback.answer("Topilmadi.", show_alert=True)
        return
    u = await get_or_create_user(
        callback.from_user.id, callback.from_user.username or "", callback.from_user.full_name
    )
    if u["gems"] < item["price"]:
        await callback.answer(f"Yetarli {GEM_NAME} yo'q! Kerak: {item['price']}, sizda: {u['gems']}", show_alert=True)
        return
    await adjust_gems(callback.from_user.id, -item["price"])
    await record_purchase(callback.from_user.id, key, "gem")
    await callback.message.edit_text(f"✅ Xarid muvaffaqiyatli: {item['name']}!")
    await callback.answer("Xarid amalga oshirildi ✅")


# ---------------- Kunlik bonus va balans ----------------

@router.message(Command("daily"))
async def cmd_daily(message: Message):
    ok, remaining_h = await claim_daily_gems(message.from_user.id)
    if ok:
        await message.answer(f"{GEM_SYMBOL} Kunlik bonusingiz: <b>+{DAILY_GEM_REWARD} {GEM_NAME}</b>! Ertaga yana qayting 🙌")
    else:
        await message.answer(f"⏳ Kunlik bonusni allaqachon oldingiz. Yana {remaining_h} soatdan so'ng qayting.")


@router.callback_query(F.data == "menu_daily")
async def on_menu_daily(callback: CallbackQuery):
    ok, remaining_h = await claim_daily_gems(callback.from_user.id)
    if ok:
        await callback.message.answer(f"{GEM_SYMBOL} Kunlik bonusingiz: <b>+{DAILY_GEM_REWARD} {GEM_NAME}</b>! Ertaga yana qayting 🙌")
    else:
        await callback.message.answer(f"⏳ Kunlik bonusni allaqachon oldingiz. Yana {remaining_h} soatdan so'ng qayting.")
    await callback.answer()


@router.message(Command("balance"))
async def cmd_balance(message: Message):
    u = await get_or_create_user(
        message.from_user.id, message.from_user.username or "", message.from_user.full_name
    )
    await message.answer(f"{CURRENCY_SYMBOL} {CURRENCY_NAME}: <b>{u['balance']}</b>\n{GEM_SYMBOL} {GEM_NAME}: <b>{u['gems']}</b>")
