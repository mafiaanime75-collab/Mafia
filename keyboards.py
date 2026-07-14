from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import MAIN_GROUP_INVITE_LINK


def genre_results_kb(genres: list[str]) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    for g in genres:
        b.button(text=g, callback_data=f"genre:{g}")
    b.adjust(2)
    return b.as_markup()


def genre_confirm_kb(genre: str) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text=f"✅ {genre} tanlandi — Lobby ochish", callback_data=f"lobby_open:{genre}")
    b.button(text="🔎 Boshqa janr qidirish", callback_data="genre_search_again")
    b.adjust(1)
    return b.as_markup()


def lobby_share_kb(session_id: str) -> InlineKeyboardMarkup:
    """
    Rasmda ko'rsatilgandek: lobby'ni biror chatga ulashish (switch_inline_query orqali
    foydalanuvchi o'zi chat tanlaydi) + asosiy o'yin guruhiga qo'shilish tugmasi.
    """
    b = InlineKeyboardBuilder()
    b.button(text="📤 Guruhga ulashish", switch_inline_query=f"join:{session_id}")
    b.button(text="👥 Asosiy guruhga qo'shilish", url=MAIN_GROUP_INVITE_LINK)
    b.button(text="🎮 Lobbyga qo'shilish", callback_data=f"lobby_join:{session_id}")
    b.button(text="▶️ O'yinni boshlash (host)", callback_data=f"lobby_start:{session_id}")
    b.adjust(2, 2)
    return b.as_markup()


def night_action_kb(session_id: str, targets: list[tuple[int, str]], action: str) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    for uid, name in targets:
        b.button(text=name, callback_data=f"act:{action}:{session_id}:{uid}")
    b.adjust(1)
    return b.as_markup()


def vote_kb(session_id: str, targets: list[tuple[int, str]]) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    for uid, name in targets:
        b.button(text=f"🗳 {name}", callback_data=f"vote:{session_id}:{uid}")
    b.adjust(1)
    return b.as_markup()
