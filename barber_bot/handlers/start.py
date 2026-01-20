from aiogram import Router, types
from aiogram.filters import Command
from sheets import get_barbers
from keyboards.barbers_kb import create_barbers_keyboard

router = Router()

@router.message(Command(commands=["start"]))
async def start_command(message: types.Message):
    barbers = get_barbers()
    kb = create_barbers_keyboard(barbers)
    await message.answer("Выберите барбера:", reply_markup=kb)