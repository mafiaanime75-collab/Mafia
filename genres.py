"""
Anime "dunyo"lari ro'yxati + lore generator + fuzzy qidiruv + aholi ismlari.

Do'stingizdan 60 ta anime nomini yuborsangiz, shu yerdagi ANIME_WORLDS
ro'yxatiga qo'shib/almashtirib chiqaman. Hozircha 60 ta bilan boshladim,
xohlasangiz 100 tagacha kengaytiramiz.
"""
import random

ANIME_WORLDS = [
    "Naruto", "One Piece", "Bleach", "Attack on Titan", "Death Note",
    "Dragon Ball", "Demon Slayer", "My Hero Academia", "Jujutsu Kaisen",
    "Tokyo Ghoul", "Fullmetal Alchemist", "Hunter x Hunter", "One Punch Man",
    "Code Geass", "Steins;Gate", "Neon Genesis Evangelion", "Cowboy Bebop",
    "Chainsaw Man", "Spy x Family", "Sword Art Online", "Fairy Tail",
    "Black Clover", "Haikyuu!!", "Mob Psycho 100", "Vinland Saga",
    "Re:Zero", "Overlord", "Tensei Slime", "Konosuba", "Violet Evergarden",
    "Your Name", "A Silent Voice", "Parasyte", "Assassination Classroom",
    "Seven Deadly Sins", "Dr. Stone", "Promised Neverland", "Noragami",
    "Blue Lock", "Kaguya-sama", "Toilet-Bound Hanako-kun", "Made in Abyss",
    "Berserk", "Hellsing", "JoJo's Bizarre Adventure", "Gintama",
    "Slam Dunk", "Inuyasha", "Yu Yu Hakusho", "Rurouni Kenshin",
    "Trigun", "Fruits Basket", "Erased", "Psycho-Pass", "Akame ga Kill",
    "Tokyo Revengers", "Mushoku Tensei", "Fire Force", "Kingdom",
    "Frieren",
]
assert len(set(ANIME_WORLDS)) == len(ANIME_WORLDS) == 60, "60 ta noyob dunyo bo'lishi kerak"

# Qo'lda yozilgan noyob lore — nechta xohlasa shuncha kengaytirish mumkin
ANIME_LORE = {
    "Naruto": {
        "world": "Yashirin Qishloqlar Olami",
        "villain_team": "Akatsuki soyalari",
        "intro": "Tun cho'kdi — Konoha ko'chalarida Akatsuki soyalari yashirinib, qishloq ahli orasidan qurbon tanlamoqda...",
    },
    "One Piece": {
        "world": "Grand Line Kemasi",
        "villain_team": "Yashirin Dengiz Qaroqchilari",
        "intro": "Kema tunda suzmoqda, ammo ekipaj orasida yashirin qaroqchilar bor — ular ertaga birontasini dengizga uloqtiradi...",
    },
    "Death Note": {
        "world": "Soya Daftari Shahri",
        "villain_team": "Kira izdoshlari",
        "intro": "Kimdir Daftarga ism yozmoqda... Tun tushishi bilan yana bir ism o'chadi.",
    },
    "Attack on Titan": {
        "world": "Devorlar Ichidagi Shahar",
        "villain_team": "Titanlarga Xizmat Qiluvchilar",
        "intro": "Devor ortida xavf kutmoqda, lekin haqiqiy dushman — o'z orangizda yashiringan xoin.",
    },
}

# Aholi ismlarini yasash uchun bo'g'in bloklari (har bir o'yinchiga tasodifiy, anime-uslub ism)
_NAME_PARTS_A = ["Aki", "Hiro", "Ren", "Sora", "Yuki", "Kaze", "Rin", "Shin", "Mio", "Kuro", "Sen", "Nao"]
_NAME_PARTS_B = ["taro", "chi", "kage", "maru", "mi", "to", "ka", "shi", "ru", "na", "ki", "zu"]


def generate_resident_name() -> str:
    return random.choice(_NAME_PARTS_A) + random.choice(_NAME_PARTS_B)


def _build_generic_lore(name: str) -> dict:
    templates = [
        "{name} olamida tungi sukunat cho'kishi bilanoq, yashirin dushman kuchlari orasingizdan birini tanlaydi.",
        "{name} dunyosida ishonch — eng qimmatli va eng xavfli qurol. Kim xoin, kim sodiq — faqat kunduz oshkor bo'ladi.",
        "{name} sarguzashti davom etmoqda, ammo bu safar jang maydoni sizning o'z jamoangiz ichida.",
    ]
    return {
        "world": f"{name} Olami",
        "villain_team": f"{name} Soya Klani",
        "intro": random.choice(templates).format(name=name),
    }


def get_lore(anime_name: str) -> dict:
    if anime_name in ANIME_LORE:
        return ANIME_LORE[anime_name]
    return _build_generic_lore(anime_name)


def search_worlds(query: str, limit: int = 8) -> list[str]:
    q = query.strip().lower()
    if not q:
        return ANIME_WORLDS[:limit]
    starts = [g for g in ANIME_WORLDS if g.lower().startswith(q)]
    contains = [g for g in ANIME_WORLDS if q in g.lower() and g not in starts]
    return (starts + contains)[:limit]
