import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from database import init_db

import start_handler
import lobby_handler
import game_handler
import rating_handler
import economy_handler
import feedback_handler
import admin_handler


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
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
