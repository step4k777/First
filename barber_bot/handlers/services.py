from aiogram import Router
from aiogram.types import CallbackQuery
from keyboards.services_kb import create_services_keyboard
from sheets import get_services

router = Router()

@router.callback_query(lambda c: c.data and c.data.startswith("barber_"))
async def barber_chosen(callback: CallbackQuery):
    barber_name = callback.data.replace("barber_", "")

    services = get_services()
    kb = create_services_keyboard(services)

    await callback.message.edit_text(
        f"Вы выбрали барбера {barber_name}. Теперь выберите услугу:",
        reply_markup=kb
    )
    await callback.answer()