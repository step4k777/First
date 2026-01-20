from aiogram import Router
from aiogram.types import CallbackQuery, Message
from sheets import add_record
from aiogram.fsm.context import FSMContext

router = Router()

@router.callback_query(lambda c: c.data.startswith("time_"))
async def time_chosen(callback: CallbackQuery, state: FSMContext):
    time = callback.data.replace("time_", "")
    await state.update_data(time=time)
    await callback.message.answer("Введите ваше имя:")
    await callback.answer()

@router.message()
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите телефон:")

@router.message()
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = await state.get_data()

    add_record(data)

    await message.answer("✅ Запись создана!")
    await state.clear()