from aiogram.fsm.state import State, StatesGroup


class WorldSelect(StatesGroup):
    waiting_query = State()
