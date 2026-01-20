from aiogram import Router
from aiogram.types import CallbackQuery
from datetime import datetime, timedelta
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.callback_query(lambda c: c.data.startswith("service_"))
async def service_chosen(callback: CallbackQuery, state):
    service = callback.data.replace("service_", "")
    await state.update_data(service=service)

    kb = InlineKeyboardBuilder()

    today = datetime.today()
    for i in range(7):
        day = today + timedelta(days=i)
        date_str = day.strftime("%d.%m.%Y")
        kb.button(text=date_str, callback_data=f"date_{date_str}")

    kb.adjust(2)

    await callback.message.edit_text("Выберите дату:", reply_markup=kb.as_markup())
    await callback.answer()