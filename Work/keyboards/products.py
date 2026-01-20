from aiogram.utils.keyboard import InlineKeyboardBuilder

def products_kb(products, back_callback="back_games"):
    kb = InlineKeyboardBuilder()

    for product in products:
        kb.button(
            text=f"{product['name']} - {product['price']} ₽",
            callback_data=f"product_{product['id']}"
        )

    kb.button(text="⬅ Назад", callback_data=back_callback)
    kb.adjust(1)
    return kb.as_markup()