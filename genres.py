"""
100 ta anime "dunyosi" (o'yin o'ynaladigan olam) + har biri uchun:
  - qisqa lore (villain_team, intro)
  - ROL NOMLARI (Oyabun/Meitantei va h.k. endi HAR BIR dunyoda boshqacha —
    bitta doim bir xil nom bilan qolib ketmaydi)
  - ALOHIDA aholi ismlari ro'yxati — 20 tadan mashhur anime uchun HAQIQIY
    personaj ismlari, qolganlari uchun esa dunyo nomiga qarab har xil
    chiqadigan (lekin tasodifiy bo'g'in emas) generik ism to'plami.

Ro'yxatning katta qismi foydalanuvchi (Davronbek) yuborgan 71 ta nom —
ba'zilari juda uzun bo'lgani uchun tugma/xabarlarda qisqartirilgan holda
qoldirildi (asl uzun nomi izohda ko'rsatilgan).
"""
import random

# ----------------------------------------------------------------------
# 100 TA DUNYO
# ----------------------------------------------------------------------
WORLDS = [
    # --- Davronbek yuborgan ro'yxat (71 ta, ba'zilari qisqartirilgan) ---
    "O'lmas sarguzashtchi", "Shamolni bo'ysundirish", "Iblislar lordi ishda",
    "Jonli efirda jang", "Buchchigiri", "Sening isming", "Ovoz shakli",
    "Solo Leveling", "Men yomon ko'rgan sinfdoshimga uylandim",
    "Medaka meni jozibadorligimga tushunmaydi", "Zanjirlangan askar",
    "Sehr va mushaklar", "O'zga dunyoda darajamni oshirib bu dunyoda ham kuchli bo'ldim",
    "Lookizm", "Baholash qobiliyati eng kuchlisi bo'lib chiqdi",
    "Men eng kuchli sarguzashtchi bo'lish uchun doimo mashq qildim",
    "Soyada ko'tarilish", "O'zga dunyoga yolg'iz hujum", "Omadsizning qayta tug'ilishi",
    "Suv sehrgari", "Sirlar hukmdori", "Sinfsiz qahramon", "Yangi darvoza",
    "Naruto", "Muz qilich sehrgari", "Arra odam",
    "Davolash sehridan foydalanishning noto'g'ri usuli", "Shokolad kupidon",
    "Akashic Records: Eng yomon sehr o'qituvchisi", "Oxiridan keyingi boshlanish",
    "Eng kuchli sehrgar",
    "G'ayritabiiy Holat muvaffaqiyatsizi",  # to'liq: "Men «G'ayritabiiy Holat» muvaffaqiyatsiz mahorati bilan eng kuchli bo'lib, hamma narsani yo'q qilaman"
    "Kaiju No.8", "Trinity: Yetti sehrgar", "Brilliant davolovchining soyadagi yangi hayoti",
    "Nega hamma bu dunyoni unutdi",
    "S darajali yirtqich hayvon uy hayvoni",  # to'liq: "O'zga dunyoda S darajali yirtqich hayvonman..."
    "Davolovchi qahramon", "Yashirin sevgi",
    "A darajali guruhdan zindon tubiga",  # to'liq: "A darajali guruhdan chiqib sobiq o'quvchilarim bilan zindon tubiga kirdim"
    "Ochko'z Berserk", "Cheksizlik qasoskori",  # to'liq: "Zindon tubida safdoshlarim manga xiyonat qildi..."
    "Taqdir: G'alati soxtalik", "DMC", "Jodugarlar jangi", "O'lim tog'ida o'lim o'yini",
    "Yuqori maktab hukmdori", "Gachiakuta", "Tayoq va qilich", "Harobalar qirolligi",
    "Guruhdagi yoqimtoy qiz",  # to'liq: "Qahramon Guruhida Yoqimtoy Qiz Bor Edi..."
    "Men gallaktikalar aro imperiyaning yovuz lordiman",
    "Mening qotillik darajam qahramonnikidan oshib ketdi",
    "Sehr yaratuvchisi o'zga dunyoda", "Yolg'iz qahramon: ming hunar egasi",
    "Yengilmas Ossan sarguzashtchi",  # to'liq: "Eng qudratli partiya tomonidan o'limgacha tarbiyalangan Ossan..."
    "Salom dunyo", "Talonchi", "Jodugar va Maxluq", "Sehirgarlar atelyesi",
    "Kill Ao", "Vahshilar Malikasi", "Baholovchi ekan aslida",  # to'liq: "Ma'lum bo'lishicha, eng qudratli qahramon..."
    "Qora chaqiruvchi", "Sinfdagi ikkinchi eng chiroyli qiz bilan do'stlashdim",
    "Zulmat farzandi", "Tokyo qasoskorlari", "Iblislar qotili", "Tokyo guli",
    "Ko'k zindon", "Shilliq bo'lib qayta tug'ulganligim haqida",

    # --- mashhur qo'shimchalar (100 taga to'ldirish uchun) ---
    "Attack on Titan", "One Piece", "Bleach", "Death Note", "My Hero Academia",
    "Hunter x Hunter", "One Punch Man", "Fullmetal Alchemist", "Berserk",
    "JoJo's Bizarre Adventure", "Cowboy Bebop", "Fairy Tail", "Black Clover",
    "Haikyuu!!", "Mob Psycho 100", "Vinland Saga", "Re:Zero", "Overlord",
    "Konosuba", "Violet Evergarden", "Parasyte", "Assassination Classroom",
    "Seven Deadly Sins", "Dr. Stone", "Promised Neverland", "Noragami",
    "Kaguya-sama", "Made in Abyss", "Hellsing",
]
assert len(set(WORLDS)) == len(WORLDS) == 100, f"100 ta noyob dunyo kerak, hozir: {len(WORLDS)}"


