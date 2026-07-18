import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats

from config import BOT_TOKEN
from database import init_db

import start_handler
import lobby_handler
import game_handler
import rating_handler
import economy_handler
import feedback_handler
import admin_handler


PRIVATE_COMMANDS = [
    BotCommand(command="start", description="🏠 Bosh menyu"),
    BotCommand(command="lobby", description="🏮 Yangi lobby ochish"),
    BotCommand(command="profile", description="👤 Profilim"),
    BotCommand(command="rating", description="🏆 Global reyting"),
    BotCommand(command="shop", description="🛍 Kizuna do'koni"),
    BotCommand(command="gemshop", description="💎 Sehirli Tosh bozori"),
    BotCommand(command="daily", description="🎁 Kunlik bonus"),
    BotCommand(command="balance", description="💰 Balansim"),
    BotCommand(command="myid", description="🆔 Telegram ID raqamim"),
]

GROUP_COMMANDS = [
    BotCommand(command="lobby", description="🏮 Yangi o'yin lobbysini ochish"),
    BotCommand(command="grouprating", description="🏅 Shu guruh reytingi"),
    BotCommand(command="rating", description="🏆 Global reyting"),
    BotCommand(command="shop", description="🛍 Kizuna do'koni"),
    BotCommand(command="gemshop", description="💎 Sehirli Tosh bozori"),
    BotCommand(command="balance", description="💰 Balansim"),
]


async def setup_commands(bot: Bot):
    await bot.set_my_commands(PRIVATE_COMMANDS, scope=BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(GROUP_COMMANDS, scope=BotCommandScopeAllGroupChats())


async def main():
    logging.basicConfig(level=logging.INFO)
    await init_db()

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    # Tartib muhim emas, lekin admin/feedback avval bo'lsa xatolik kamroq bo'ladi
    dp.include_router(admin_handler.router)
    dp.include_router(feedback_handler.router)
    dp.include_router(start_handler.router)
    dp.include_router(lobby_handler.router)
    dp.include_router(game_handler.router)
    dp.include_router(rating_handler.router)
    dp.include_router(economy_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await setup_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
