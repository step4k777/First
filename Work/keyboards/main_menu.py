from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="🎮 Игры", callback_data="games")
    kb.button(text="ℹ️ Поддержка", callback_data="support")
    kb.adjust(1)
    return kb.as_markup()