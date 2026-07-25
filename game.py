# ============ O'YIN BOSHQARUVI ============
from telegram import Update
from telegram.ext import ContextTypes
from database import db
from keyboards import anime_select_keyboard, join_game_keyboard, game_admin_keyboard, back_to_main
from anime_worlds import ANIME_WORLDS
from game_roles import get_roles_distribution
from config import MIN_PLAYERS, MAX_PLAYERS
import random

# Aktiv o'yinlar
active_games = {}

async def new_game_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Yangi o'yin boshlash"""
    query = update.callback_query
    await query.answer()

    # Anime tanlash
    text = """
🎮 <b>YANGI O'YIN BOSHLASH</b> 🎮

<b>Anime olamini tanlang:</b>

Pastdagi ro'yxatdan o'zingiz yoqtirgan anime ni tanlang yoki qidirish tugmasidan foydalaning!

💡 Maslahat: Har bir anime o'ziga xos personajlarga ega!
    """

    await query.edit_message_text(text, reply_markup=anime_select_keyboard(ANIME_WORLDS), parse_mode="HTML")

async def anime_page_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Anime sahifasi"""
    query = update.callback_query
    await query.answer()

    page = int(query.data.split("_")[-1])

    text = """
🎮 <b>YANGI O'YIN BOSHLASH</b> 🎮

<b>Anime olamini tanlang:</b>

Pastdagi ro'yxatdan tanlang!
    """

    await query.edit_message_text(text, reply_markup=anime_select_keyboard(ANIME_WORLDS, page), parse_mode="HTML")

async def select_anime_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Anime tanlash"""
    query = update.callback_query
    await query.answer()

    anime_name = query.data.replace("select_anime_", "")
    anime_data = ANIME_WORLDS.get(anime_name)

    if not anime_data:
        await query.answer("❌ Xatolik!", show_alert=True)
        return

    # Guruh ID sini olish
    chat_id = update.effective_chat.id

    # O'yin yaratish
    game_id = db.create_game(chat_id, anime_name)

    # Aktiv o'yinlarga qo'shish
    active_games[game_id] = {
        'anime': anime_name,
        'players': [],
        'status': 'waiting',
        'chat_id': chat_id
    }

    text = f"""
🎮 <b>YANGI O'YIN YARATILDI!</b> 🎮

<b>🌸 Anime olami:</b> {anime_data['icon']} {anime_name}
<b>🆔 O'yin ID:</b> <code>{game_id}</code>

<b>👥 O'yinchilar:</b> 0 / {MAX_PLAYERS}

<b>➕ Q'oshilish uchun pastdagi tugmani bosing!</b>

⚠️ Kamida {MIN_PLAYERS} ta o'yinchii kerak!
    """

    await query.edit_message_text(text, reply_markup=join_game_keyboard(game_id), parse_mode="HTML")

async def join_game(update: Update, context: ContextTypes.DEFAULT_TYPE, game_id=None):
    """O'yini qo'shilish"""
    user = update.effective_user

    if not game_id and context.args:
        game_id = int(context.args[0].split("_")[1])

    if game_id not in active_games:
        await update.message.reply_text("❌ Bu o'yin topilmadi yoki tugagan!")
        return

    game = active_games[game_id]

    if user.id in [p['id'] for p in game['players']]:
        await update.message.reply_text("❌ Siz allaqachon bu o'yinda qatnashyapsiz!")
        return

    if len(game['players']) >= MAX_PLAYERS:
        await update.message.reply_text("❌ O'yin to'ldi!")
        return

    # Foydalanuvchini qo'shish
    game['players'].append({
        'id': user.id,
        'name': user.first_name,
        'username': user.username
    })

    # Bazaga yangilash
    db.update_game(game_id, players=game['players'])

    await update.message.reply_text(
        f"✅ <b>Siz o'yini qo'shildingiz!</b>

"
        f"🌸 Anime: {ANIME_WORLDS[game['anime']]['icon']} {game['anime']}
"
        f"👥 O'yinchilar: {len(game['players'])} / {MAX_PLAYERS}",
        parse_mode="HTML"
    )

    # Guruhga xabar
    if len(game['players']) >= MIN_PLAYERS:
        await context.bot.send_message(
            game['chat_id'],
            f"🎮 <b>Yangi o'yinchii qo'shildi!</b>

"
            f"👤 {user.first_name}
"
            f"👥 Jami: {len(game['players'])} ta

"
            f"⏳ O'yinni boshlash mumkin!",
            parse_mode="HTML"
        )

async def start_game_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """O'yinni boshlash"""
    query = update.callback_query
    await query.answer()

    # Bu funksiya guruhda ishlaydi
    # Admin tekshiruvi
    chat_member = await context.bot.get_chat_member(update.effective_chat.id, update.effective_user.id)
    if chat_member.status not in ['administrator', 'creator']:
        await query.answer("❌ Faqat adminlar o'yin boshlashi mumkin!", show_alert=True)
        return

    # Aktiv o'yinni topish
    chat_id = update.effective_chat.id
    game = None
    game_id = None

    for gid, gdata in active_games.items():
        if gdata['chat_id'] == chat_id and gdata['status'] == 'waiting':
            game = gdata
            game_id = gid
            break

    if not game:
        await query.answer("❌ Aktiv o'yin topilmadi!", show_alert=True)
        return

    if len(game['players']) < MIN_PLAYERS:
        await query.answer(f"❌ Kamida {MIN_PLAYERS} ta o'yinchii kerak!", show_alert=True)
        return

    # Rollarni taqsimlash
    roles = get_roles_distribution(len(game['players']))
    random.shuffle(roles)

    anime = ANIME_WORLDS[game['anime']]

    # Har bir o'yinchiga rolni yuborish
    for i, player in enumerate(game['players']):
        role = roles[i]

        # Anime personajini tanlash
        if role in anime['characters']['tinchlik']:
            character = anime['characters']['tinchlik'][role]
            team = "🕊️ TINCHLIK TARAFI"
        elif role in anime['characters']['mafia']:
            character = anime['characters']['mafia'][role]
            team = "🖤 MAFIYA"
        else:
            character = anime['characters']['yolg'iz'][role]
            team = "⚔️ YOLG'IZ O'YINCHI"

        try:
            await context.bot.send_message(
                player['id'],
                f"""
🎭 <b>SIZNING ROLINGIZ</b> 🎭

<b>🌸 Anime:</b> {anime['icon']} {game['anime']}
<b>🎭 Sizning personajingiz:</b> {character}
<b>📋 Rolingiz:</b> {role}
<b>🎯 Jamoa:</b> {team}

<b>💡 Eslatma:</b>
• Rolingizni maxfiy saqlang!
• Tunda faqat o'z navbatingizda gapiring
• Strategiya ishlab chiqing!

<b>🍀 O'yinda omad!</b>
                """,
                parse_mode="HTML"
            )
        except Exception as e:
            print(f"Xabar yuborishda xatolik: {e}")

    # Guruhga xabar
    game['status'] = 'playing'
    db.update_game(game_id, status='playing', roles={str(p['id']): roles[i] for i, p in enumerate(game['players'])})

    await query.edit_message_text(
        f"""
🎮 <b>O'YIN BOSHLANDI!</b> 🎮

<b>🌸 Anime olami:</b> {anime['icon']} {game['anime']}
<b>👥 O'yinchilar:</b> {len(game['players'])} ta

<b>🌙 Tungi bosqich boshlanmoqda...</b>

Har bir o'yinchiga roli yuborildi! ✅
        """,
        parse_mode="HTML"
    )
