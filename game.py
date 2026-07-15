import asyncio

from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from lobby_handler import ACTIVE_LOBBIES
from genres import get_lore, get_resident_pool, search_worlds
from game_engine import GameState, Player, build_role_list, Role, role_label, \
    compute_elo_delta, compute_kizuna_reward
from keyboards import night_action_kb, vote_kb, world_results_kb
from database import update_user_after_game, update_group_rating
from states import WorldSelect
from config import MIN_PLAYERS, NIGHT_DURATION_SEC, DAY_DISCUSSION_SEC, VOTING_DURATION_SEC

router = Router(name="game_handler")

RUNNING_GAMES: dict[str, GameState] = {}
# host_id -> session_id (o'yin boshlanishi kutilayotgan lobby)
PENDING_WORLD_SELECTION: dict[int, str] = {}


@router.callback_query(F.data.startswith("lobby_start:"))
async def on_lobby_start(callback: CallbackQuery, state: FSMContext):
    session_id = callback.data.split("lobby_start:", 1)[1]
    lobby = ACTIVE_LOBBIES.get(session_id)
    if not lobby:
        await callback.answer("Lobby topilmadi.", show_alert=True)
        return
    if callback.from_user.id != lobby["host_id"]:
        await callback.answer("Faqat lobby ochgan odam o'yinni boshlaydi.", show_alert=True)
        return
    if len(lobby["players"]) < MIN_PLAYERS:
        await callback.answer(f"Kamida {MIN_PLAYERS} o'yinchi kerak!", show_alert=True)
        return

    PENDING_WORLD_SELECTION[callback.from_user.id] = session_id
    await state.set_state(WorldSelect.waiting_query)
    await state.update_data(session_id=session_id)

    await callback.message.answer(
        f"🌍 <b>{callback.from_user.full_name}</b>, o'yin uchun ANIME DUNYOSINI tanlang!\n"
        f"Nomini yozing (masalan: <i>naruto</i>, <i>tokyo</i>...):"
    )
    await callback.answer()


@router.message(WorldSelect.waiting_query, F.text)
async def on_world_query(message: Message, state: FSMContext):
    data = await state.get_data()
    session_id = data.get("session_id")
    if not session_id or PENDING_WORLD_SELECTION.get(message.from_user.id) != session_id:
        return  # bu holat boshqa foydalanuvchiga tegishli emas

    results = search_worlds(message.text.strip(), limit=8)
    if not results:
        await message.answer("Bunday dunyo topilmadi 😔 Boshqa nom bilan urinib ko'ring.")
        return
    await message.answer("🔎 Natijalar:", reply_markup=world_results_kb(results))


@router.callback_query(F.data.startswith("world:"))
async def on_world_chosen(callback: CallbackQuery, state: FSMContext, bot: Bot):
    world = callback.data.split("world:", 1)[1]
    data = await state.get_data()
    session_id = data.get("session_id")
    if not session_id or PENDING_WORLD_SELECTION.get(callback.from_user.id) != session_id:
        await callback.answer("Bu tanlov sizga tegishli emas.", show_alert=True)
        return

    lobby = ACTIVE_LOBBIES.get(session_id)
    if not lobby:
        await callback.answer("Lobby endi mavjud emas.", show_alert=True)
        return

    lobby["world"] = world
    PENDING_WORLD_SELECTION.pop(callback.from_user.id, None)
    await state.clear()

    lore = get_lore(world)
    await callback.message.edit_text(
        f"🎴 Tanlangan dunyo: <b>{world}</b>\n🌍 {lore['world']}\n\n{lore['intro']}\n\nO'yin boshlanmoqda..."
    )
    await callback.answer()

    await _start_actual_game(bot, callback.message.chat.id, session_id, world)


async def _start_actual_game(bot: Bot, group_id: int, session_id: str, world: str):
    lobby = ACTIVE_LOBBIES.get(session_id)
    if not lobby:
        return

    game = GameState(session_id=session_id, group_id=group_id, world=world)
    roles = build_role_list(len(lobby["players"]))
    resident_pool = get_resident_pool(world).copy()
    import random
    random.shuffle(resident_pool)

    for i, (uid, name) in enumerate(lobby["players"].items()):
        resident_name = resident_pool[i % len(resident_pool)]
        role = roles[i]
        game.players[uid] = Player(user_id=uid, full_name=name, resident_name=resident_name, role=role)

    RUNNING_GAMES[session_id] = game

    lore = get_lore(world)
    roster = "\n".join(f"• {p.full_name} → <b>{p.resident_name}</b>" for p in game.players.values())
    await bot.send_message(
        group_id,
        f"🎬 <b>O'yin boshlandi!</b>\nDunyo: <b>{world}</b> — {lore['world']}\n\n"
        f"🧑‍🤝‍🧑 Aholi ismlari:\n{roster}\n\n"
        f"Rollar shaxsiy xabar orqali yuborildi. Omad tilaymiz!",
    )

    for p in game.players.values():
        try:
            await bot.send_message(
                p.user_id,
                f"🎭 Sizning rolingiz: <b>{role_label(p.role, world)}</b>\n"
                f"🏷 Bu o'yindagi ismingiz: <b>{p.resident_name}</b>\n"
                f"Dunyo: {world} ({lore['world']})",
            )
        except Exception:
            pass

    asyncio.create_task(run_game_loop(bot, session_id))


