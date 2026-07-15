from aiogram.fsm.state import State, StatesGroup


class WorldSelect(StatesGroup):
    """Lobby ochilib, HOST 'boshlash'ni bosganda ishlaydigan holat."""
    waiting_query = State()


class FeedbackFlow(StatesGroup):
    waiting_kind = State()
    waiting_text = State()