def search_worlds(query: str, limit: int = 8) -> list[str]:
    q = query.strip().lower()
    if not q:
        return WORLDS[:limit]
    starts = [g for g in WORLDS if g.lower().startswith(q)]
    contains = [g for g in WORLDS if q in g.lower() and g not in starts]
    return (starts + contains)[:limit]


# ----------------------------------------------------------------------
# LORE (dunyo tavsifi + yovuz jamoa nomi)
# ----------------------------------------------------------------------
LORE = {
    "Naruto": {"world": "Yashirin Qishloqlar Olami", "villain_team": "Akatsuki",
               "intro": "Tun cho'kdi — Konoha ko'chalarida Akatsuki soyalari yashiringan, qishloq ahli orasidan qurbon tanlamoqda..."},
    "One Piece": {"world": "Grand Line Kemasi", "villain_team": "Yashirin Dengiz Qaroqchilari",
                  "intro": "Kema tunda suzmoqda, ammo ekipaj orasida yashirin qaroqchilar bor — ular ertaga birontasini dengizga uloqtiradi..."},
    "Death Note": {"world": "Soya Daftari Shahri", "villain_team": "Kira izdoshlari",
                   "intro": "Kimdir Daftarga ism yozmoqda... Tun tushishi bilan yana bir ism o'chadi."},
    "Attack on Titan": {"world": "Devorlar Ichidagi Shahar", "villain_team": "Titanlarga Xizmat Qiluvchilar",
                        "intro": "Devor ortida xavf kutmoqda, lekin haqiqiy dushman — o'z orangizda yashiringan xoin."},
    "Solo Leveling": {"world": "Zindonlar Tizimi Olami", "villain_team": "Zaif Ovchilar Ittifoqi ichidagi xoinlar",
                      "intro": "Zindon darvozasi yopilgach, ovchilar orasidan kimdir boshqalarni yo'q qilish uchun soyada kutmoqda..."},
    "Arra odam": {"world": "Shaytonlar Olami", "villain_team": "Yashirin Shayton Egalari",
                  "intro": "Tun tushdi — shahar ko'chalarida shayton egalari yashiringan, ov boshlanmoqda..."},
    "Jodugarlar jangi": {"world": "La'nat Ruhlari Olami", "villain_team": "La'nat Ruhlariga Sig'inuvchilar",
                         "intro": "La'nat energiyasi kuchaymoqda — jamoa ichida kimdir allaqachon qoraygan..."},
    "Tokyo qasoskorlari": {"world": "Motorli To'da Olami", "villain_team": "Xoin To'da A'zolari",
                           "intro": "To'da yig'ilishi boshlandi, ammo safda xoinlar bor — ular ertaga birovni yo'q qiladi..."},
    "Iblislar qotili": {"world": "Meiji Davri Yaponiyasi", "villain_team": "Iblislar Qoni Izdoshlari",
                       "intro": "Tun bo'yi iblislar ov qilmoqda — qishloq ahli orasida allaqachon biri o'zgargan..."},
    "Tokyo guli": {"world": "Tokio Ko'k Tun Olami", "villain_team": "Yashirin Gullar (Ghoullar)",
                  "intro": "Ko'chada kimdir haqiqiy odam emas — Gullar orasingizda yashirinib, tunda ov qilmoqda..."},
    "Ko'k zindon": {"world": "Blue Lock Akademiyasi", "villain_team": "Raqib Strategiya Guruhi",
                   "intro": "Akademiyada faqat bitta g'olib qoladi — sherigingiz sizni chiqarib yuborish uchun tayyor..."},
    "Shilliq bo'lib qayta tug'ulganligim haqida": {"world": "Tempest Olami", "villain_team": "Yashirin Imperiya Josuslari",
                                                    "intro": "Tempest tinch uxlayotgan tunda, imperiya josuslari orangizga kirib olgan..."},
    "Kaiju No.8": {"world": "Mudofaa Korpusi Bazasi", "villain_team": "Yashirin Kaiju Egalari",
                  "intro": "Baza ichida kimdir aslida kayju — tun tushishi bilan haqiqiy qiyofasi oshkor bo'ladi..."},
    "Berserk": {"world": "Qorong'u O'rta Asr Qit'asi", "villain_team": "Qo'l Belgisi Egalari",
               "intro": "Kusun'i tuni yaqinlashmoqda — otryad ichida allaqachon qurbonlik uchun belgilangan xoin bor..."},
    "JoJo's Bizarre Adventure": {"world": "Joestar Xonadoni Olami", "villain_team": "Stend Egasi Dushmanlar",
                                 "intro": "G'ayrioddiy kuchlar (Stendlar) uyg'onmoqda — jamoa ichida kimning Stendi zaharli ekanini bilib bo'lmaydi..."},
}


