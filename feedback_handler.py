from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from keyboards import feedback_kind_kb
from states import FeedbackFlow
from database import add_feedback

router = Router(name="feedback_handler")


@router.callback_query(F.data == "menu_feedback")
async def on_menu_feedback(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FeedbackFlow.waiting_kind)
    await callback.message.answer(
        "📝 Taklif yoki shikoyatingizni yubormoqchimisiz?", reply_markup=feedback_kind_kb()
    )
    await callback.answer()


@router.callback_query(F.data.startswith("fb_kind:"))
async def on_feedback_kind(callback: CallbackQuery, state: FSMContext):
    kind = callback.data.split("fb_kind:", 1)[1]
    await state.update_data(kind=kind)
    await state.set_state(FeedbackFlow.waiting_text)
    label = "Taklifingizni" if kind == "taklif" else "Shikoyatingizni"
    await callback.message.edit_text(f"✍️ {label} yozib yuboring:")
    await callback.answer()


@router.message(FeedbackFlow.waiting_text, F.text)
async def on_feedback_text(message: Message, state: FSMContext):
    data = await state.get_data()
    kind = data.get("kind", "taklif")
    await add_feedback(
        user_id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username or "",
        kind=kind,
        text=message.text,
    )
    await state.clear()
    label = "Taklifingiz" if kind == "taklif" else "Shikoyatingiz"
    await message.answer(f"✅ {label} qabul qilindi, rahmat! Tez orada ko'rib chiqiladi.")
