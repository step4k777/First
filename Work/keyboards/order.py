from aiogram.utils.keyboard import InlineKeyboardBuilder

def order_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="🛒 Оформить заказ", callback_data="order_start")
    kb.adjust(1)
    return kb.as_markup()