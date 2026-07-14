from aiogram.fsm.state import State, StatesGroup


class GenreSelect(StatesGroup):
    waiting_query = State()
