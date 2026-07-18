from aiogram.fsm.state import State, StatesGroup


class FeedbackFlow(StatesGroup):
    waiting_kind = State()
    waiting_text = State()
