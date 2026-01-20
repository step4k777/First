from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_barbers_keyboard(barbers: list) -> InlineKeyboardMarkup:
    # Каждая кнопка в отдельной строке
    keyboard = [
        [InlineKeyboardButton(text=barber, callback_data=f"barber_{barber}")]
        for barber in barbers
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
