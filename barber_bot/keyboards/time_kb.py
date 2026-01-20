from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime, time, timedelta

def create_time_keyboard(busy_times: list):
    keyboard = []

    start = time(10,0)
    end = time(22, 0)

    current = datetime.combine(datetime.today(), start)
    end_dt = datetime.combine(datetime.today(), end)

    while current < end_dt:
        t = current.strftime("%H:%M")

        if t not in busy_times:
            keyboard.append([InlineKeyboardButton(text=t, callback_data=f"time_{t}")])

        current += timedelta(minutes=30)

    return InlineKeyboardMarkup(inline_keyboard=keyboard)