import uuid

from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from aiogram.fsm.context import FSMContext

from data.genres import get_lore, search_genres
from keyboards import genre_confirm_kb, genre_results_kb, lobby_share_kb
from states import GenreSelect
from database import create_session, load_session, save_session_state
from config import MAX_PLAYERS

router = Router(name="lobby")

# session_id -> {"genre":..., "group_id":..., "host_id":..., "players": {uid: name}}
ACTIVE_LOBBIES: dict[str, dict] = {}


@router.callback_query(F.data.startswith("genre:"))
async def on_genre_chosen(callback: CallbackQuery, state: FSMContext):
    genre = callback.data.split("genre:", 1)[1]
    lore = get_lore(genre)
    text = (
        f"🎴 Siz tanladingiz: <b>{genre}</b>\n\n"
        f"🌍 Dunyo: <i>{lore['world']}</i>\n"
        f"🩸 Yovuz jamoa: <i>{lore['villain_team']}</i>\n\n"
        f"{lore['intro']}\n\n"
        f"Endi lobby oching va o'yinchilarni yig'ing!"
    )
    await callback.message.edit_text(text, reply_markup=genre_confirm_kb(genre))
    await callback.answer()


@router.callback_query(F.data == "genre_search_again")
async def on_search_again(callback: CallbackQuery, state: FSMContext):
    await state.set_state(GenreSelect.waiting_query)
    await callback.message.edit_text("✍️ Yangi janr nomini yozing:")
    await callback.answer()


@router.callback_query(F.data.startswith("lobby_open:"))
async def on_lobby_open(callback: CallbackQuery, state: FSMContext):
    genre = callback.data.split("lobby_open:", 1)[1]
    session_id = uuid.uuid4().hex[:10]
    host = callback.from_user

    ACTIVE_LOBBIES[session_id] = {
        "genre": genre,
        "host_id": host.id,
        "players": {host.id: host.full_name},
    }
    await create_session(session_id, group_id=callback.message.chat.id, host_id=host.id)

    lore = get_lore(genre)
    text = (
        f"🏮 <b>Lobby ochildi!</b> Janr: <b>{genre}</b>\n"
        f"🌍 {lore['world']}\n\n"
        f"👥 O'yinchilar (1): {host.full_name}\n\n"
        f"Do'stlaringizni chaqiring yoki asosiy guruhga o'ting!"
    )
    await callback.message.edit_text(text, reply_markup=lobby_share_kb(session_id))
    await callback.answer("Lobby ochildi ✅")


@router.callback_query(F.data.startswith("lobby_join:"))
async def on_lobby_join(callback: CallbackQuery):
    session_id = callback.data.split("lobby_join:", 1)[1]
    lobby = ACTIVE_LOBBIES.get(session_id)
    if not lobby:
        await callback.answer("Bu lobby endi faol emas.", show_alert=True)
        return
    if len(lobby["players"]) >= MAX_PLAYERS:
        await callback.answer("Lobby to'lgan!", show_alert=True)
        return
    lobby["players"][callback.from_user.id] = callback.from_user.full_name
    names = "\n".join(f"• {n}" for n in lobby["players"].values())
    text = (
        f"🏮 <b>Lobby</b> — Janr: <b>{lobby['genre']}</b>\n\n"
        f"👥 O'yinchilar ({len(lobby['players'])}):\n{names}\n\n"
        f"Do'stlaringizni chaqiring yoki asosiy guruhga o'ting!"
    )
    await callback.message.edit_text(text, reply_markup=lobby_share_kb(session_id))
    await callback.answer("Lobbyga qo'shildingiz ✅")


@router.inline_query(F.query.startswith("join:"))
async def inline_share_lobby(inline_query: InlineQuery):
    """
    Rasmdagi "Chatni tanlang" ekrani aynan shu switch_inline_query orqali chiqadi —
    foydalanuvchi tugmani bosganda Telegram o'zi chat tanlash ro'yxatini ko'rsatadi,
    keyin shu inline natija o'sha chatga yuboriladi.
    """
    session_id = inline_query.query.split("join:", 1)[1]
    lobby = ACTIVE_LOBBIES.get(session_id)
    genre = lobby["genre"] if lobby else "Anime Mafia"
    result = InlineQueryResultArticle(
        id=session_id,
        title=f"🎴 {genre} — Mafia lobby'siga taklif",
        description="Ushbu guruhga lobby taklifnomasini yuborish",
        input_message_content=InputTextMessageContent(
            message_text=(
                f"🌙 <b>Anime Mafia</b> o'yiniga taklif qilinasiz!\n"
                f"Janr: <b>{genre}</b>\n\n"
                f"Qo'shilish uchun pastdagi tugmani bosing 👇"
            ),
            parse_mode="HTML",
        ),
    )
    await inline_query.answer([result], cache_time=1, is_personal=True)