async def run_game_loop(bot: Bot, session_id: str):
    game = RUNNING_GAMES.get(session_id)
    if not game:
        return
    world = game.world

    while True:
        game.day_number += 1
        game.phase = "night"
        await bot.send_message(
            game.group_id,
            f"🌙 <b>{game.day_number}-tun</b> boshlandi. Maxsus rolli o'yinchilar shaxsiy xabarda harakat qilsin "
            f"({NIGHT_DURATION_SEC} soniya)...",
        )
        await send_night_prompts(bot, game)
        await asyncio.sleep(NIGHT_DURATION_SEC)

        killed = game.resolve_night()
        winner = game.check_winner()
        if killed:
            name = game.players[killed].resident_name
            await bot.send_message(game.group_id, f"☠️ Tunda <b>{name}</b> yo'q qilindi.")
        else:
            await bot.send_message(game.group_id, "🌤 Bu tun hech kim halok bo'lmadi.")

        if winner:
            await finish_game(bot, game, winner)
            return

        game.phase = "day_discussion"
        alive_names = ", ".join(p.resident_name for p in game.alive_players())
        await bot.send_message(
            game.group_id,
            f"☀️ <b>{game.day_number}-kun</b>. Tirik qolganlar: {alive_names}\n"
            f"Muhokama vaqti ({DAY_DISCUSSION_SEC} soniya) — kim shubhali ekanini muhokama qiling.",
        )
        await asyncio.sleep(DAY_DISCUSSION_SEC)

        game.phase = "voting"
        targets = [(p.user_id, p.resident_name) for p in game.alive_players()]
        await bot.send_message(
            game.group_id,
            "🗳 Ovoz berish vaqti! Kimni chiqarib yubormoqchisiz?",
            reply_markup=vote_kb(session_id, targets),
        )
        await asyncio.sleep(VOTING_DURATION_SEC)

        voted_out = game.resolve_vote()
        winner = game.check_winner()
        if voted_out:
            name = game.players[voted_out].resident_name
            role_name = role_label(game.players[voted_out].role, world)
            await bot.send_message(
                game.group_id, f"⚖️ Ovoz natijasida <b>{name}</b> chiqarib yuborildi. Roli: {role_name}"
            )
        else:
            await bot.send_message(game.group_id, "🤷 Ovozlar teng — hech kim chiqarilmadi.")

        if winner:
            await finish_game(bot, game, winner)
            return


async def send_night_prompts(bot: Bot, game: GameState):
    alive = game.alive_players()
    world = game.world
    for p in alive:
        if p.role in (Role.OYABUN, Role.KAGE):
            targets = [(t.user_id, t.resident_name) for t in alive if t.role not in (Role.OYABUN, Role.KAGE)]
            try:
                await bot.send_message(
                    p.user_id, f"🗡 ({role_label(p.role, world)}) Bu kecha kimni yo'q qilamiz?",
                    reply_markup=night_action_kb(game.session_id, targets, "kill"),
                )
            except Exception:
                pass
        elif p.role == Role.MEITANTEI:
            targets = [(t.user_id, t.resident_name) for t in alive if t.user_id != p.user_id]
            try:
                await bot.send_message(
                    p.user_id, f"🔍 ({role_label(p.role, world)}) Kimni tekshiramiz?",
                    reply_markup=night_action_kb(game.session_id, targets, "check"),
                )
            except Exception:
                pass
        elif p.role == Role.IYASHI:
            targets = [(t.user_id, t.resident_name) for t in alive]
            try:
                await bot.send_message(
                    p.user_id, f"💊 ({role_label(p.role, world)}) Kimni himoya qilamiz?",
                    reply_markup=night_action_kb(game.session_id, targets, "heal"),
                )
            except Exception:
                pass


@router.callback_query(F.data.startswith("act:"))
async def on_night_action(callback: CallbackQuery):
    _, action, session_id, target_id = callback.data.split(":")
    target_id = int(target_id)
    game = RUNNING_GAMES.get(session_id)
    if not game:
        await callback.answer("O'yin topilmadi.", show_alert=True)
        return

    if action == "kill":
        game.night_kill_target = target_id
        await callback.answer("Tanlov qabul qilindi 🗡")
    elif action == "heal":
        if target_id == game.doctor_last_protect:
            await callback.answer("Bir xil odamni ketma-ket himoya qila olmaysiz!", show_alert=True)
            return
        game.doctor_protect_target = target_id
        await callback.answer("Himoya o'rnatildi 💊")
    elif action == "check":
        target = game.players.get(target_id)
        is_mafia = target and target.role in (Role.OYABUN, Role.KAGE)
        await callback.answer(
            f"Natija: {'🩸 U MAFIA!' if is_mafia else '✅ U tinch aholi.'}", show_alert=True
        )


@router.callback_query(F.data.startswith("vote:"))
async def on_vote(callback: CallbackQuery):
    _, session_id, target_id = callback.data.split(":")
    game = RUNNING_GAMES.get(session_id)
    if not game:
        await callback.answer("O'yin topilmadi.", show_alert=True)
        return
    game.votes[callback.from_user.id] = int(target_id)
    await callback.answer("Ovozingiz qabul qilindi ✅")


async def finish_game(bot: Bot, game: GameState, winner: str):
    game.phase = "finished"
    winner_label = "🩸 Mafia" if winner == "mafia" else "🕊 Nakama (Tinch aholi)"
    await bot.send_message(game.group_id, f"🏁 <b>O'yin tugadi!</b> G'olib: {winner_label}")

    for p in game.players.values():
        won = (winner == "mafia" and p.role in (Role.OYABUN, Role.KAGE)) or \
              (winner == "nakama" and p.role not in (Role.OYABUN, Role.KAGE))
        elo_delta = compute_elo_delta(won)
        reward = compute_kizuna_reward(won)
        await update_user_after_game(p.user_id, won, elo_delta, reward)
        await update_group_rating(game.group_id, p.user_id, won, elo_delta)

    RUNNING_GAMES.pop(game.session_id, None)
    ACTIVE_LOBBIES.pop(game.session_id, None)
