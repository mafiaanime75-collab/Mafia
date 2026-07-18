import uuid

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from keyboards import lobby_share_kb
from database import create_session
from config import MAX_PLAYERS

router = Router(name="lobby_handler")

# session_id -> {"world": None yoki tanlangan nom, "host_id":..., "players": {uid: name}}
ACTIVE_LOBBIES: dict[str, dict] = {}


def _new_lobby_text(host_name: str, players: dict) -> str:
    names = "\n".join(f"• {n}" for n in players.values())
    return (
        f"🏮 <b>Lobby ochildi!</b>\n\n"
        f"👥 O'yinchilar ({len(players)}/{MAX_PLAYERS}):\n{names}\n\n"
        f"Do'stlaringizni chaqiring yoki asosiy guruhga o'ting!\n"
        f"Host tayyor bo'lgach «▶️ Boshlash»ni bossin — o'shanda ANIME DUNYOSI so'raladi."
    )


@router.message(Command("lobby"))
async def cmd_lobby(message: Message):
    """
    Guruhda TO'G'RIDAN-TO'G'RI ishlaydi — Telegram buyruqlari (/lobby)
    bot Privacy Mode yoqilgan bo'lsa ham har doim botga yetib boradi,
    shuning uchun bu eng ishonchli usul.
    """
    session_id = uuid.uuid4().hex[:10]
    host = message.from_user
    ACTIVE_LOBBIES[session_id] = {"world": None, "host_id": host.id, "players": {host.id: host.full_name}}
    await create_session(session_id, group_id=message.chat.id, host_id=host.id)
    await message.answer(
        _new_lobby_text(host.full_name, ACTIVE_LOBBIES[session_id]["players"]),
        reply_markup=lobby_share_kb(session_id),
    )


@router.callback_query(F.data == "menu_open_lobby")
async def on_menu_open_lobby(callback: CallbackQuery):
    session_id = uuid.uuid4().hex[:10]
    host = callback.from_user
    ACTIVE_LOBBIES[session_id] = {"world": None, "host_id": host.id, "players": {host.id: host.full_name}}
    await create_session(session_id, group_id=callback.message.chat.id, host_id=host.id)
    await callback.message.edit_text(
        _new_lobby_text(host.full_name, ACTIVE_LOBBIES[session_id]["players"]),
        reply_markup=lobby_share_kb(session_id),
    )
    await callback.answer("Lobby ochildi ✅")


@router.callback_query(F.data.startswith("lobby_join:"))
async def on_lobby_join(callback: CallbackQuery):
    session_id = callback.data.split("lobby_join:", 1)[1]
    lobby = ACTIVE_LOBBIES.get(session_id)
    if not lobby:
        await callback.answer("Bu lobby endi faol emas.", show_alert=True)
        return
    if len(lobby["players"]) >= MAX_PLAYERS:
        await callback.answer(f"Lobby to'lgan (max {MAX_PLAYERS})!", show_alert=True)
        return
    lobby["players"][callback.from_user.id] = callback.from_user.full_name
    names = "\n".join(f"• {n}" for n in lobby["players"].values())
    text = (
        f"🏮 <b>Lobby</b>\n\n"
        f"👥 O'yinchilar ({len(lobby['players'])}/{MAX_PLAYERS}):\n{names}\n\n"
        f"Do'stlaringizni chaqiring yoki asosiy guruhga o'ting!\n"
        f"Host tayyor bo'lgach «▶️ Boshlash»ni bossin."
    )
    await callback.message.edit_text(text, reply_markup=lobby_share_kb(session_id))
    await callback.answer("Lobbyga qo'shildingiz ✅")


@router.inline_query(F.query.startswith("join:"))
async def inline_share_lobby(inline_query: InlineQuery):
    session_id = inline_query.query.split("join:", 1)[1]
    result = InlineQueryResultArticle(
        id=session_id,
        title="🎴 Anime Mafia — lobby'ga taklif",
        description="Ushbu guruhga lobby taklifnomasini yuborish",
        input_message_content=InputTextMessageContent(
            message_text=(
                "🌙 <b>Anime Mafia</b> o'yiniga taklif qilinasiz!\n\n"
                "Qo'shilish uchun pastdagi tugmani bosing 👇"
            ),
            parse_mode="HTML",
        ),
    )
    await inline_query.answer([result], cache_time=1, is_personal=True)
