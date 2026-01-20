from aiogram.utils.keyboard import InlineKeyboardBuilder

def games_menu_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="RPG", callback_data="games_rpg")
    kb.button(text="Shooter", callback_data="games_shooter")
    kb.button(text="Strategy", callback_data="games_strategy")
    kb.button(text="⬅ Назад", callback_data="back_games")
    kb.adjust(1)
    return kb.as_markup()