"""
Bot valyutasi: "Sehirli tosh" (絆 — yapon tilida "bog'liqlik/ahdlashuv" degani,
anime olamida qahramonlar orasidagi do'stlik-ittifoq g'oyasiga ishora,
shu sabab istalgan anime janriga mos keladi).

Ishlab topish yo'llari:
  - G'alaba: +50 Kizuna
  - Mag'lubiyat: +15 Kizuna (ishtirok uchun tasalli mukofoti)
  - MVP (eng faol/foydali o'yinchi): +30 Kizuna qo'shimcha

Do'kon narsalari — barchasi anime-uslubidagi nom bilan, lekin funksional:
"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import aiosqlite
import time

from config import DB_PATH, CURRENCY_NAME, CURRENCY_SYMBOL
from database import get_or_create_user, adjust_balance

router = Router(name="economy")

SHOP_ITEMS = {
    "tirilish_tumori": {
        "name": "🔮 Tirilish Tumori",
        "desc": "Tunda o'ldirilsangiz, bir marta tirilib qolasiz.",
        "price": 200,
    },
    "soya_pardasi": {
        "name": "🌫 Soya Pardasi",
        "desc": "Bir kechaga Meitantei tekshiruvidan yashirinasiz.",
        "price": 150,
    },
    "sodiqlik_nishoni": {
        "name": "🎖 Sodiqlik Nishoni",
        "desc": "Profilingizga maxsus unvon qo'yish huquqi.",
        "price": 100,
    },
    "ikki_baravar_ovoz": {
        "name": "⚡ Qo'sh Ovoz",
        "desc": "Kunduzgi ovoz berishda ovozingiz 2 marta hisoblanadi.",
        "price": 120,
    },
}


@router.message(Command("shop"))
async def cmd_shop(message: Message):
    lines = [f"🛍 <b>Kizuna Do'koni</b> ({CURRENCY_SYMBOL} {CURRENCY_NAME})\n"]
    for key, item in SHOP_ITEMS.items():
        lines.append(f"• {item['name']} — {item['price']} {CURRENCY_SYMBOL}\n   <i>{item['desc']}</i>")
    lines.append(f"\nSotib olish uchun: <code>/buy {list(SHOP_ITEMS.keys())[0]}</code> kabi yozing.")
    await message.answer("\n".join(lines))


@router.message(Command("balance"))
async def cmd_balance(message: Message):
    u = await get_or_create_user(
        message.from_user.id, message.from_user.username or "", message.from_user.full_name
    )
    await message.answer(f"{CURRENCY_SYMBOL} Balansingiz: <b>{u['balance']} {CURRENCY_NAME}</b>")


@router.message(Command("buy"))
async def cmd_buy(message: Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2 or parts[1].strip() not in SHOP_ITEMS:
        keys = ", ".join(SHOP_ITEMS.keys())
        await message.answer(f"Foydalanish: /buy <item>\nMavjud: {keys}")
        return

    item_key = parts[1].strip()
    item = SHOP_ITEMS[item_key]
    u = await get_or_create_user(
        message.from_user.id, message.from_user.username or "", message.from_user.full_name
    )
    if u["balance"] < item["price"]:
        await message.answer(
            f"Yetarli {CURRENCY_NAME} yo'q! Kerak: {item['price']}, sizda: {u['balance']}"
        )
        return

    await adjust_balance(message.from_user.id, -item["price"])
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO shop_purchases (user_id, item_key, purchased_at) VALUES (?, ?, ?)",
            (message.from_user.id, item_key, int(time.time())),
        )
        await db.commit()

    await message.answer(f"✅ Xarid muvaffaqiyatli: {item['name']}!")
