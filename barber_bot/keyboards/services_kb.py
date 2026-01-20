from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def create_services_keyboard(services:list) -> InlineKeyboardMarkup:
    """
    services: список словарей вида {"Услуга": "Стрижка", "Длительность": 2}
    """
    keyboard = [
        [InlineKeyboardButton(text=service["Услуга"], callback_data=f"service_{service['Услуга']}")]
        for service in services
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)