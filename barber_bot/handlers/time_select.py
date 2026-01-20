from aiogram import Router
from aiogram.types import CallbackQuery
from keyboards.time_kb import create_time_keyboard
from sheets import get_busy_times

router = Router()

@router.callback_query(lambda c: c.data and c.data.startswith("date_"))
async def date_chosen(callback: CallbackQuery):
    date = callback.data[len("date_"):]

    barber = "Иван"

    busy = get_busy_times(date, barber)
    kb = create_time_keyboard(busy)

    await callback.message.edit_text(
        f"Дата {date} выбрана.\nТеперь выберите время:",
        reply_markup=kb
    )
    await callback.answer()