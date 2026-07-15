from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from genres import search_worlds
from keyboards import world_results_kb
from states import WorldSelect
from database import get_or_create_user

router = Router(name="start")

WELCOME = (
    "🌙 <b>Anime Mafia: Kizuna no Yoru</b> 🌙\n\n"
    "Xush kelibsiz! Avval o'yin o'tadigan <b>dunyoni tanlang</b> — nom yozib qidiring "
    "(masalan: <i>na</i> deb yozsangiz <b>Naruto</b> chiqadi).\n\n"
    "✍️ Dunyo nomini yozing:"
)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await get_or_create_user(
        message.from_user.id, message.from_user.username or "", message.from_user.full_name
    )
    await state.set_state(WorldSelect.waiting_query)
    await message.answer(WELCOME)


@router.message(WorldSelect.waiting_query, F.text)
async def on_world_query(message: Message, state: FSMContext):
    query = message.text.strip()
    results = search_worlds(query, limit=8)
    if not results:
        await message.answer("Hech narsa topilmadi 😔 Boshqa nom bilan urinib ko'ring.")
        return
    await message.answer(
        f"🔎 <b>{query}</b> uchun natijalar:",
        reply_markup=world_results_kb(results),
    )