def _hash_pick(pool: list[str], world: str, salt: str = "") -> str:
    idx = abs(hash(world + salt)) % len(pool)
    return pool[idx]


_GENERIC_LEADER_WORDS = ["Soyabon", "Qorao'y Sardor", "Zulmat Boshlig'i", "Xufyona Sarkarda",
                          "Ko'lanka Hukmdori", "Yashirin Lord", "Qora Niqob", "Tun Sultoni"]
_GENERIC_ASSIST_WORDS = ["Soya Xodimi", "Maxfiy Kuryer", "Qora Qanot", "Sirli Hamkor",
                          "Zulmat Shogirdi", "Ko'lanka Ittifoqchisi"]
_GENERIC_DETECTIVE_WORDS = ["Bosh Tergovchi", "Sirlar Ustasi", "Haqiqat Ovchisi",
                             "Kuzatuvchi Ko'z", "Mantiq Ustasi", "Sinchkov Tekshiruvchi"]
_GENERIC_HEALER_WORDS = ["Bosh Shifokor", "Hayot Bag'ishlovchi", "Muqaddas Tabib",
                          "Davo Ustasi", "Najotkor Qo'l"]
_GENERIC_CIVILIAN_WORDS = ["Oddiy Aholi", "Dunyo Fuqarosi", "Mahalliy Yashovchi", "Diyor Farzandi"]


