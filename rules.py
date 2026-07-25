# ============ QOIDALAR ============
from telegram import Update
from telegram.ext import ContextTypes
from game_roles import RULES_TEXT
from keyboards import back_to_main

async def rules_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Qoidalar"""
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(RULES_TEXT, reply_markup=back_to_main(), parse_mode="HTML")
