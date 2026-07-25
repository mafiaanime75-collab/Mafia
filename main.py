# ============ ASOSIY FAYL ============
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    filters,
    ContextTypes
)

from config import BOT_TOKEN, ADMIN_ID
from database import db

# Handlers
from handlers.start import start_command, main_menu_callback
from handlers.shop import (
    shop_callback, shop_stones_callback, shop_coins_callback,
    buy_item_callback, locked_item_callback
)
from handlers.profile import profile_callback, inventory_callback, stats_callback
from handlers.league import league_callback, league_info_callback, league_rating_callback
from handlers.rating import rating_callback, global_rating_callback, friends_rating_callback
from handlers.daily_bonus import daily_bonus_callback, claim_bonus_callback
from handlers.game import (
    new_game_callback, anime_page_callback, select_anime_callback,
    start_game_callback
)
from handlers.admin import (
    admin_callback, admin_feedback_new_callback, admin_feedback_read_callback,
    admin_stats_callback, mark_read_command, delete_feedback_command,
    clear_read_command
)
from handlers.feedback import (
    feedback_callback, feedback_type_callback, receive_feedback,
    cancel_feedback, WAITING_FOR_FEEDBACK
)
from handlers.rules import rules_callback

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Asosiy funksiya"""
    print("🎮 AniMafia Bot ishga tushmoqda...")

    # Application yaratish
    application = Application.builder().token(BOT_TOKEN).build()

    # Conversation handler (taklif/shikoyat)
    feedback_conv = ConversationHandler(
        entry_points=[CallbackQueryHandler(feedback_type_callback, pattern="^feedback_")],
        states={
            WAITING_FOR_FEEDBACK: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_feedback)]
        },
        fallbacks=[CommandHandler("cancel", cancel_feedback)]
    )

    # Handlers
    # Komandalar
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("admin", admin_callback))
    application.add_handler(CommandHandler("read", mark_read_command))
    application.add_handler(CommandHandler("delete", delete_feedback_command))
    application.add_handler(CommandHandler("clear_read", clear_read_command))

    # Conversation
    application.add_handler(feedback_conv)

    # Callback querylar
    application.add_handler(CallbackQueryHandler(main_menu_callback, pattern="^main_menu$"))

    # Magazin
    application.add_handler(CallbackQueryHandler(shop_callback, pattern="^shop$"))
    application.add_handler(CallbackQueryHandler(shop_stones_callback, pattern="^shop_stones$"))
    application.add_handler(CallbackQueryHandler(shop_coins_callback, pattern="^shop_coins$"))
    application.add_handler(CallbackQueryHandler(buy_item_callback, pattern="^buy_"))
    application.add_handler(CallbackQueryHandler(locked_item_callback, pattern="^locked$"))

    # Profil
    application.add_handler(CallbackQueryHandler(profile_callback, pattern="^profile$"))
    application.add_handler(CallbackQueryHandler(inventory_callback, pattern="^inventory$"))
    application.add_handler(CallbackQueryHandler(stats_callback, pattern="^stats$"))

    # Liga
    application.add_handler(CallbackQueryHandler(league_callback, pattern="^league$"))
    application.add_handler(CallbackQueryHandler(league_info_callback, pattern="^league_info$"))
    application.add_handler(CallbackQueryHandler(league_rating_callback, pattern="^league_rating$"))

    # Reyting
    application.add_handler(CallbackQueryHandler(rating_callback, pattern="^rating$"))
    application.add_handler(CallbackQueryHandler(global_rating_callback, pattern="^global_rating$"))
    application.add_handler(CallbackQueryHandler(friends_rating_callback, pattern="^friends_rating$"))

    # Kunlik bonus
    application.add_handler(CallbackQueryHandler(daily_bonus_callback, pattern="^daily_bonus$"))
    application.add_handler(CallbackQueryHandler(claim_bonus_callback, pattern="^claim_bonus$"))
    application.add_handler(CallbackQueryHandler(daily_bonus_callback, pattern="^bonus_info$"))
    application.add_handler(CallbackQueryHandler(daily_bonus_callback, pattern="^bonus_claimed$"))

    # O'yin
    application.add_handler(CallbackQueryHandler(new_game_callback, pattern="^new_game$"))
    application.add_handler(CallbackQueryHandler(anime_page_callback, pattern="^anime_page_"))
    application.add_handler(CallbackQueryHandler(select_anime_callback, pattern="^select_anime_"))
    application.add_handler(CallbackQueryHandler(start_game_callback, pattern="^start_game$"))

    # Admin
    application.add_handler(CallbackQueryHandler(admin_callback, pattern="^admin_panel$"))
    application.add_handler(CallbackQueryHandler(admin_feedback_new_callback, pattern="^admin_feedback_new$"))
    application.add_handler(CallbackQueryHandler(admin_feedback_read_callback, pattern="^admin_feedback_read$"))
    application.add_handler(CallbackQueryHandler(admin_stats_callback, pattern="^admin_stats$"))

    # Taklif/Shikoyat
    application.add_handler(CallbackQueryHandler(feedback_callback, pattern="^feedback$"))

    # Qoidalar
    application.add_handler(CallbackQueryHandler(rules_callback, pattern="^rules$"))

    # Botni ishga tushirish
    print("✅ Bot ishga tushdi!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
