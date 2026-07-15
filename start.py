from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards import main_menu_kb
from database import get_or_create_user

router = Router(name="start_handler")

WELCOME = (
    "🌙 <b>Anime Mafia: Kizuna no Yoru</b> 🌙\n\n"
    "Xush kelibsiz! Quyidagi paneldan kerakli bo'limni tanlang.\n"
    "Anime dunyosi esa o'yin <b>boshlanayotganda</b>, lobbyni boshlagan odamdan so'raladi."
)


@router.message(CommandStart())
async def cmd_start(message: Message):
    await get_or_create_user(
        message.from_user.id, message.from_user.username or "", message.from_user.full_name
    )
    await message.answer(WELCOME, reply_markup=main_menu_kb())
