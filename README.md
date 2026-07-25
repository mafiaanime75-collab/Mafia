# 🎮 AniMafia Bot

Anime uslubidagi Mafia o'yini Telegram boti!

## 🌟 Xususiyatlar

- 🌸 30+ turli anime olami
- 🎭 Anime personajlari bilan o'ynash
- 🛒 Magazin va valyuta tizimi
- 🏆 Liga va reyting tizimi
- 🎁 Kunlik bonuslar
- 👥 Do'stlar bilan o'ynash

## 🚀 O'rnatish

```bash
pip install -r requirements.txt
```

## ⚙️ Konfiguratsiya

`config.py` fayliga o'zingizning ma'lumotlaringizni yozing:

```python
BOT_TOKEN = "your_bot_token_here"
ADMIN_ID = 123456789
```

## 🎮 Ishga tushirish

```bash
python main.py
```

## 📁 Loyiha tuzilishi

```
animafia_bot/
├── config.py          # Konfiguratsiya
├── database.py        # SQLite ma'lumotlar bazasi
├── keyboards.py       # Tugmalar
├── anime_worlds.py    # Anime olamlari
├── game_roles.py      # Rollar va qoidalar
├── requirements.txt   # Kutubxonalar
├── main.py            # Asosiy fayl
└── handlers/
    ├── start.py       # Start va menyu
    ├── shop.py        # Magazin
    ├── profile.py     # Profil
    ├── league.py      # Liga
    ├── rating.py      # Reyting
    ├── daily_bonus.py # Kunlik bonus
    ├── game.py        # O'yin
    ├── admin.py       # Admin panel
    ├── feedback.py    # Taklif/Shikoyat
    └── rules.py       # Qoidalar
```

## 📝 Litsenziya

MIT
