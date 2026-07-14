# 🌙 Anime Mafia: Kizuna no Yoru

Anime-uslubidagi Mafia (Werewolf) o'yin boti — Python + aiogram 3.

## O'rnatish

```bash
pip install -r requirements.txt
```

`config.py` faylida:
- `BOT_TOKEN` — @BotFather'dan olingan tokeningiz
- `MAIN_GROUP_ID` va `MAIN_GROUP_INVITE_LINK` — asosiy o'yin guruhingiz

Botni ishga tushirish:
```bash
python bot.py
```

## Loyiha tuzilishi

```
config.py            - sozlamalar (token, guruh, o'yin vaqtlari)
database.py           - SQLite (foydalanuvchi, reyting, valyuta, sessiya)
game_engine.py         - rollar, tun/kun mantiqi, g'olibni aniqlash
keyboards.py            - barcha inline tugmalar
states.py                - FSM holatlar (janr qidiruvi uchun)
data/genres.py            - 100 ta anime nomi + fuzzy qidiruv + lore generator
handlers/start.py          - /start va janr qidiruv boshlanishi
handlers/lobby.py            - janr tanlash, lobby ochish, guruhga ulashish/qo'shilish
handlers/game.py               - o'yin davri: tun/kun, ovoz berish, g'alaba
handlers/rating.py               - /rating /grouprating /profile
handlers/economy.py                - /shop /balance /buy — Kizuna valyutasi
```

## Rollar (universal, har qanday tanlangan animega moslashadi)

| Rol | Klassik mos kelishi | Vazifasi |
|---|---|---|
| 🐍 Oyabun | Don/Boss | Mafia yetakchisi, tunda o'ldiradi |
| 🗡 Kage | Mafia a'zosi | Oyabun bilan birga o'ldiradi |
| 🔍 Meitantei | Komissar/Detektiv | Tunda birini tekshiradi (mafiami-yo'qmi) |
| 💊 Iyashi-nin | Shifokor | Tunda birini himoya qiladi |
| 👤 Nakama | Tinch aholi | Kunduzi ovoz beradi |

G'alaba shartlari klassik Mafiaga to'liq mos: mafia soni tinch aholiga
teng/ko'p bo'lsa — mafia yutadi; barcha mafia yo'q qilinsa — tinch aholi yutadi.

## Janr tanlash (fuzzy qidiruv)

`data/genres.py` da 100 ta anime nomi bor. Foydalanuvchi harflar yozganda
(`na`, `one`, `dr` va h.k.) `search_genres()` mos nomlarni chiqaradi —
avval nom boshidan mos kelganlar, keyin ichida uchraydiganlar. Har bir
janr uchun `get_lore()` orqali o'yin tasviri (dunyo nomi, yovuz jamoa nomi,
kirish matni) chiqadi — bir nechta mashhur anime uchun qo'lda yozilgan
noyob matn bor (`ANIME_LORE`), qolganlari uchun avtomatik moslashtirilgan
matn generatsiya qilinadi. Xohlagancha ko'proq janrga qo'lda noyob matn
qo'shishingiz mumkin — tuzilma bir xil qoladi.

## Lobby va guruhga ulash (rasmdagi kabi)

Lobby ochilgach ikkita asosiy tugma chiqadi:
- **📤 Guruhga ulashish** — `switch_inline_query` orqali ishlaydi: bosilganda
  Telegram O'ZI "Chatni tanlang" ekranini ochadi (aynan siz yuborgan
  skrinshotdagidek), foydalanuvchi guruhni tanlaydi, taklifnoma o'sha yerga
  yuboriladi.
- **👥 Asosiy guruhga qo'shilish** — to'g'ridan-to'g'ri asosiy o'yin guruhi
  linkiga olib boradi.

Bundan tashqari **🎮 Lobbyga qo'shilish** va **▶️ Boshlash** tugmalari bor.

## Reyting tizimi

- **Global reyting** (`/rating`) — butun bot bo'yicha ELO asosida.
- **Guruh reytingi** (`/grouprating`) — har bir guruh o'z alohida jadvaliga
  ega (`group_ratings` jadvali), shu guruhdagi o'yinlar asosida hisoblanadi.

ELO g'alabada +20, mag'lubiyatda -10 (`compute_elo_delta`) — xohlasangiz
`game_engine.py` da moslashtirishingiz mumkin.

## Bot valyutasi — "Kizuna" 🔗

*Kizuna* (絆) — yaponcha "bog'liqlik/ahd" degani, deyarli barcha anime
janrlarida (do'stlik, sodiqlik, jamoa ruhi) uchraydigan universal tushuncha
— shu sabab qaysi anime tanlansa ham mos keladi.

**Ishlab topish:** g'alaba +50, mag'lubiyat +15 (ishtirok mukofoti), MVP +30.

**Do'kon (`/shop`, `/buy <item>`):**
| Narsa | Narxi | Effekti |
|---|---|---|
| 🔮 Tirilish Tumori | 200 | Tunda o'lsangiz — bir marta tirilasiz |
| 🌫 Soya Pardasi | 150 | Bir kechaga detektiv tekshiruvidan yashirinasiz |
| 🎖 Sodiqlik Nishoni | 100 | Profilga maxsus unvon qo'yish huquqi |
| ⚡ Qo'sh Ovoz | 120 | Kunduzgi ovozingiz 2x hisoblanadi |

Bu — boshlang'ich versiya, keyinroq buyumlarning o'yin ichida haqiqiy
effektini (`game_engine.py` ichida) ulash kerak bo'ladi (hozircha xarid
qilish va balans mexanizmi to'liq ishlaydi, effektlarni join qilish esa
keyingi bosqich).

## Keyingi qadamlar (tavsiya)

1. `ANIME_LORE` ga ko'proq janr uchun qo'lda noyob syujet matn qo'shish.
2. Do'kon buyumlarining real effektini `game_engine.py` bilan bog'lash
   (masalan Tirilish Tumori sotib olganlarni GameState da belgilash).
3. Guruh ichida bir nechta parallel lobby bo'lishi mumkinligini hisobga
   olib, `ACTIVE_LOBBIES`/`RUNNING_GAMES` ni guruh+session bo'yicha
   filtrlashni kuchaytirish.
4. Production uchun webhook (polling o'rniga) va Docker konteyner qo'shish.
