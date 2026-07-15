"""
Ikki alohida iqtisod:

1) 🔗 KIZUNA — faqat o'yin natijasidan (g'alaba/mag'lubiyat/MVP) olinadi.
   Do'koni o'yin ICHIDAGI kuchli effektlarga ega (tirilish, himoya va h.k.)
   va bilvosita reytingga (g'alaba ehtimoliga) ta'sir qiladi.

2) 💎 SEHIRLI TOSH — har kuni bepul (/daily) beriladi. Bularning do'koni
   ALOHIDA (/gemshop) va faqat KOSMETIK/qulaylik narsalarni sotadi —
   bu valyuta va uning do'koni reytingga HECH QANDAY ta'sir qilmaydi.
"""
import aiosqlite
import time

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import DB_PATH, CURRENCY_NAME, CURRENCY_SYMBOL, GEM_NAME, GEM_SYMBOL, DAILY_GEM_REWARD
from database import get_or_create_user, adjust_balance, adjust_gems, claim_daily_gems, record_purchase

router = Router(name="economy")

# --- 🔗 Kizuna do'koni: o'yin ichidagi effektli narsalar ---
KIZUNA_SHOP = {
    "tirilish_tumori": {"name": "🔮 Tirilish Tumori", "desc": "Tunda o'ldirilsangiz, bir marta tirilib qolasiz.", "price": 200},
    "soya_pardasi": {"name": "🌫 Soya Pardasi", "desc": "Bir kechaga Meitantei tekshiruvidan yashirinasiz.", "price": 150},
    "qosh_ovoz": {"name": "⚡ Qo'sh Ovoz", "desc": "Kunduzgi ovoz berishda ovozingiz 2 marta hisoblanadi.", "price": 120},
    "vaqtinchalik_alibi": {"name": "🕵️ Vaqtinchalik Alibi", "desc": "Ovoz natijasida chiqarilishdan bir marta qutulasiz.", "price": 180},
    "ittifoq_qasamyodi": {"name": "🤝 Ittifoq Qasamyodi", "desc": "(Faqat Mafia) — sherigingiz kimligini darhol bilib olasiz.", "price": 100},
    "chaqmoq_zarbasi": {"name": "⚔️ Chaqmoq Zarbasi", "desc": "O'zingizni bir tunga himoya qilasiz (shifokorsiz ham).", "price": 160},
    "sodiqlik_nishoni": {"name": "🎖 Sodiqlik Nishoni", "desc": "Profilingizga maxsus unvon qo'yish huquqi.", "price": 100},
}

# --- 💎 Sehirli Tosh do'koni: faqat kosmetik/qulaylik, reytingga ta'sir qilmaydi ---
GEM_SHOP = {
    "ism_ozgartirish": {"name": "✍️ Ism O'zgartirish Kartasi", "desc": "O'yin ichidagi anime-ismingizni o'zingiz tanlaysiz.", "price": 5},
    "nodir_ramka": {"name": "🖼 Nodir Avatar Ramka", "desc": "Profilingizga bezakli ramka.", "price": 8},
    "vip_unvon": {"name": "👑 VIP Unvon: Afsonaviy Otaku", "desc": "Profilda ko'rinadigan dekorativ unvon.", "price": 10},
    "signature_emoji": {"name": "✨ Signature Emoji To'plami", "desc": "O'yin xabarlaringizga maxsus emoji qo'shiladi.", "price": 6},
    "baxt_tumori": {"name": "🍀 Baxt Tumori", "desc": "Profilda ko'rinadigan kosmetik tumor (kuchga ta'siri yo'q).", "price": 6},
    "fon_rasmi": {"name": "🌆 Statistika Fon Rasmi", "desc": "/profile kartochkangiz uchun fon.", "price": 7},
    "duo_kartasi": {"name": "🎴 Duo Kartasi", "desc": "Do'stingizni taklif qilib, ikkalangizga ham +5 💎 bonus.", "price": 4},
}


