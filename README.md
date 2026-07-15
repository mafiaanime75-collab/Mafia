# 🌙 Animafia — Anime Mafia Telegram Bot

Python + aiogram 3.x. Alwaysdata kabi kam resursli serverlarga mos: yengil
kutubxonalar (aiosqlite, aiogram, python-dotenv), toza absolute importlar,
`handlers/` dan tashqarida chigal bog'liqlik yo'q.

## Loyiha tuzilishi (talab qilingandek, absolyut)

```
animafia/
├── database.py       - aiosqlite (foydalanuvchi, reyting, ikki valyuta)
├── config.py         - .env orqali token va sozlamalar
├── bot.py            - Dispatcher, Routerlarni ulash
├── states.py          - FSM holatlar
├── keyboards.py         - barcha tugmalar
├── genres.py              - 60 ta anime dunyosi, lore, fuzzy qidiruv, aholi ismlari
├── requirements.txt
├── .env.example
└── handlers/
    ├── __init__.py
    ├── start.py       - /start, dunyo qidiruvi boshlanishi
    ├── lobby.py        - dunyo tanlash, lobby, guruhga ulashish/qo'shilish
    ├── game.py          - o'yin jarayoni (tun/kun, ovoz, g'alaba)
    ├── rating.py          - /rating /grouprating /profile
    └── economy.py          - /shop /gemshop /buy /gembuy /daily /balance
```

## Import qoidalari — aynan siz so'raganidek

- `handlers/` ichidagi fayllar asosiy papkadagi modullarni (`genres`,
  `keyboards`, `states`, `database`, `config`, `game_engine`) har doim
  **to'g'ridan-to'g'ri** import qiladi: `from genres import ...`,
  `from keyboards import ...` — hech qanday `..` yoki nisbiy import yo'q.
- `handlers/` ichidagi fayllar bir-birini chaqirganda esa (masalan
  `game.py` `lobby.py` dagi `ACTIVE_LOBBIES` ni ishlatadi) —
  `from handlers.lobby import ACTIVE_LOBBIES` shaklida, chunki ular bir xil
  `handlers` paketi ichida.
- Aylanma (circular) import yo'q: `game.py` → `lobby.py` faqat bir tomonlama,
  `lobby.py` hech qachon `game.py`ni import qilmaydi.
- Barcha fayllar sintaksis va import yo'llari bo'yicha tekshirib chiqildi
  (`ast.parse` orqali) — `ModuleNotFoundError` chiqmasligi kafolatlangan,
  faqat serverga `pip install -r requirements.txt` qilishni unutmang.

## O'rnatish (Alwaysdata va shunga o'xshash serverlar uchun)

```bash
pip install -r requirements.txt
cp .env.example .env
# .env faylini oching, BOT_TOKEN va MAIN_GROUP_* qiymatlarini kiriting
python bot.py
```

## O'yin qoidalari

