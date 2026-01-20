from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config import TOKEN
from handlers import start, services, schedule, time_select
import asyncio

bot = Bot(token=TOKEN)
dp = Dispatcher()

# регистрируем router
dp.include_router(start.router)
dp.include_router(schedule.router)
dp.include_router(services.router)
dp.include_router(time_select.router)

async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())