def get_role_labels(world: str) -> dict:
    """
    Har bir dunyo uchun ROL NOMLARINI qaytaradi — mashhur dunyolar uchun
    lore'ga mos maxsus nomlar, qolganlari uchun dunyo nomiga qarab
    FARQLANADIGAN (lekin barqaror) generik nomlar. Shu bilan "bitta nom
    bilan qolib ketish" muammosi hal qilinadi.
    """
    curated = {
        "Naruto": {"oyabun": "Akatsuki Yetakchisi", "kage": "Akatsuki A'zosi",
                   "meitantei": "Konoha Jasusi", "iyashi": "Klan Tabibi", "nakama": "Qishloq Shinobisi"},
        "One Piece": {"oyabun": "Qaroqchilar Kapitani", "kage": "Ekipaj Xoini",
                      "meitantei": "Dengiz Fuqarolari Kotibi", "iyashi": "Kema Shifokori", "nakama": "Ekipaj A'zosi"},
        "Death Note": {"oyabun": "Kira", "kage": "Kira Izdoshi",
                       "meitantei": "L Klassi Tergovchi", "iyashi": "Shinigami Homiysi", "nakama": "Fuqaro"},
        "Attack on Titan": {"oyabun": "Titan Boshlig'i", "kage": "Titan Xizmatkori",
                            "meitantei": "Razvedka Otryadi Detektivi", "iyashi": "Qo'shin Shifokori", "nakama": "Devor Fuqarosi"},
        "Solo Leveling": {"oyabun": "Zulmat Monarxi", "kage": "Soya Askari",
                          "meitantei": "S-Darajali Ovchi", "iyashi": "Qo'llab-quvvatlovchi Ovchi", "nakama": "Oddiy Ovchi"},
        "Arra odam": {"oyabun": "Shayton Egasi", "kage": "Shayton Xodimi",
                      "meitantei": "Xavfsizlik Bo'limi Nazoratchisi", "iyashi": "Bo'lim Shifokori", "nakama": "Ov Bo'limi A'zosi"},
        "Jodugarlar jangi": {"oyabun": "La'nat Ruhi Boshlig'i", "kage": "La'nat Ruhi Xizmatkori",
                             "meitantei": "Jodu Maktabi Ustozi", "iyashi": "Energiya Davolovchisi", "nakama": "Jodu Maktabi O'quvchisi"},
        "Tokyo qasoskorlari": {"oyabun": "To'da Boshlig'i", "kage": "To'da Xoini",
                               "meitantei": "Sobiq A'zo Tergovchi", "iyashi": "To'da Shifokori", "nakama": "To'da A'zosi"},
        "Iblislar qotili": {"oyabun": "Iblislar Boshlig'i", "kage": "Yosh Iblis",
                            "meitantei": "Iblis Qotillari Ustozi", "iyashi": "Nafas Uslubi Shifokori", "nakama": "Qishloq Aholisi"},
        "Tokyo guli": {"oyabun": "Gul Boshlig'i", "kage": "Yashirin Gul",
                       "meitantei": "CCG Tergovchisi", "iyashi": "Qahvaxona Shifokori", "nakama": "Tinch Fuqaro"},
        "Ko'k zindon": {"oyabun": "Strategiya Boshlig'i", "kage": "Raqib Josus",
                        "meitantei": "Bosh Murabbiy", "iyashi": "Jismoniy Tayyorgarlik Shifokori", "nakama": "Akademiya O'quvchisi"},
        "Shilliq bo'lib qayta tug'ulganligim haqida": {"oyabun": "Yashirin Imperator", "kage": "Imperiya Josusi",
                                                        "meitantei": "Tempest Maslahatchisi", "iyashi": "Tabiat Shifokori", "nakama": "Tempest Fuqarosi"},
        "Kaiju No.8": {"oyabun": "Yashirin Kaiju", "kage": "Kaiju Xodimi",
                       "meitantei": "Mudofaa Korpusi Kapitani", "iyashi": "Baza Shifokori", "nakama": "Korpus Askari"},
        "Berserk": {"oyabun": "Qo'l Belgisi Egasi", "kage": "Qorong'u Ritsar",
                    "meitantei": "Sayyor Qilichbozi", "iyashi": "Sehrgar Shifokor", "nakama": "Otryad A'zosi"},
        "JoJo's Bizarre Adventure": {"oyabun": "Stend Foydalanuvchi Xoin", "kage": "Yashirin Stend Egasi",
                                     "meitantei": "Joestar Vorisi", "iyashi": "Hamayo Shifokori", "nakama": "Oddiy Fuqaro"},
    }
    if world in curated:
        return curated[world]
    return {
        "oyabun": _hash_pick(_GENERIC_LEADER_WORDS, world, "oyabun"),
        "kage": _hash_pick(_GENERIC_ASSIST_WORDS, world, "kage"),
        "meitantei": _hash_pick(_GENERIC_DETECTIVE_WORDS, world, "meitantei"),
        "iyashi": _hash_pick(_GENERIC_HEALER_WORDS, world, "iyashi"),
        "nakama": _hash_pick(_GENERIC_CIVILIAN_WORDS, world, "nakama"),
    }