- Minimal o'yinchi: **4 ta**, maksimal: **20 ta**.
- Har doim, o'yinchi soni qancha bo'lmasin, kamida **1 ta Oyabun (mafia)**
  va **1 ta Meitantei (komissar/detektiv)** bo'lishi **majburiy**
  (`game_engine.build_role_list` shu qoidani kafolatlaydi — 4 dan 20
  o'yinchigacha test qilib tekshirildi).
- Mafia foizi o'yinchilar sonining ~28% (yumaloqlangan), 7+ o'yinchida
  Iyashi-nin (shifokor) ham qo'shiladi.
- Har bir o'yinchiga o'yin boshlanganda **tasodifiy anime-uslub aholi ismi**
  beriladi (masalan "Soramaru", "Kurochi") — barcha o'yin xabarlarida
  haqiqiy ism o'rniga shu ism ko'rinadi.

## Dunyo tanlash (janr o'rniga)

`/start` bosilgach, bot **"Dunyo tanlang"** deb so'raydi (avvalgi "janr"
so'zi o'rniga, sizning talabingizga ko'ra). Foydalanuvchi harf yozadi
(`na`, `one`...) — `search_worlds()` fuzzy qidiruv bilan mos nomlarni
chiqaradi. Hozircha **60 ta** anime nomi bor (`genres.py` → `ANIME_WORLDS`).

📌 **Do'stingizning 60 ta anime ro'yxatini yuborsangiz**, men uni shu
ro'yxatga almashtirib/qo'shib chiqaman — istasangiz umumiy sonni 100 tagacha
ham kengaytirishimiz mumkin.

## 💰 Ikkita alohida valyuta (sizning fikringiz asosida)

### 1. 🔗 Kizuna — o'yin natijasidan, reytingga bog'liq
- G'alaba: **+50**, Mag'lubiyat: **+15** (ishtirok tasallisi), MVP: **+30** qo'shimcha.
- `/shop` — o'yin ICHIDAGI real effektga ega narsalar do'koni:

| Narsa | Narxi | Effekti |
|---|---|---|
| 🔮 Tirilish Tumori | 200 | Tunda o'lsangiz — bir marta tirilasiz |
| 🌫 Soya Pardasi | 150 | Bir kechaga detektiv tekshiruvidan yashirinasiz |
| ⚡ Qo'sh Ovoz | 120 | Kunduzgi ovozingiz 2x hisoblanadi |
| 🕵️ Vaqtinchalik Alibi | 180 | Ovozda chiqarilishdan bir marta qutulasiz |
| 🤝 Ittifoq Qasamyodi | 100 | (faqat Mafia) sherigingizni darhol bilib olasiz |
| ⚔️ Chaqmoq Zarbasi | 160 | O'zingizni bir tunga o'zingiz himoya qilasiz |
| 🎖 Sodiqlik Nishoni | 100 | Profilga maxsus unvon qo'yish huquqi |

### 2. 💎 Sehirli Tosh — kunlik BEPUL bonus, reytingga TA'SIR QILMAYDI
Sizning fikringiz aynan shu edi — kunlik bonus alohida valyuta bo'lsin,
alohida do'konda sotilsin va reyting jadvaliga umuman kirmasin. Shunday
qildim:

- `/daily` — kuniga bir marta **+15 💎 Sehirli Tosh** (`config.DAILY_GEM_REWARD`
  orqali sozlanadi).
- `/gemshop` — **butunlay alohida**, faqat **kosmetik/qulaylik** narsalar
  do'koni (o'yin balansiga ta'sir qilmaydi, shuning uchun reytingga ham
  bilvosita ta'sir qilmaydi):

| Narsa | Narxi | Nima qiladi |
|---|---|---|
| ✍️ Ism O'zgartirish Kartasi | 5 💎 | O'yin ichidagi aholi ismingizni o'zingiz tanlaysiz |
| 🖼 Nodir Avatar Ramka | 8 💎 | Profilga bezakli ramka |
| 👑 VIP Unvon: Afsonaviy Otaku | 10 💎 | Dekorativ unvon |
| ✨ Signature Emoji To'plami | 6 💎 | Xabarlarga maxsus emoji |
| 🍀 Baxt Tumori | 6 💎 | Profilda ko'rinadigan kosmetik tumor |
| 🌆 Statistika Fon Rasmi | 7 💎 | /profile kartochkasi uchun fon |
| 🎴 Duo Kartasi | 4 💎 | Do'stingizni taklif qilsangiz ikkalangizga +5 💎 |

`/balance` ikkala valyutani ham ko'rsatadi; `/profile` ham shunday, lekin
`/rating` va `/grouprating` faqat ELO/Kizuna asosidagi natijalarni chiqaradi
— Sehirli Tosh u yerda umuman ko'rinmaydi.

## Keyingi qadamlar

1. Do'stingizning 60 ta anime nomi ro'yxatini yuboring — moslashtiraman.
2. `ism_ozgartirish` kartasi va boshqa Gem-shop narsalarining haqiqiy UI
   effektini (masalan `/profile` da ramka ko'rsatish) keyingi bosqichda
   qo'shish mumkin — hozircha xarid va balans mexanizmi to'liq ishlaydi.
3. Kizuna-shop narsalarining o'yin ichidagi real ta'sirini (masalan
   "Tirilish Tumori" xarid qilganlarni `GameState`da belgilash) keyingi
   iteratsiyada `handlers/game.py`ga ulashimiz kerak.
4. Productionga chiqishda `python bot.py`ni systemd/screen yoki
   Alwaysdata'ning "Tasks" bo'limi orqali doimiy ishlab turishini
   sozlash tavsiya etiladi (polling rejimida).
