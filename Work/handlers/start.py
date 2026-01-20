from aiogram import Router, types
from aiogram.filters import CommandStart
from keyboards.main_menu import main_menu_kb

router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Добро пожаловать! Выберите раздел 👇",
        reply_markup=main_menu_kb()
    )