from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import MAIN_GROUP_INVITE_LINK


def main_menu_kb() -> InlineKeyboardMarkup:
    """Bot ishga tushganda (/start) chiqadigan asosiy panel."""
    b = InlineKeyboardBuilder()
    b.button(text="🏮 Lobby ochish", callback_data="menu_open_lobby")
    b.button(text="👤 Profilim", callback_data="menu_profile")
    b.button(text="🏆 Reyting", callback_data="menu_rating")
    b.button(text="🛍 Kizuna Do'koni", callback_data="menu_shop")
    b.button(text="💎 Tosh Bozori", callback_data="menu_gemshop")
    b.button(text="🎁 Kunlik bonus", callback_data="menu_daily")
    b.button(text="📝 Taklif/Shikoyat", callback_data="menu_feedback")
    b.adjust(1, 2, 2, 2)
    return b.as_markup()


def lobby_share_kb(session_id: str) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="📤 Guruhga ulashish", switch_inline_query=f"join:{session_id}")
    b.button(text="👥 Asosiy guruhga qo'shilish", url=MAIN_GROUP_INVITE_LINK)
    b.button(text="🎮 Lobbyga qo'shilish", callback_data=f"lobby_join:{session_id}")
    b.button(text="▶️ O'yinni boshlash (host)", callback_data=f"lobby_start:{session_id}")
    b.adjust(2, 2)
    return b.as_markup()


def world_page_kb(worlds: list[str], page: int, per_page: int = 10) -> InlineKeyboardMarkup:
    """
    100 ta dunyoni SAHIFALAB, faqat tugmalar orqali ko'rsatadi — hech narsa
    yozish shart emas. Bu guruhlarda ham ishonchli ishlaydi (Telegram bot
    Privacy Mode yoqilgan bo'lsa ham, tugma bosish har doim botga yetib boradi,
    lekin oddiy matn yetib bormasligi mumkin).
    """
    start = page * per_page
    chunk = worlds[start:start + per_page]
    b = InlineKeyboardBuilder()
    for w in chunk:
        b.button(text=w, callback_data=f"world:{w}")
    b.adjust(2)

    total_pages = (len(worlds) + per_page - 1) // per_page
    nav = InlineKeyboardBuilder()
    if page > 0:
        nav.button(text="⬅️ Oldingi", callback_data=f"wpage:{page-1}")
    nav.button(text=f"📄 {page+1}/{total_pages}", callback_data="wpage_noop")
    if page < total_pages - 1:
        nav.button(text="Keyingi ➡️", callback_data=f"wpage:{page+1}")
    nav.adjust(3)

    b.attach(nav)
    return b.as_markup()


def night_action_kb(
        session_id: str, targets: list[tuple[int, str]], action: str) -> InlineKeyboardMarkup:
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


def feedback_kind_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="💡 Taklif", callback_data="fb_kind:taklif")
    b.button(text="⚠️ Shikoyat", callback_data="fb_kind:shikoyat")
    b.adjust(2)
    return b.as_markup()


def shop_list_kb(items: dict, prefix: str, symbol: str) -> InlineKeyboardMarkup:
    """Do'kon ro'yxati — har bir mahsulot alohida tugma (narxi bilan)."""
    b = InlineKeyboardBuilder()
    for key, item in items.items():
        b.button(text=f"{item['name']} — {item['price']}{symbol}", callback_data=f"{prefix}:{key}")
    b.adjust(1)
    return b.as_markup()


def shop_item_kb(item_key: str, prefix: str, back_callback: str) -> InlineKeyboardMarkup:
    """Bitta mahsulot uchun: sotib olish yoki ortga qaytish."""
    b = InlineKeyboardBuilder()
    b.button(text="✅ Sotib olish", callback_data=f"{prefix}_confirm:{item_key}")
    b.button(text="⬅️ Ortga", callback_data=back_callback)
    b.adjust(1)
    return b.as_markup()


def admin_feedback_item_kb(feedback_id: int) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="✅ O'qildi deb belgilash", callback_data=f"fb_read:{feedback_id}")
    b.button(text="🗑 O'chirish", callback_data=f"fb_del:{feedback_id}")
    b.adjust(1)
    return b.as_markup()
