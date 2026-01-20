from aiogram import Router, types
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.order import OrderForm

router = Router()

@router.message(OrderForm.waiting_for_email)
async def get_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Введите номер телефона:")
    await state.set_state(OrderForm.waiting_for_phone)

@router.message(OrderForm.waiting_for_phone)
async def get_phone(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(
        f"✅ Заказ оформлен!\n\n"
        f"📧 Email: {data['email']}\n"
        f"📞 Телефон: {message.text}\n\n"
        f"Мы скоро с вами свяжемся."
    )
    await state.clear()