def _build_generic_lore(name: str) -> dict:
    templates = [
        "{name} olamida tungi sukunat cho'kishi bilanoq, yashirin dushman kuchlari orasingizdan birini tanlaydi.",
        "{name} dunyosida ishonch — eng qimmatli va eng xavfli qurol. Kim xoin, kim sodiq — faqat kunduz oshkor bo'ladi.",
        "{name} sarguzashti davom etmoqda, ammo bu safar jang maydoni sizning o'z jamoangiz ichida.",
    ]
    return {
        "world": f"{name} Olami",
        "villain_team": f"{name} Soya Klani",
        "intro": templates[abs(hash(name)) % len(templates)].format(name=name),
    }


def get_lore(world: str) -> dict:
    if world in LORE:
        return LORE[world]
    return _build_generic_lore(world)


# ----------------------------------------------------------------------
# ALOHIDA ISM RO'YXATLARI — 20 ta mashhur dunyo uchun HAQIQIY personajlar
# ----------------------------------------------------------------------
CHARACTER_NAMES = {
    "Naruto": ["Naruto", "Sasuke", "Sakura", "Kakashi", "Itachi", "Gaara", "Hinata", "Shikamaru",
               "Jiraiya", "Tsunade", "Orochimaru", "Rock Lee", "Neji", "Ino", "Choji", "Kiba",
               "Shino", "Temari", "Kankuro", "Konohamaru"],
    "One Piece": ["Luffy", "Zoro", "Nami", "Usopp", "Sanji", "Chopper", "Robin", "Franky",
                  "Brook", "Jinbe", "Ace", "Sabo", "Shanks", "Law", "Buggy", "Boa Hancock",
                  "Smoker", "Kaido", "Big Mom", "Doflamingo"],
    "Bleach": ["Ichigo", "Rukia", "Renji", "Orihime", "Uryu", "Chad", "Byakuya", "Toshiro",
               "Kenpachi", "Yoruichi", "Urahara", "Aizen", "Grimmjow", "Ulquiorra", "Nel",
               "Shunsui", "Rangiku", "Ikkaku", "Yumichika", "Kisuke"],
    "Death Note": ["L", "Light", "Misa", "Ryuk", "Near", "Mello", "Soichiro", "Matsuda",
                   "Watari", "Rem", "Naomi", "Sayu", "Aizawa", "Mogi", "Ide", "Shiori",
                   "Takada", "Higuchi", "Ukita", "Matt"],
    "Attack on Titan": ["Eren", "Mikasa", "Armin", "Levi", "Erwin", "Historia", "Jean", "Sasha",
                        "Connie", "Reiner", "Bertholdt", "Annie", "Ymir", "Hange", "Zeke",
                        "Gabi", "Falco", "Pieck", "Marco", "Krista"],
    "My Hero Academia": ["Deku", "Bakugo", "Todoroki", "Ochaco", "Iida", "Tsuyu", "Kirishima",
                         "Denki", "Momo", "Tokoyami", "Mineta", "Ojiro", "Aizawa", "All Might",
                         "Endeavor", "Present Mic", "Midnight", "Toga", "Shigaraki", "Dabi"],
    "Hunter x Hunter": ["Gon", "Killua", "Kurapika", "Leorio", "Hisoka", "Chrollo", "Illumi",
                        "Netero", "Meruem", "Neferpitou", "Kite", "Ging", "Biscuit", "Knuckle",
                        "Shoot", "Shalnark", "Machi", "Feitan", "Phinks", "Nobunaga"],
    "One Punch Man": ["Saitama", "Genos", "Mumen Rider", "Bang", "King", "Tatsumaki", "Fubuki",
                      "Sonic", "Garou", "Boros", "Amai Mask", "Puri-Puri Prisoner", "Metal Knight",
                      "Atomic Samurai", "Child Emperor", "Zombieman", "Watchdog Man",
                      "Superalloy Darkshine", "Silver Fang", "Speed-o'-Sound Sonic"],
    "Fullmetal Alchemist": ["Edward", "Alphonse", "Winry", "Roy Mustang", "Riza Hawkeye",
                            "Alex Armstrong", "Scar", "Izumi", "Maes Hughes", "King Bradley",
                            "Envy", "Lust", "Gluttony", "Greed", "Wrath", "Sloth", "Pride",
                            "Ling Yao", "May Chang", "Olivier Armstrong"],
    "Solo Leveling": ["Sung Jin-Woo", "Cha Hae-In", "Go Gun-Hee", "Baek Yoonho", "Yoo Jinho",
                      "Choi Jong-In", "Woo Jin-Chul", "Thomas Andre", "Liu Zhigang",
                      "Christopher Reed", "Beru", "Igris", "Tank", "Bellion", "Tusk",
                      "Kang Taeshik", "Lim Tae-Gyu", "Han Song-Yi", "Sung Il-Hwan", "Sung Jin-Ah"],
    "Arra odam": ["Denji", "Power", "Aki", "Makima", "Himeno", "Kobeni", "Arai", "Angel Devil",
                  "Quanxi", "Reze", "Kishibe", "Katana Man", "Sawatari", "Kurose", "Nayuta",
                  "Asa Mitaka", "Yoru", "Fami", "Yoshida", "Barem"],
    "Jodugarlar jangi": ["Yuji", "Megumi", "Nobara", "Gojo", "Nanami", "Maki", "Toge", "Panda",
                         "Todo", "Yuta", "Sukuna", "Mahito", "Jogo", "Hanami", "Nue", "Kenjaku",
                         "Yuki Tsukumo", "Choso", "Miwa", "Ijichi"],
    "Tokyo qasoskorlari": ["Takemichi", "Hinata", "Chifuyu", "Mikey", "Draken", "Baji", "Mitsuya",
                           "Pah-chin", "Peh-yan", "Kazutora", "Hakkai", "Kokonoi", "Inui", "Akkun",
                           "Smiley", "Angry", "Shinichiro", "Emma", "Izana", "Kisaki"],
    "Iblislar qotili": ["Tanjiro", "Nezuko", "Zenitsu", "Inosuke", "Giyu", "Shinobu", "Kanao",
                        "Mitsuri", "Tengen", "Muichiro", "Gyomei", "Sanemi", "Obanai", "Kagaya",
                        "Akaza", "Doma", "Muzan", "Rui", "Daki", "Kokushibo"],
    "Tokyo guli": ["Kaneki", "Touka", "Hide", "Rize", "Yoshimura", "Nishiki", "Kimi", "Hinami",
                   "Amon", "Juuzou", "Arima", "Tsukiyama", "Uta", "Ayato", "Eto", "Akira",
                   "Shuu", "Kuki Urie", "Saiko", "Mutsuki"],
    "Ko'k zindon": ["Isagi", "Bachira", "Rin", "Chigiri", "Kunigami", "Barou", "Nagi", "Reo",
                    "Kurona", "Niko", "Aryu", "Otoya", "Gagamaru", "Shidou", "Yukimiya",
                    "Naruhaya", "Jinpachi", "Sae", "Karasu", "Raichi"],
    "Shilliq bo'lib qayta tug'ulganligim haqida": ["Rimuru", "Benimaru", "Shion", "Souei", "Shuna",
                                                     "Hakurou", "Gobta", "Ranga", "Diablo", "Milim",
                                                     "Veldora", "Rigurd", "Gabiru", "Geld", "Souka",
                                                     "Testarossa", "Ultima", "Carrera", "Ramiris", "Chloe"],
    "Kaiju No.8": ["Kafka", "Reno", "Mina", "Kikoru", "Iharu", "Shinomiya", "Ashiro", "Aoi",
                   "Hoshina", "Isao", "Narumi", "Kotaro", "Gen", "Haruichi", "Konomi",
                   "Kyu Yoshikane", "Yamamoto", "Tsuji", "Kudalia", "Sagaru"],
    "Berserk": ["Guts", "Griffith", "Casca", "Judeau", "Pippin", "Corkus", "Rickert", "Zodd",
                "Void", "Slan", "Ubik", "Conrad", "Farnese", "Serpico", "Isidro", "Schierke",
                "Puck", "Roderick", "Mule", "Charlotte"],
    "JoJo's Bizarre Adventure": ["Jonathan", "Joseph", "Jotaro", "Josuke", "Giorno", "Jolyne",
                                 "Johnny", "Dio", "Polnareff", "Avdol", "Kakyoin", "Iggy",
                                 "Rohan", "Koichi", "Okuyasu", "Yukako", "Bruno", "Mista",
                                 "Trish", "Gyro"],
}

