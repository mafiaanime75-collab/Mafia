"""
100 ta anime turi (janr/nom) va har biri uchun o'yin syujetini "moslashtiruvchi"
flavor-matn generatori.

Har bir janr uchun to'liq qo'lda yozilgan noyob lore ANIME_LORE lug'atida,
qolganlari uchun esa GENERIC lar asosida avtomatik, lekin nomga mos matn
generatsiya qilinadi (_build_generic_lore). Xohlasangiz istalgan nechta
janr uchun ANIME_LORE ichiga qo'lda noyob matn qo'shishingiz mumkin —
tuzilma bir xil turadi.
"""
import random

# 100 ta mashhur anime nomi (foydalanuvchi qidiruv orqali shulardan birini tanlaydi)
ANIME_GENRES = [
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
    "Shingeki no Bahamut", "Seraph of the End", "Tokyo Revengers",
    "The Devil is a Part-Timer", "Mushoku Tensei", "The Rising of the Shield Hero",
    "Fire Force", "Dorohedoro", "Kingdom", "Golden Kamuy",
    "Monster", "Great Teacher Onizuka", "Beelzebub", "Nichijou",
    "Clannad", "Angel Beats!", "Anohana", "Toradora!", "Your Lie in April",
    "K-On!", "Lucky Star", "Bakemonogatari", "Durarara!!", "Baccano!",
    "Samurai Champloo", "Ping Pong the Animation",
    "Devilman Crybaby", "Kill la Kill", "Darling in the Franxx",
    "Guilty Crown", "Akudama Drive", "The Great Pretender",
    "86 Eighty-Six", "To Your Eternity", "Ranking of Kings",
    "Wonder Egg Priority", "Deca-Dence", "Kemono Jihen", "Vanitas no Karte",
    "Spy Classroom", "Skip and Loafer", "Frieren", "Solo Leveling",
    "Delicious in Dungeon", "Blue Exorcist",
]
assert len(set(ANIME_GENRES)) == len(ANIME_GENRES) == 100, "Ro'yxat aynan 100 ta noyob nomdan iborat bo'lishi shart"

# Qo'lda yozilgan noyob lore — xohlagancha kengaytirish mumkin
ANIME_LORE = {
    "Naruto": {
        "world": "Yashirin Qishloqlar Olami",
        "villain_team": "Akatsuki soyalari",
        "hero_role": "Konoha Meitantei-si",
        "healer_role": "Klan Tabibi",
        "civilian_role": "Qishloq Shinobisi",
        "intro": "Tun cho'kdi — Konoha ko'chalarida Akatsuki soyalari yashirinib, qishloq ahli orasidan qurbon tanlamoqda...",
    },
    "One Piece": {
        "world": "Grand Line Kemasi",
        "villain_team": "Yashirin Dengiz Qaroqchilari",
        "hero_role": "Kemadagi Detektiv",
        "healer_role": "Kema Shifokori",
        "civilian_role": "Ekipaj A'zosi",
        "intro": "Kema tunda suzmoqda, ammo ekipaj orasida yashirin qaroqchilar bor — ular ertaga birontasini dengizga uloqtiradi...",
    },
    "Death Note": {
        "world": "Soya Daftari Shahri",
        "villain_team": "Kira izdoshlari",
        "hero_role": "L Klassi Tergovchi",
        "healer_role": "Shinigami Homiysi",
        "civilian_role": "Fuqaro",
        "intro": "Kimdir Daftarga ism yozmoqda... Tun tushishi bilan yana bir ism o'chadi.",
    },
    "Attack on Titan": {
        "world": "Devorlar Ichidagi Shahar",
        "villain_team": "Titanlarga Xizmat Qiluvchilar",
        "hero_role": "Разведка Otryadi Detektivi",
        "healer_role": "Qo'shin Shifokori",
        "civilian_role": "Devor Fuqarosi",
        "intro": "Devor ortida xavf kutmoqda, lekin haqiqiy dushman — o'z orangizda yashiringan xoin.",
    },
}


def _build_generic_lore(name: str) -> dict:
    """Qo'lda lore yozilmagan janrlar uchun avtomatik, lekin nomga moslashtirilgan lore."""
    templates = [
        "{name} olamida tungi sukunat cho'kishi bilanoq, yashirin dushman kuchlari orasingizdan birini tanlaydi.",
        "{name} dunyosida ishonch — eng qimmatli va eng xavfli qurol. Kim xoin, kim sodiq — faqat kunduz oshkor bo'ladi.",
        "{name} sarguzashti davom etmoqda, ammo bu safar jang maydoni sizning o'z jamoangiz ichida.",
    ]
    return {
        "world": f"{name} Olami",
        "villain_team": f"{name} Soya Klani",
        "hero_role": f"{name} Detektivi",
        "healer_role": f"{name} Tabibi",
        "civilian_role": f"{name} Qahramoni",
        "intro": random.choice(templates).format(name=name),
    }


def get_lore(anime_name: str) -> dict:
    if anime_name in ANIME_LORE:
        return ANIME_LORE[anime_name]
    return _build_generic_lore(anime_name)


def search_genres(query: str, limit: int = 8) -> list[str]:
    """
    Oddiy, tez "typeahead" qidiruv: avval so'z boshidan mos kelganlar,
    keyin ichida uchraydiganlar chiqadi (masalan "na" -> "Naruto").
    """
    q = query.strip().lower()
    if not q:
        return ANIME_GENRES[:limit]
    starts = [g for g in ANIME_GENRES if g.lower().startswith(q)]
    contains = [g for g in ANIME_GENRES if q in g.lower() and g not in starts]
    return (starts + contains)[:limit]
