"""
O'yin dvigateli — klassik Mafia (Werewolf) qoidalarining anime-uslubdagi
qayta ishlangan versiyasi. Rollar universal (istalgan tanlangan anime
janriga moslashadi), faqat nomlar va lore matnlar tanlangan janrga
qarab data/genres.py orqali "bo'yaladi".

ROLLAR:
  OYABUN      - Mafia yetakchisi (klassik "Don"). Har kecha bitta o'yinchini
                yo'q qilishni tanlaydi (o'z jamoasi bilan maslahatlashib).
  KAGE        - Mafia a'zosi/soyasi. Oyabun bilan birga tungi ovoz beradi.
  MEITANTEI   - Buyuk detektiv (klassik "Komissar"). Har kecha bitta
                o'yinchini tekshirib, u mafiami-emasmi bilib oladi.
  IYASHI-NIN  - Shifokor. Har kecha bitta o'yinchini himoya qiladi
                (o'zini ketma-ket 2 marta himoya qila olmaydi).
  NAKAMA      - Oddiy fuqaro. Maxsus qobiliyati yo'q, faqat kunduzi ovoz beradi.

G'alaba shartlari klassik mafiaga to'liq mos:
  - Mafia soni tinch aholi soniga teng yoki ko'p bo'lsa -> Mafia g'alabasi
  - Barcha mafia a'zolari yo'q qilinsa -> Tinch aholi g'alabasi
"""
import random
from dataclasses import dataclass, field
from enum import Enum


class Role(str, Enum):
    OYABUN = "OYABUN"          # Mafia boshlig'i
    KAGE = "KAGE"              # Mafia a'zosi
    MEITANTEI = "MEITANTEI"    # Detektiv
    IYASHI = "IYASHI"          # Shifokor
    NAKAMA = "NAKAMA"          # Tinch aholi


ROLE_LABELS_UZ = {
    Role.OYABUN: "🐍 Oyabun (Mafia Boshlig'i)",
    Role.KAGE: "🗡 Kage (Mafia Soyasi)",
    Role.MEITANTEI: "🔍 Meitantei (Detektiv)",
    Role.IYASHI: "💊 Iyashi-nin (Shifokor)",
    Role.NAKAMA: "👤 Nakama (Tinch Aholi)",
}

MAFIA_ROLES = {Role.OYABUN, Role.KAGE}


def build_role_list(player_count: int) -> list[Role]:
    """
    O'yinchilar soniga qarab rol ro'yxatini tuzadi.
    Nisbat: mafia ~ jami o'yinchilarning 25-30% atrofida, 1 detektiv, 1 shifokor
    (agar o'yinchi yetarli bo'lsa), qolganlari tinch aholi.
    """
    if player_count < 5:
        raise ValueError("Kamida 5 ta o'yinchi kerak")

    mafia_count = max(1, round(player_count * 0.28))
    roles: list[Role] = [Role.OYABUN]
    mafia_count -= 1
    roles += [Role.KAGE] * mafia_count

    roles.append(Role.MEITANTEI)
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
    role: Role = Role.NAKAMA
    alive: bool = True


@dataclass
class GameState:
    session_id: str
    group_id: int
    genre: str
    players: dict[int, Player] = field(default_factory=dict)
    phase: str = "lobby"          # lobby | night | day_discussion | voting | finished
    day_number: int = 0
    night_kill_target: int | None = None
    doctor_protect_target: int | None = None
    doctor_last_protect: int | None = None
    votes: dict[int, int] = field(default_factory=dict)   # voter_id -> target_id
    winner: str | None = None      # "mafia" | "nakama" | None

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
        """Tungi harakatlarni hisoblash: o'ldirish va davolashni solishtirish."""
        target = self.night_kill_target
        if target is not None and target == self.doctor_protect_target:
            target = None  # shifokor qutqarib qoldi
        if target is not None and target in self.players:
            self.players[target].alive = False
        self.doctor_last_protect = self.doctor_protect_target
        self.night_kill_target = None
        self.doctor_protect_target = None
        return target

    def resolve_vote(self) -> int | None:
        """Kunduzgi ovoz berish natijasini hisoblash — eng ko'p ovoz olgan chiqib ketadi."""
        if not self.votes:
            return None
        tally: dict[int, int] = {}
        for target in self.votes.values():
            tally[target] = tally.get(target, 0) + 1
        max_votes = max(tally.values())
        top = [uid for uid, v in tally.items() if v == max_votes]
        if len(top) > 1:
            return None  # durrang - hech kim chiqmaydi
        chosen = top[0]
        if chosen in self.players:
            self.players[chosen].alive = False
        self.votes.clear()
        return chosen


def compute_elo_delta(won: bool, base: int = 20) -> int:
    return base if won else -base // 2


def compute_currency_reward(won: bool, is_mvp: bool = False) -> int:
    reward = 50 if won else 15
    if is_mvp:
        reward += 30
    return reward
