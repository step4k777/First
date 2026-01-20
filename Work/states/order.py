from aiogram.fsm.state import State, StatesGroup

class OrderForm(StatesGroup):
    waiting_for_email = State()
    waiting_for_phone = State()