# Kuratsiya qilinmagan dunyolar uchun generik, lekin dunyodan-dunyoga
# FARQ QILADIGAN (bir xil bo'lib qolmaydigan) ism to'plami
_GENERIC_NAME_POOL = [
    "Aki", "Hiro", "Ren", "Sora", "Yuki", "Kaze", "Rin", "Shin", "Mio", "Kuro",
    "Sen", "Nao", "Tsumugi", "Haru", "Yuma", "Kanade", "Riko", "Souta", "Airi", "Ryoma",
    "Fuyuki", "Nozomi", "Takeshi", "Kotone", "Yamato", "Aoi", "Isamu", "Chihiro", "Daiki", "Emi",
    "Fumiko", "Goro", "Hana", "Ichika", "Jun", "Kaori", "Rami", "Mai", "Natsu", "Osamu",
    "Reika", "Saki", "Tatsu", "Umi", "Wataru", "Yui", "Zen", "Akane", "Botan", "Chika",
]


def get_resident_pool(world: str) -> list[str]:
    """Berilgan dunyo uchun 20 ta o'yin-ichi aholi ismini qaytaradi."""
    if world in CHARACTER_NAMES:
        return CHARACTER_NAMES[world]
    pool = _GENERIC_NAME_POOL.copy()
    rnd = random.Random(hash(world))  # dunyo bo'yicha barqaror, lekin dunyodan-dunyoga farqli tartib
    rnd.shuffle(pool)
    return pool[:20]
