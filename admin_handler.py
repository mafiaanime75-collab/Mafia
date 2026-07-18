from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from config import ADMIN_IDS
from database import list_unread_feedback, count_unread_feedback, mark_feedback_read, delete_feedback
from keyboards import admin_feedback_item_kb

router = Router(name="admin_handler")


def _is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS


@router.message(Command("myid"))
async def cmd_myid(message: Message):
    """Har kim o'z Telegram ID raqamini bilishi uchun — ADMIN_IDS ga shu raqam kerak."""
    await message.answer(
        f"🆔 Sizning Telegram ID raqamingiz: <code>{message.from_user.id}</code>\n\n"
        f"Buni <b>.env</b> faylidagi <code>ADMIN_IDS</code> ga (yoki config.py dagi "
        f"<code>ADMIN_IDS_HARDCODED</code> ro'yxatiga) qo'shing va botni QAYTA ISHGA TUSHIRING "
        f"(.env o'zgarishi faqat restartdan keyin kuchga kiradi)."
    )


@router.message(Command("admin"))
async def cmd_admin(message: Message):
    if not _is_admin(message.from_user.id):
        await message.answer(
            f"⛔ Sizda admin panelga kirish huquqi yo'q.\n\n"
            f"Sizning ID: <code>{message.from_user.id}</code>\n"
            f"Buni ADMIN_IDS ga qo'shib, botni QAYTA ISHGA TUSHIRING."
        )
        return
    unread = await count_unread_feedback()
    await message.answer(
        f"🛠 <b>Admin Panel</b>\n\n📬 O'qilmagan taklif/shikoyatlar: <b>{unread}</b>\n\n"
        f"Ko'rish uchun: /feedbacks"
    )


@router.message(Command("feedbacks"))
async def cmd_feedbacks(message: Message):
    if not _is_admin(message.from_user.id):
        await message.answer("⛔ Sizda admin panelga kirish huquqi yo'q.")
        return
    items = await list_unread_feedback(limit=5)
    if not items:
        await message.answer("📭 O'qilmagan taklif/shikoyat yo'q.")
        return
    for item in items:
        kind_label = "💡 Taklif" if item["kind"] == "taklif" else "⚠️ Shikoyat"
        uname = f"@{item['username']}" if item["username"] else str(item["user_id"])
        text = (
            f"{kind_label} — {item['full_name']} ({uname})\n\n"
            f"{item['text']}"
        )
        await message.answer(text, reply_markup=admin_feedback_item_kb(item["id"]))


@router.callback_query(F.data.startswith("fb_read:"))
async def on_fb_read(callback: CallbackQuery):
    if not _is_admin(callback.from_user.id):
        await callback.answer("⛔ Ruxsat yo'q.", show_alert=True)
        return
    feedback_id = int(callback.data.split("fb_read:", 1)[1])
    await mark_feedback_read(feedback_id)
    await callback.message.edit_text(callback.message.text + "\n\n✅ O'qildi deb belgilandi.")
    await callback.answer("O'qildi deb belgilandi")


@router.callback_query(F.data.startswith("fb_del:"))
async def on_fb_delete(callback: CallbackQuery):
    if not _is_admin(callback.from_user.id):
        await callback.answer("⛔ Ruxsat yo'q.", show_alert=True)
        return
    feedback_id = int(callback.data.split("fb_del:", 1)[1])
    await delete_feedback(feedback_id)
    await callback.message.edit_text(callback.message.text + "\n\n🗑 O'chirildi.")
    await callback.answer("O'chirildi")
