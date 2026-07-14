from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from data.genres import search_genres
from keyboards import genre_results_kb
from states import GenreSelect
from database import get_or_create_user

router = Router(name="start")

WELCOME = (
    "🌙 <b>Anime Mafia: Kizuna no Yoru</b> 🌙\n\n"
    "Xush kelibsiz! Bu — sevimli anime olamlaringiz fonida o'ynaladigan Mafia o'yini.\n"
    "Avval o'yin o'tadigan <b>anime janrini</b> tanlang — nom yozib qidiring "
    "(masalan: <i>na</i> deb yozsangiz <b>Naruto</b> chiqadi).\n\n"
    "✍️ Janr nomini yozing:"
)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await get_or_create_user(
        message.from_user.id, message.from_user.username or "", message.from_user.full_name
    )
    await state.set_state(GenreSelect.waiting_query)
    await message.answer(WELCOME)


@router.message(GenreSelect.waiting_query, F.text)
async def on_genre_query(message: Message, state: FSMContext):
    query = message.text.strip()
    results = search_genres(query, limit=8)
    if not results:
        await message.answer("Hech narsa topilmadi 😔 Boshqa nom bilan urinib ko'ring.")
        return
    await message.answer(
        f"🔎 <b>{query}</b> uchun natijalar:",
        reply_markup=genre_results_kb(results),
    )
