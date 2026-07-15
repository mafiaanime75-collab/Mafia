"""
O'yin dvigateli. Qoida: o'yinchi soni qancha bo'lmasin (4-20 orasida),
HAR DOIM kamida bitta Oyabun (mafia) va bitta Meitantei (komissar/detektiv)
bo'lishi SHART.
"""
import random
from dataclasses import dataclass, field
from enum import Enum


class Role(str, Enum):
    OYABUN = "OYABUN"        # Mafia boshlig'i (Don)
    KAGE = "KAGE"             # Mafia a'zosi
    MEITANTEI = "MEITANTEI"   # Detektiv/Komissar
    IYASHI = "IYASHI"         # Shifokor
    NAKAMA = "NAKAMA"         # Tinch aholi


ROLE_LABELS_UZ = {
    Role.OYABUN: "🐍 Oyabun (Mafia Boshlig'i)",
    Role.KAGE: "🗡 Kage (Mafia Soyasi)",
    Role.MEITANTEI: "🔍 Meitantei (Komissar)",
    Role.IYASHI: "💊 Iyashi-nin (Shifokor)",
    Role.NAKAMA: "👤 Nakama (Tinch Aholi)",
}

MAFIA_ROLES = {Role.OYABUN, Role.KAGE}


def build_role_list(player_count: int) -> list[Role]:
    """
    Qoida: player_count 4 dan 20 gacha. HAR DOIM kamida 1 Oyabun + 1 Meitantei bor.
    Mafia umumiy soni ~ o'yinchilarning 25-30% (lekin kamida 1 ta).
    """
    if player_count < 4:
        raise ValueError("Kamida 4 ta o'yinchi kerak")
    if player_count > 20:
        raise ValueError("Ko'pi bilan 20 ta o'yinchi bo'lishi mumkin")

    mafia_count = max(1, round(player_count * 0.28))
    roles: list[Role] = [Role.OYABUN]           # majburiy: kamida 1 mafia boshlig'i
    roles += [Role.KAGE] * (mafia_count - 1)     # qolgan mafia a'zolari
    roles.append(Role.MEITANTEI)                 # majburiy: kamida 1 komissar

    if player_count >= 7:
        roles.append(Role.IYASHI)

    while len(roles) < player_count:
        roles.append(Role.NAKAMA)

    random.shuffle(roles)
    return roles[:player_count]


@dataclass
class Player:
    user_id: int
    full_name: str
    resident_name: str = ""   # anime-uslub o'yin ichidagi taxallus
    role: Role = Role.NAKAMA
    alive: bool = True


@dataclass
class GameState:
    session_id: str
    group_id: int
    world: str
    players: dict[int, Player] = field(default_factory=dict)
    phase: str = "lobby"
    day_number: int = 0
    night_kill_target: int | None = None
    doctor_protect_target: int | None = None
    doctor_last_protect: int | None = None
    votes: dict[int, int] = field(default_factory=dict)
    winner: str | None = None

    def alive_players(self) -> list[Player]:
        return [p for p in self.players.values() if p.alive]

    def alive_mafia(self) -> list[Player]:
        return [p for p in self.alive_players() if p.role in MAFIA_ROLES]

    def alive_civilians(self) -> list[Player]:
        return [p for p in self.alive_players() if p.role not in MAFIA_ROLES]

    def check_winner(self) -> str | None:
        mafia = len(self.alive_mafia())
        civ = len(self.alive_civilians())
        if mafia == 0:
            return "nakama"
        if mafia >= civ:
            return "mafia"
        return None

    def resolve_night(self):
        target = self.night_kill_target
        if target is not None and target == self.doctor_protect_target:
            target = None
        if target is not None and target in self.players:
            self.players[target].alive = False
        self.doctor_last_protect = self.doctor_protect_target
        self.night_kill_target = None
        self.doctor_protect_target = None
        return target

    def resolve_vote(self) -> int | None:
        if not self.votes:
            return None
        tally: dict[int, int] = {}
        for target in self.votes.values():
            tally[target] = tally.get(target, 0) + 1
        max_votes = max(tally.values())
        top = [uid for uid, v in tally.items() if v == max_votes]
        if len(top) > 1:
            return None
        chosen = top[0]
        if chosen in self.players:
            self.players[chosen].alive = False
        self.votes.clear()
        return chosen


def compute_elo_delta(won: bool, base: int = 20) -> int:
    return base if won else -base // 2


def compute_kizuna_reward(won: bool, is_mvp: bool = False) -> int:
    reward = 50 if won else 15
    if is_mvp:
        reward += 30
    return reward
