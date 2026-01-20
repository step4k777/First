from aiogram import Router
from aiogram.types import CallbackQuery
from keyboards.schedule import create_date_keyboards

router = Router()

@router.callback_query(lambda c: c.data and c.data.startswith("service_"))
async def service_choser(callback: CallbackQuery):
    service_name = callback.data[len("service_"):]

    kb = create_date_keyboards()

    await callback.message.edit_text(
        f"Вы выбрали услугу: {service_name}\nТеперь выберите дату:",
        reply_markup=kb
    )

    await callback.answer()