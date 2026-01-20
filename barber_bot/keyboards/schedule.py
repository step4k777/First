from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime, timedelta

def create_date_keyboards(days_ahead=7):
    keyboard = []
    today = datetime.today()

    for i in range(days_ahead):
        day = today + timedelta(days=1)
        text = day.strftime("%d.%m")
        value = day.strftime("%y-%m-%d")
        keyboard.append([InlineKeyboardButton(text=text, callback_data=f"date_{value}")])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)