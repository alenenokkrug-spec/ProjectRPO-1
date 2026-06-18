import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import main_router
from info import info_router
from exercises import exercise_router


async def main():
    if not BOT_TOKEN:
        raise RuntimeError

    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(info_router)
    dp.include_router(exercise_router)
    dp.include_router(main_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
