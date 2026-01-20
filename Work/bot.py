import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers import start, games, order



async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(games.router)
    dp.include_router(order.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    print("ЗАПУСК ФАЙЛА")
    asyncio.run(main())