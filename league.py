# ============ LIGA ============
from telegram import Update
from telegram.ext import ContextTypes
from database import db
from keyboards import league_keyboard, back_to_main
from config import LEAGUES

async def league_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Liga ma'lumotlari"""
    query = update.callback_query
    await query.answer()

    user_data = db.get_user(update.effective_user.id)
    current_league = user_data['league'] if user_data else 1
    games_played = user_data['games_played'] if user_data else 0

    league_info = LEAGUES.get(current_league, LEAGUES[1])
    next_league = LEAGUES.get(current_league + 1)

    # Liga tavsifi
    leagues_text = ""
    for league_id, info in LEAGUES.items():
        if league_id == current_league:
            leagues_text += f"\n<b>→ {info['icon']} {info['name']}</b> (Siz shu yerda)"
        elif league_id < current_league:
            leagues_text += f"\n✅ {info['icon']} {info['name']}"
        else:
            leagues_text += f"\n🔒 {info['icon']} {info['name']} ({info['min_games']} o'yin)"

    text = f"""
🏆 <b>LIGA</b> 🏆

<b>Sizning ligangiz:</b> {league_info['name']}
<b>O'ynalgan o'yinlar:</b> {games_played}

<b>📈 Liga tizimi:</b>
{leagues_text}

{"\n<b>🎯 Keyingi maqsad:</b>\n" + next_league['name'] + " ga o'tish uchun yana " + str(next_league['min_games'] - games_played) + " ta o'yin o'ynang!" if next_league else "\n🎉 <b>Tabriklaymiz!</b> Siz eng yuqori ligadasiz!"}

<b>💡 Maslahat:</b>
Ko'proq o'yin o'ynang va g'alaba qozoning - ligangiz oshadi!
    """

    await query.edit_message_text(text, reply_markup=league_keyboard(), parse_mode="HTML")

async def league_info_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Liga haqida batafsil"""
    query = update.callback_query
    await query.answer()

    text = """
📈 <b>LIGA HAQIDA</b> 📈

<b>Liga nima?</b>
Liga - bu sizning tajribangizni ko'rsatuvchi tizim. Ko'proq o'yin o'ynab, g'alaba qozonib, yuqori ligalarga ko'tariling!

<b>🏆 Ligalar:</b>
• 🥉 Bronza Liga - 0 o'yin
• 🥈 Kumush Liga - 10 o'yin
• 🥇 Oltin Liga - 30 o'yin
• 💎 Olmos Liga - 60 o'yin
• 👑 Qirol Liga - 100 o'yin
• 🔥 Afsona Liga - 150 o'yin
• ⚡ Xudo Liga - 220 o'yin
• 🌌 Koinot Liga - 300 o'yin

<b>⭐ Reyting:</b>
Har bir o'yinda reytingingiz oshadi:
• G'alaba: +10 reyting
• Mag'lubiyat: +2 reyting

<b>🎁 Liga bonuslari:</b>
Yuqori ligalarda ko'proq bonuslar ochiladi!
    """

    await query.edit_message_text(text, reply_markup=back_to_main(), parse_mode="HTML")

async def league_rating_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Liga reytingi"""
    query = update.callback_query
    await query.answer()

    top_users = db.get_top_users(20)

    rating_text = "\n".join([
        f"{i+1}. {user[2] or user[1] or 'Noma\'lum'} - {user[3]} ⭐ ({LEAGUES.get(user[5], LEAGUES[1])['name']})"
        for i, user in enumerate(top_users)
    ])

    text = f"""
🏆 <b>LIGA REYTINGI</b> 🏆

<b>Top 20 o'yinchii:</b>
{rating_text}

<b>💡 Maslahat:</b>
Ko'proq o'yin o'ynang va reytingingizni oshiring!
    """

    await query.edit_message_text(text, reply_markup=back_to_main(), parse_mode="HTML")
