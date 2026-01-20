from aiogram import Router
from aiogram.types import CallbackQuery
from booking import get_free_slots
from sheets import get_services
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.callback_query(lambda c: c.data.startswith("date_"))
async def date_chosen(callback: CallbackQuery, state):
    date = callback.data.replace("date_", "")
    data = await state.get_data()
    barber = data["barber"]
    service = data["service"]

    services = get_services()
    duration = next(s["Длительность_мин"] for s in services if s["Услуга"] == service)

    free_times = get_free_slots(barber, date, int(duration))

    kb = InlineKeyboardBuilder()
    for t in free_times:
        kb.button(text=t, callback_data=f"time_{t}")
    kb.adjust(3)

    await callback.message.edit_text("Выберите время:", reply_markup=kb.as_markup())
    await callback.answer()