from aiogram import Router, types
from services.products import get_products_by_category
from keyboards.products import products_kb
from keyboards.main_menu import main_menu_kb
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

# Главное меню игр
@router.callback_query(lambda c: c.data == "games")
async def open_games(callback: types.CallbackQuery):
    kb = InlineKeyboardBuilder()
    kb.button(text="RPG", callback_data="games_rpg")
    kb.button(text="Shooter", callback_data="games_shooter")
    kb.button(text="Strategy", callback_data="games_strategy")
    kb.button(text="⬅ Назад", callback_data="back_main")  # ← назад в главное меню
    kb.adjust(1)

    await callback.message.edit_text(
        "🎮 Игры — выберите жанр:",
        reply_markup=kb.as_markup()
    )
    await callback.answer()


# RPG
@router.callback_query(lambda c: c.data == "games_rpg")
async def open_rpg(callback: types.CallbackQuery):
    products = get_products_by_category("rpg")
    if not products:
        await callback.message.edit_text("❌ Товары не найдены")
        return

    await callback.message.edit_text(
        "🎮 RPG — выберите игру:",
        reply_markup=products_kb(products, back_callback="games")
    )
    await callback.answer()


# Shooter
@router.callback_query(lambda c: c.data == "games_shooter")
async def open_shooter(callback: types.CallbackQuery):
    products = get_products_by_category("shooter")
    if not products:
        await callback.message.edit_text("❌ Товары не найдены")
        return

    await callback.message.edit_text(
        "🔫 Shooter — выберите игру:",
        reply_markup=products_kb(products, back_callback="games")
    )
    await callback.answer()


# Strategy
@router.callback_query(lambda c: c.data == "games_strategy")
async def open_strategy(callback: types.CallbackQuery):
    products = get_products_by_category("strategy")
    if not products:
        await callback.message.edit_text("❌ Товары не найдены")
        return

    await callback.message.edit_text(
        "🗺 Strategy — выберите игру:",
        reply_markup=products_kb(products, back_callback="games")
    )
    await callback.answer()


# Назад в главное меню
@router.callback_query(lambda c: c.data == "back_main")
async def back_to_main(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Добро пожаловать! Выберите раздел 👇",
        reply_markup=main_menu_kb()
    )
    await callback.answer()