@router.message(Command("daily"))
async def cmd_daily(message: Message):
    ok, remaining_h = await claim_daily_gems(message.from_user.id)
    if ok:
        await message.answer(
            f"{GEM_SYMBOL} Kunlik bonusingiz: <b>+{DAILY_GEM_REWARD} {GEM_NAME}</b>!\n"
            f"Ertaga yana qaytib keling 🙌"
        )
    else:
        await message.answer(f"⏳ Kunlik bonusni allaqachon oldingiz. Yana {remaining_h} soatdan so'ng qayting.")


@router.message(Command("shop"))
async def cmd_shop(message: Message):
    lines = [f"🛍 <b>Kizuna Do'koni</b> ({CURRENCY_SYMBOL} {CURRENCY_NAME} — o'yin natijasidan)\n"]
    for key, item in KIZUNA_SHOP.items():
        lines.append(f"• {item['name']} — {item['price']} {CURRENCY_SYMBOL}\n   <i>{item['desc']}</i>")
    lines.append(f"\nSotib olish: <code>/buy {list(KIZUNA_SHOP.keys())[0]}</code>")
    await message.answer("\n".join(lines))


@router.message(Command("gemshop"))
async def cmd_gemshop(message: Message):
    lines = [f"💎 <b>Sehirli Tosh Bozori</b> ({GEM_SYMBOL} {GEM_NAME} — kunlik bonusdan, reytingga ta'sir qilmaydi)\n"]
    for key, item in GEM_SHOP.items():
        lines.append(f"• {item['name']} — {item['price']} {GEM_SYMBOL}\n   <i>{item['desc']}</i>")
    lines.append(f"\nSotib olish: <code>/gembuy {list(GEM_SHOP.keys())[0]}</code>")
    lines.append("\n<code>/daily</code> orqali har kuni bepul Sehirli Tosh oling!")
    await message.answer("\n".join(lines))


@router.message(Command("balance"))
async def cmd_balance(message: Message):
    u = await get_or_create_user(
        message.from_user.id, message.from_user.username or "", message.from_user.full_name
    )
    await message.answer(
        f"{CURRENCY_SYMBOL} {CURRENCY_NAME}: <b>{u['balance']}</b>\n"
        f"{GEM_SYMBOL} {GEM_NAME}: <b>{u['gems']}</b>"
    )


@router.message(Command("buy"))
async def cmd_buy(message: Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2 or parts[1].strip() not in KIZUNA_SHOP:
        keys = ", ".join(KIZUNA_SHOP.keys())
        await message.answer(f"Foydalanish: /buy <item>\nMavjud: {keys}")
        return

    item_key = parts[1].strip()
    item = KIZUNA_SHOP[item_key]
    u = await get_or_create_user(
        message.from_user.id, message.from_user.username or "", message.from_user.full_name
    )
    if u["balance"] < item["price"]:
        await message.answer(f"Yetarli {CURRENCY_NAME} yo'q! Kerak: {item['price']}, sizda: {u['balance']}")
        return

    await adjust_balance(message.from_user.id, -item["price"])
    await record_purchase(message.from_user.id, item_key, "kizuna")
    await message.answer(f"✅ Xarid muvaffaqiyatli: {item['name']}!")


@router.message(Command("gembuy"))
async def cmd_gembuy(message: Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2 or parts[1].strip() not in GEM_SHOP:
        keys = ", ".join(GEM_SHOP.keys())
        await message.answer(f"Foydalanish: /gembuy <item>\nMavjud: {keys}")
        return

    item_key = parts[1].strip()
    item = GEM_SHOP[item_key]
    u = await get_or_create_user(
        message.from_user.id, message.from_user.username or "", message.from_user.full_name
    )
    if u["gems"] < item["price"]:
        await message.answer(f"Yetarli {GEM_NAME} yo'q! Kerak: {item['price']}, sizda: {u['gems']}")
        return

    await adjust_gems(message.from_user.id, -item["price"])
    await record_purchase(message.from_user.id, item_key, "gem")
    await message.answer(f"✅ Xarid muvaffaqiyatli: {item['name']}!")
