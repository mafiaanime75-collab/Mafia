from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import MAIN_GROUP_INVITE_LINK


def world_results_kb(worlds: list[str]) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    for w in worlds:
        b.button(text=w, callback_data=f"world:{w}")
    b.adjust(2)
    return b.as_markup()


def world_confirm_kb(world: str) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text=f"✅ {world} tanlandi — Lobby ochish", callback_data=f"lobby_open:{world}")
    b.button(text="🔎 Boshqa dunyo qidirish", callback_data="world_search_again")
    b.adjust(1)
    return b.as_markup()


def lobby_share_kb(session_id: str) -> InlineKeyboardMarkup:
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
