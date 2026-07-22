
# 2. anime_worlds.py - 30 ta anime olami (to'liq o'zbek tilida)
anime_worlds_content = '''# ============ ANIME OLAMLARI (30 ta) ============
# Har bir anime olamidan mafia rollariga mos keladigan personajlar

ANIME_WORLDS = {
    "Naruto": {
        "icon": "🍥",
        "characters": {
            "tinchlik": {
                "Komissar": "Kakashi Hatake",
                "Sergant": "Iruka Umino",
                "Mer": "Tsunade",
                "Shifokor": "Sakura Haruno",
                "Sevgil": "Ino Yamanaka",
                "Bomj": "Jiraiya",
                "Oddiy fuqaro": "Shikamaru Nara",
                "Omadli": "Naruto Uzumaki",
                "O'z joniga qasqon": "Gaara",
                "Kamikadze": "Choji Akimichi"
            },
            "mafia": {
                "Don": "Madara Uchiha",
                "Mafioz": "Obito Uchiha",
                "Advokat": "Danzo Shimura",
                "Qotil": "Itachi Uchiha",
                "Jurnalist": "Kabuto Yakushi"
            },
            "yolg'iz": {
                "Manyak": "Orochimaru",
                "Aylanuvchi": "Kimimaro",
                "Yondiruvchi": "Hidan",
                "Sehrgar": "Nagato/Pein",
                "Aferist": "Konohamaru",
                "Stukach": "Sai"
            }
        }
    },
    
    "One Piece": {
        "icon": "🏴‍☠️",
        "characters": {
            "tinchlik": {
                "Komissar": "Smoker",
                "Sergant": "Tashigi",
                "Mer": "Koby",
                "Shifokor": "Chopper",
                "Sevgil": "Nami",
                "Bomj": "Rayleigh",
                "Oddiy fuqaro": "Usopp",
                "Omadli": "Luffy",
                "O'z joniga qasqon": "Brook",
                "Kamikadze": "Franky"
            },
            "mafia": {
                "Don": "Marshall D. Teach",
                "Mafioz": "Doflamingo",
                "Advokat": "Crocodile",
                "Qotil": "Rob Lucci",
                "Jurnalist": "Van Augur"
            },
            "yolg'iz": {
                "Manyak": "Kaido",
                "Aylanuvchi": "Marco",
                "Yondiruvchi": "Ace",
                "Sehrgar": "Enel",
                "Aferist": "Buggy",
                "Stukach": "Morgan"
            }
        }
    },
    
    "Attack on Titan": {
        "icon": "⚔️",
        "characters": {
            "tinchlik": {
                "Komissar": "Levi Ackerman",
                "Sergant": "Hange Zoe",
                "Mer": "Erwin Smith",
                "Shifokor": "Eren Yeager",
                "Sevgil": "Mikasa Ackerman",
                "Bomj": "Kenny Ackerman",
                "Oddiy fuqaro": "Armin Arlert",
                "Omadli": "Sasha Braus",
                "O'z joniga qasqon": "Reiner Braun",
                "Kamikadze": "Bertolt Hoover"
            },
            "mafia": {
                "Don": "Zeke Yeager",
                "Mafioz": "Reiner Braun",
                "Advokat": "Pieck Finger",
                "Qotil": "Annie Leonhart",
                "Jurnalist": "Floch"
            },
            "yolg'iz": {
                "Manyak": "Eren Yeager",
                "Aylanuvchi": "Falco",
                "Yondiruvchi": "Bertolt",
                "Sehrgar": "Ymir",
                "Aferist": "Historia",
                "Stukach": "Grisha"
            }
        }
    },
    
    "Demon Slayer": {
        "icon": "🗡️",
        "characters": {
            "tinchlik": {
                "Komissar": "Giyu Tomioka",
                "Sergant": "Shinobu Kocho",
                "Mer": "Kagaya Ubuyashiki",
                "Shifokor": "Shinobu Kocho",
                "Sevgil": "Mitsuri Kanroji",
                "Bomj": "Yoriichi",
                "Oddiy fuqaro": "Zenitsu Agatsuma",
                "Omadli": "Inosuke Hashibira",
                "O'z joniga qasqon": "Kaigaku",
                "Kamikadze": "Gyomei"
            },
            "mafia": {
                "Don": "Muzan Kibutsuji",
                "Mafioz": "Kokushibo",
                "Advokat": "Doma",
                "Qotil": "Akaza",
                "Jurnalist": "Enmu"
            },
            "yolg'iz": {
                "Manyak": "Doma",
                "Aylanuvchi": "Nezuko",
                "Yondiruvchi": "Kyojuro",
                "Sehrgar": "Yoriichi",
                "Aferist": "Tanjiro",
                "Stukach": "Genya"
            }
        }
    },
    
    "Jujutsu Kaisen": {
        "icon": "👁️",
        "characters": {
            "tinchlik": {
                "Komissar": "Kento Nanami",
                "Sergant": "Nobara Kugisaki",
                "Mer": "Yoshinobu Gakuganji",
                "Shifokor": "Shoko Ieiri",
                "Sevgil": "Maki Zenin",
                "Bomj": "Toji Fushiguro",
                "Oddiy fuqaro": "Yuta Okkotsu",
                "Omadli": "Yuji Itadori",
                "O'z joniga qasqon": "Mahito",
                "Kamikadze": "Mei Mei"
            },
            "mafia": {
                "Don": "Sukuna",
                "Mafioz": "Geto",
                "Advokat": "Jogo",
                "Qotil": "Choso",
                "Jurnalist": "Momo"
            },
            "yolg'iz": {
                "Manyak": "Mahito",
                "Aylanuvchi": "Hakari",
                "Yondiruvchi": "Jogo",
                "Sehrgar": "Gojo Satoru",
                "Aferist": "Fushiguro",
                "Stukach": "Miwa"
            }
        }
    },
    
    "My Hero Academia": {
        "icon": "💥",
        "characters": {
            "tinchlik": {
                "Komissar": "Tenya Iida",
                "Sergant": "Ochaco Uraraka",
                "Mer": "Toshinori Yagi",
                "Shifokor": "Rei Garaki",
                "Sevgil": "Momo Yaoyorozu",
                "Bomj": "Knuckleduster",
                "Oddiy fuqaro": "Deku",
                "Omadli": "Mineta",
                "O'z joniga qasqon": "Tomura",
                "Kamikadze": "Bakugo"
            },
            "mafia": {
                "Don": "All For One",
                "Mafioz": "Tomura Shigaraki",
                "Advokat": "Kurogiri",
                "Qotil": "Dabi",
                "Jurnalist": "Spinner"
            },
            "yolg'iz": {
                "Manyak": "Shigaraki",
                "Aylanuvchi": "Himiko",
                "Yondiruvchi": "Dabi",
                "Sehrgar": "Deku",
                "Aferist": "Neito Monoma",
                "Stukach": "La Brava"
            }
        }
    },
    
    "Death Note": {
        "icon": "📓",
        "characters": {
            "tinchlik": {
                "Komissar": "L",
                "Sergant": "Watari",
                "Mer": "Soichiro Yagami",
                "Shifokor": "Misa Amane",
                "Sevgil": "Kiyomi Takada",
                "Bomj": "Raye Penber",
                "Oddiy fuqaro": "Matsuda",
                "Omadli": "Near",
                "O'z joniga qasqon": "Misa",
                "Kamikadze": "Mello"
            },
            "mafia": {
                "Don": "Light Yagami (Kira)",
                "Mafioz": "Mikami",
                "Advokat": "Takada",
                "Qotil": "Ryuk",
                "Jurnalist": "Aizawa"
            },
            "yolg'iz": {
                "Manyak": "Kira",
                "Aylanuvchi": "Rem",
                "Yondiruvchi": "Mello",
                "Sehrgar": "Near",
                "Aferist": "Light",
                "Stukach": "Aizawa"
            }
        }
    },
    
    "Tokyo Ghoul": {
        "icon": "🩸",
        "characters": {
            "tinchlik": {
                "Komissar": "Kishou Arima",
                "Sergant": "Akira Mado",
                "Mer": "Yoshitoki Washuu",
                "Shifokor": "Kimie Nishio",
                "Sevgil": "Rize Kamishiro",
                "Bomj": "Yoshimura",
                "Oddiy fuqaro": "Hide",
                "Omadli": "Kaneki",
                "O'z joniga qasqon": "Juuzou",
                "Kamikadze": "Amon"
            },
            "mafia": {
                "Don": "Eto (Bir ko'zli qirol)",
                "Mafioz": "Tatara",
                "Advokat": "Noro",
                "Qotil": "Yamori (Jason)",
                "Jurnalist": "Nishio"
            },
            "yolg'iz": {
                "Manyak": "Juuzou",
                "Aylanuvchi": "Kaneki",
                "Yondiruvchi": "Tatara",
                "Sehrgar": "Eto",
                "Aferist": "Uta",
                "Stukach": "Akira"
            }
        }
    },
    
    "Fullmetal Alchemist": {
        "icon": "⚗️",
        "characters": {
            "tinchlik": {
                "Komissar": "Roy Mustang",
                "Sergant": "Riza Hawkeye",
                "Mer": "King Bradley",
                "Shifokor": "Marcus",
                "Sevgil": "Winry Rockbell",
                "Bomj": "Sig Curtis",
                "Oddiy fuqaro": "Alphonse",
                "Omadli": "Edward",
                "O'z joniga qasqon": "Scar",
                "Kamikadze": "Maes Hughes"
            },
            "mafia": {
                "Don": "Ota (Gomunkul)",
                "Mafioz": "Lust",
                "Advokat": "Pride",
                "Qotil": "Gluttony",
                "Jurnalist": "Envy"
            },
            "yolg'iz": {
                "Manyak": "Gluttony",
                "Aylanuvchi": "Envy",
                "Yondiruvchi": "Roy",
                "Sehrgar": "Ota",
                "Aferist": "Edward",
                "Stukach": "Kimblee"
            }
        }
    },
    
    "Hunter x Hunter": {
        "icon": "🎯",
        "characters": {
            "tinchlik": {
                "Komissar": "Kurapika",
                "Sergant": "Leorio",
                "Mer": "Netero",
                "Shifokor": "Leorio",
                "Sevgil": "Pakunoda",
                "Bomj": "Ging",
                "Oddiy fuqaro": "Killua",
                "Omadli": "Gon",
                "O'z joniga qasqon": "Uvogin",
                "Kamikadze": "Pokkle"
            },
            "mafia": {
                "Don": "Meruem",
                "Mafioz": "Hisoka",
                "Advokat": "Chrollo",
                "Qotil": "Illumi",
                "Jurnalist": "Melody"
            },
            "yolg'iz": {
                "Manyak": "Hisoka",
                "Aylanuvchi": "Chimera",
                "Yondiruvchi": "Feitan",
                "Sehrgar": "Netero",
                "Aferist": "Gon",
                "Stukach": "Pakunoda"
            }
        }
    },
    
    "Sailor Moon": {
        "icon": "🌙",
        "characters": {
            "tinchlik": {
                "Komissar": "Tuxedo Mask",
                "Sergant": "Mercury",
                "Mer": "Queen Serenity",
                "Shifokor": "Jupiter",
                "Sevgil": "Venus",
                "Bomj": "Artemis",
                "Oddiy fuqaro": "Chibiusa",
                "Omadli": "Usagi",
                "O'z joniga qasqon": "Hotaru",
                "Kamikadze": "Mars"
            },
            "mafia": {
                "Don": "Metallia",
                "Mafioz": "Beryl",
                "Advokat": "Esmeraude",
                "Qotil": "Kunzite",
                "Jurnalist": "Zoisite"
            },
            "yolg'iz": {
                "Manyak": "Mistress 9",
                "Aylanuvchi": "Galaxia",
                "Yondiruvchi": "Fire",
                "Sehrgar": "Sailor Galaxia",
                "Aferist": "Neptune",
                "Stukach": "Pluto"
            }
        }
    },
    
    "Sword Art Online": {
        "icon": "⚔️",
        "characters": {
            "tinchlik": {
                "Komissar": "Heathcliff",
                "Sergant": "Asuna",
                "Mer": "Kayaba",
                "Shifokor": "Lisbeth",
                "Sevgil": "Sinon",
                "Bomj": "Klein",
                "Oddiy fuqaro": "Silica",
                "Omadli": "Kirito",
                "O'z joniga qasqon": "Yuuki",
                "Kamikadze": "Agil"
            },
            "mafia": {
                "Don": "Kayaba",
                "Mafioz": "Sugou",
                "Advokat": "Oberon",
                "Qotil": "Death Gun",
                "Jurnalist": "Argo"
            },
            "yolg'iz": {
                "Manyak": "Death Gun",
                "Aylanuvchi": "Yui",
                "Yondiruvchi": "Sinon",
                "Sehrgar": "Asuna",
                "Aferist": "Kirito",
                "Stukach": "Argo"
            }
        }
    },
    
    "Bleach": {
        "icon": "⚔️",
        "characters": {
            "tinchlik": {
                "Komissar": "Byakuya",
                "Sergant": "Rukia",
                "Mer": "Yamamoto",
                "Shifokor": "Unohana",
                "Sevgil": "Orihime",
                "Bomj": "Urahara",
                "Oddiy fuqaro": "Chad",
                "Omadli": "Ichigo",
                "O'z joniga qasqon": "Ulquiorra",
                "Kamikadze": "Renji"
            },
            "mafia": {
                "Don": "Aizen",
                "Mafioz": "Gin",
                "Advokat": "Tosen",
                "Qotil": "Grimmjow",
                "Jurnalist": "Szayel"
            },
            "yolg'iz": {
                "Manyak": "Nnoitra",
                "Aylanuvchi": "Ichigo",
                "Yondiruvchi": "Yamamoto",
                "Sehrgar": "Aizen",
                "Aferist": "Kisuke",
                "Stukach": "Nanao"
            }
        }
    },
    
    "Fairy Tail": {
        "icon": "🔥",
        "characters": {
            "tinchlik": {
                "Komissar": "Laxus",
                "Sergant": "Levy",
                "Mer": "Makarov",
                "Shifokor": "Wendy",
                "Sevgil": "Lucy",
                "Bomj": "Gajeel",
                "Oddiy fuqaro": "Happy",
                "Omadli": "Natsu",
                "O'z joniga qasqon": "Jellal",
                "Kamikadze": "Gray"
            },
            "mafia": {
                "Don": "Zeref",
                "Mafioz": "Acnologia",
                "Advokat": "Ultear",
                "Qotil": "Minerva",
                "Jurnalist": "Doranbolt"
            },
            "yolg'iz": {
                "Manyak": "Acnologia",
                "Aylanuvchi": "Lisanna",
                "Yondiruvchi": "Natsu",
                "Sehrgar": "Zeref",
                "Aferist": "Lucy",
                "Stukach": "Mest"
            }
        }
    },
    
    "Black Clover": {
        "icon": "🍀",
        "characters": {
            "tinchlik": {
                "Komissar": "Yami",
                "Sergant": "Noelle",
                "Mer": "Wizard King",
                "Shifokor": "Mimosa",
                "Sevgil": "Vanessa",
                "Bomj": "Finral",
                "Oddiy fuqaro": "Asta",
                "Omadli": "Luck",
                "O'z joniga qasqon": "Langris",
                "Kamikadze": "Magna"
            },
            "mafia": {
                "Don": "Dante",
                "Mafioz": "Zenon",
                "Advokat": "Vanica",
                "Qotil": "Rhya",
                "Jurnalist": "Gauche"
            },
            "yolg'iz": {
                "Manyak": "Vanica",
                "Aylanuvchi": "Asta",
                "Yondiruvchi": "Fuegoleon",
                "Sehrgar": "Julius",
                "Aferist": "Gauche",
                "Stukach": "Secre"
            }
        }
    },
    
    "Fire Force": {
        "icon": "🔥",
        "characters": {
            "tinchlik": {
                "Komissar": "Obi",
                "Sergant": "Tamaki",
                "Mer": "Raffles",
                "Shifokor": "Lisa",
                "Sevgil": "Hinawa",
                "Bomj": "Joker",
                "Oddiy fuqaro": "Shinra",
                "Omadli": "Arthur",
                "O'z joniga qasqon": "Sho",
                "Kamikadze": "Vulcan"
            },
            "mafia": {
                "Don": "Evangelist",
                "Mafioz": "Dragon",
                "Advokat": "Haumea",
                "Qotil": "Kurono",
                "Jurnalist": "Gold"
            },
            "yolg'iz": {
                "Manyak": "Infernal",
                "Aylanuvchi": "Shinra",
                "Yondiruvchi": "Sho",
                "Sehrgar": "Evangelist",
                "Aferist": "Joker",
                "Stukach": "Hibana"
            }
        }
    },
    
    "Dr. Stone": {
        "icon": "🧪",
        "characters": {
            "tinchlik": {
                "Komissar": "Taiju",
                "Sergant": "Kohaku",
                "Mer": "Senku",
                "Shifokor": "Senku",
                "Sevgil": "Amaryllis",
                "Bomj": "Magma",
                "Oddiy fuqaro": "Chrome",
                "Omadli": "Gen",
                "O'z joniga qasqon": "Hyoga",
                "Kamikadze": "Moz"
            },
            "mafia": {
                "Don": "Tsukasa",
                "Mafioz": "Homura",
                "Advokat": "Ukyo",
                "Qotil": "Nikki",
                "Jurnalist": "Ginro"
            },
            "yolg'iz": {
                "Manyak": "Magma",
                "Aylanuvchi": "Taiju",
                "Yondiruvchi": "Moz",
                "Sehrgar": "Senku",
                "Aferist": "Gen",
                "Stukach": "Kinro"
            }
        }
    },
    
    "The Promised Neverland": {
        "icon": "🏠",
        "characters": {
            "tinchlik": {
                "Komissar": "Norman",
                "Sergant": "Ray",
                "Mer": "Isabella",
                "Shifokor": "Anna",
                "Sevgil": "Janna",
                "Bomj": "Yett",
                "Oddiy fuqaro": "Phil",
                "Omadli": "Emma",
                "O'z joniga qasqon": "Chris",
                "Kamikadze": "Don"
            },
            "mafia": {
                "Don": "Peter Ratri",
                "Mafioz": "Musica",
                "Advokat": "Sonju",
                "Qotil": "Lewis",
                "Jurnalist": "Gilda"
            },
            "yolg'iz": {
                "Manyak": "Lewis",
                "Aylanuvchi": "Musica",
                "Yondiruvchi": "Norman",
                "Sehrgar": "Emma",
                "Aferist": "Ray",
                "Stukach": "Gilda"
            }
        }
    },
    
    "Berserk": {
        "icon": "⚔️",
        "characters": {
            "tinchlik": {
                "Komissar": "Griffith",
                "Sergant": "Casca",
                "Mer": "King of Midland",
                "Shifokor": "Rickert",
                "Sevgil": "Slan",
                "Bomj": "Guts",
                "Oddiy fuqaro": "Jill",
                "Omadli": "Puck",
                "O'z joniga qasqon": "Griffith",
                "Kamikadze": "Guts"
            },
            "mafia": {
                "Don": "Griffith (Femto)",
                "Mafioz": "Zodd",
                "Advokat": "Femto",
                "Qotil": "Guts",
                "Jurnalist": "Silat"
            },
            "yolg'iz": {
                "Manyak": "Zodd",
                "Aylanuvchi": "Guts",
                "Yondiruvchi": "Ganishka",
                "Sehrgar": "Schierke",
                "Aferist": "Puck",
                "Stukach": "Farnese"
            }
        }
    },
    
    "Vinland Saga": {
        "icon": "⚔️",
        "characters": {
            "tinchlik": {
                "Komissar": "Thorkell",
                "Sergant": "Helga",
                "Mer": "Canute",
                "Shifokor": "Gudrid",
                "Sevgil": "Helga",
                "Bomj": "Thorfinn",
                "Oddiy fuqaro": "Einar",
                "Omadli": "Thorkell",
                "O'z joniga qasqon": "Askeladd",
                "Kamikadze": "Thorgil"
            },
            "mafia": {
                "Don": "Floki",
                "Mafioz": "Askeladd",
                "Advokat": "Ketil",
                "Qotil": "Thorfinn",
                "Jurnalist": "Leif"
            },
            "yolg'iz": {
                "Manyak": "Askeladd",
                "Aylanuvchi": "Thorfinn",
                "Yondiruvchi": "Floki",
                "Sehrgar": "Canute",
                "Aferist": "Einar",
                "Stukach": "Snake"
            }
        }
    },
    
    "Monster": {
        "icon": "🧠",
        "characters": {
            "tinchlik": {
                "Komissar": "Lunge",
                "Sergant": "Eva",
                "Mer": "Richter",
                "Shifokor": "Tenma",
                "Sevgil": "Anna",
                "Bomj": "Wolff",
                "Oddiy fuqaro": "Dieter",
                "Omadli": "Otto",
                "O'z joniga qasqon": "Richard",
                "Kamikadze": "Grimmer"
            },
            "mafia": {
                "Don": "Johan",
                "Mafioz": "Roberto",
                "Advokat": "Christof",
                "Qotil": "Johan",
                "Jurnalist": "Gillen"
            },
            "yolg'iz": {
                "Manyak": "Johan",
                "Aylanuvchi": "Anna",
                "Yondiruvchi": "Christof",
                "Sehrgar": "Johan",
                "Aferist": "Wolff",
                "Stukach": "Lunge"
            }
        }
    },
    
    "Parasyte": {
        "icon": "🦠",
        "characters": {
            "tinchlik": {
                "Komissar": "Hirayama",
                "Sergant": "Murano",
                "Mer": "Takizawa",
                "Shifokor": "Uda",
                "Sevgil": "Kana",
                "Bomj": "Goto",
                "Oddiy fuqaro": "Shinichi",
                "Omadli": "Migi",
                "O'z joniga qasqon": "Reiko",
                "Kamikadze": "Goto"
            },
            "mafia": {
                "Don": "Goto",
                "Mafioz": "Reiko",
                "Advokat": "Tamiya",
                "Qotil": "Goto",
                "Jurnalist": "Uda"
            },
            "yolg'iz": {
                "Manyak": "Goto",
                "Aylanuvchi": "Shinichi",
                "Yondiruvchi": "Goto",
                "Sehrgar": "Migi",
                "Aferist": "Shinichi",
                "Stukach": "Murano"
            }
        }
    },
    
    "Psycho-Pass": {
        "icon": "🔫",
        "characters": {
            "tinchlik": {
                "Komissar": "Ginoza",
                "Sergant": "Akane",
                "Mer": "Jyoji",
                "Shifokor": "Shion",
                "Sevgil": "Yayoi",
                "Bomj": "Kogami",
                "Oddiy fuqaro": "Mika",
                "Omadli": "Kogami",
                "O'z joniga qasqon": "Makishima",
                "Kamikadze": "Kogami"
            },
            "mafia": {
                "Don": "Makishima",
                "Mafioz": "Kamui",
                "Advokat": "Togane",
                "Qotil": "Kogami",
                "Jurnalist": "Ginoza"
            },
            "yolg'iz": {
                "Manyak": "Makishima",
                "Aylanuvchi": "Kamui",
                "Yondiruvchi": "Kogami",
                "Sehrgar": "Sibyl",
                "Aferist": "Kogami",
                "Stukach": "Mika"
            }
        }
    },
    
    "Steins;Gate": {
        "icon": "⏰",
        "characters": {
            "tinchlik": {
                "Komissar": "Kurisu",
                "Sergant": "Mayuri",
                "Mer": "Tennouji",
                "Shifokor": "Kurisu",
                "Sevgil": "Faris",
                "Bomj": "Daru",
                "Oddiy fuqaro": "Luka",
                "Omadli": "Okabe",
                "O'z joniga qasqon": "Mayuri",
                "Kamikadze": "Okabe"
            },
            "mafia": {
                "Don": "SERN",
                "Mafioz": "Moeka",
                "Advokat": "Tennouji",
                "Qotil": "Nae",
                "Jurnalist": "Faris"
            },
            "yolg'iz": {
                "Manyak": "Moeka",
                "Aylanuvchi": "Okabe",
                "Yondiruvchi": "SERN",
                "Sehrgar": "Okabe",
                "Aferist": "Daru",
                "Stukach": "Faris"
            }
        }
    },
    
    "Code Geass": {
        "icon": "👑",
        "characters": {
            "tinchlik": {
                "Komissar": "Suzaku",
                "Sergant": "Kallen",
                "Mer": "Cornelia",
                "Shifokor": "Nunnally",
                "Sevgil": "Kaguya",
                "Bomj": "Jeremiah",
                "Oddiy fuqaro": "Rival",
                "Omadli": "Lelouch",
                "O'z joniga qasqon": "Euphy",
                "Kamikadze": "Suzaku"
            },
            "mafia": {
                "Don": "Lelouch",
                "Mafioz": "Schneizel",
                "Advokat": "Cornelia",
                "Qotil": "Suzaku",
                "Jurnalist": "Diethard"
            },
            "yolg'iz": {
                "Manyak": "Mao",
                "Aylanuvchi": "C.C.",
                "Yondiruvchi": "Kallen",
                "Sehrgar": "Lelouch",
                "Aferist": "Lelouch",
                "Stukach": "Ohgi"
            }
        }
    },
    
    "Gintama": {
        "icon": "🍡",
        "characters": {
            "tinchlik": {
                "Komissar": "Hijikata",
                "Sergant": "Okita",
                "Mer": "Matsudaira",
                "Shifokor": "Kagura",
                "Sevgil": "Tsukuyo",
                "Bomj": "Gintoki",
                "Oddiy fuqaro": "Shinpachi",
                "Omadli": "Gintoki",
                "O'z joniga qasqon": "Takasugi",
                "Kamikadze": "Katsura"
            },
            "mafia": {
                "Don": "Takasugi",
                "Mafioz": "Kamui",
                "Advokat": "Bansai",
                "Qotil": "Gintoki",
                "Jurnalist": "Sachan"
            },
            "yolg'iz": {
                "Manyak": "Takasugi",
                "Aylanuvchi": "Gintoki",
                "Yondiruvchi": "Kamui",
                "Sehrgar": "Gintoki",
                "Aferist": "Gintoki",
                "Stukach": "Sachan"
            }
        }
    },
    
    "Re:Zero": {
        "icon": "🔄",
        "characters": {
            "tinchlik": {
                "Komissar": "Reinhard",
                "Sergant": "Felt",
                "Mer": "Crusch",
                "Shifokor": "Emilia",
                "Sevgil": "Rem",
                "Bomj": "Al",
                "Oddiy fuqaro": "Petra",
                "Omadli": "Subaru",
                "O'z joniga qasqon": "Subaru",
                "Kamikadze": "Garfiel"
            },
            "mafia": {
                "Don": "Petelgeuse",
                "Mafioz": "Elsa",
                "Advokat": "Roswaal",
                "Qotil": "Elsa",
                "Jurnalist": "Otto"
            },
            "yolg'iz": {
                "Manyak": "Petelgeuse",
                "Aylanuvchi": "Garfiel",
                "Yondiruvchi": "Sirius",
                "Sehrgar": "Roswaal",
                "Aferist": "Subaru",
                "Stukach": "Otto"
            }
        }
    },
    
    "Overlord": {
        "icon": "💀",
        "characters": {
            "tinchlik": {
                "Komissar": "Gazef",
                "Sergant": "Climb",
                "Mer": "Ramposa",
                "Shifokor": "Lakyus",
                "Sevgil": "Albedo",
                "Bomj": "Zaryusu",
                "Oddiy fuqaro": "Enri",
                "Omadli": "Momon",
                "O'z joniga qasqon": "Carne",
                "Kamikadze": "Gazef"
            },
            "mafia": {
                "Don": "Ainz",
                "Mafioz": "Demiurge",
                "Advokat": "Albedo",
                "Qotil": "Shalltear",
                "Jurnalist": "Nigredo"
            },
            "yolg'iz": {
                "Manyak": "Shalltear",
                "Aylanuvchi": "Ainz",
                "Yondiruvchi": "Demiurge",
                "Sehrgar": "Ainz",
                "Aferist": "Momon",
                "Stukach": "Sebas"
            }
        }
    },
    
    "No Game No Life": {
        "icon": "🎮",
        "characters": {
            "tinchlik": {
                "Komissar": "Ino",
                "Sergant": "Jibril",
                "Mer": "Tet",
                "Shifokor": "Fiel",
                "Sevgil": "Shiro",
                "Bomj": "Sora",
                "Oddiy fuqaro": "Steph",
                "Omadli": "Sora",
                "O'z joniga qasqon": "Kurami",
                "Kamikadze": "Izuna"
            },
            "mafia": {
                "Don": "Tet",
                "Mafioz": "Amin",
                "Advokat": "Fiel",
                "Qotil": "Jibril",
                "Jurnalist": "Steph"
            },
            "yolg'iz": {
                "Manyak": "Amin",
                "Aylanuvchi": "Sora",
                "Yondiruvchi": "Izuna",
                "Sehrgar": "Tet",
                "Aferist": "Sora",
                "Stukach": "Steph"
            }
        }
    },
    
    "KonoSuba": {
        "icon": "💧",
        "characters": {
            "tinchlik": {
                "Komissar": "Darkness",
                "Sergant": "Megumin",
                "Mer": "Alderp",
                "Shifokor": "Aqua",
                "Sevgil": "Wiz",
                "Bomj": "Kazuma",
                "Oddiy fuqaro": "Yunyun",
                "Omadli": "Kazuma",
                "O'z joniga qasqon": "Aqua",
                "Kamikadze": "Megumin"
            },
            "mafia": {
                "Don": "Wolbach",
                "Mafioz": "Beldia",
                "Advokat": "Wiz",
                "Qotil": "Chris",
                "Jurnalist": "Yunyun"
            },
            "yolg'iz": {
                "Manyak": "Beldia",
                "Aylanuvchi": "Chris",
                "Yondiruvchi": "Megumin",
                "Sehrgar": "Wolbach",
                "Aferist": "Kazuma",
                "Stukach": "Yunyun"
            }
        }
    },
    
    "Mushoku Tensei": {
        "icon": "🧙",
        "characters": {
            "tinchlik": {
                "Komissar": "Paul",
                "Sergant": "Roxy",
                "Mer": "Perugius",
                "Shifokor": "Sylphie",
                "Sevgil": "Eris",
                "Bomj": "Rudeus",
                "Oddiy fuqaro": "Zenith",
                "Omadli": "Rudeus",
                "O'z joniga qasqon": "Paul",
                "Kamikadze": "Eris"
            },
            "mafia": {
                "Don": "Hitogami",
                "Mafioz": "Orsted",
                "Advokat": "Ariel",
                "Qotil": "Gall",
                "Jurnalist": "Linia"
            },
            "yolg'iz": {
                "Manyak": "Orsted",
                "Aylanuvchi": "Rudeus",
                "Yondiruvchi": "Eris",
                "Sehrgar": "Rudeus",
                "Aferist": "Rudeus",
                "Stukach": "Linia"
            }
        }
    },
    
    "Chainsaw Man": {
        "icon": "🪚",
        "characters": {
            "tinchlik": {
                "Komissar": "Aki",
                "Sergant": "Power",
                "Mer": "Makima",
                "Shifokor": "Himeno",
                "Sevgil": "Reze",
                "Bomj": "Denji",
                "Oddiy fuqaro": "Kobeni",
                "Omadli": "Denji",
                "O'z joniga qasqon": "Aki",
                "Kamikadze": "Power"
            },
            "mafia": {
                "Don": "Makima",
                "Mafioz": "Santa",
                "Advokat": "Kishibe",
                "Qotil": "Denji",
                "Jurnalist": "Angel"
            },
            "yolg'iz": {
                "Manyak": "Makima",
                "Aylanuvchi": "Denji",
                "Yondiruvchi": "Bomb",
                "Sehrgar": "Makima",
                "Aferist": "Denji",
                "Stukach": "Kobeni"
            }
        }
    },
    
    "Spy x Family": {
        "icon": "🕵️",
        "characters": {
            "tinchlik": {
                "Komissar": "Loid Forger (Twilight)",
                "Sergant": "Yor Forger (Thorn Princess)",
                "Mer": "Director",
                "Shifokor": "Becky",
                "Sevgil": "Yor",
                "Bomj": "Franky",
                "Oddiy fuqaro": "Damian",
                "Omadli": "Anya",
                "O'z joniga qasqon": "Yuri",
                "Kamikadze": "Bond"
            },
            "mafia": {
                "Don": "Donovan Desmond",
                "Mafioz": "Daybreak",
                "Advokat": "Handler",
                "Qotil": "Yor",
                "Jurnalist": "Fiona"
            },
            "yolg'iz": {
                "Manyak": "Daybreak",
                "Aylanuvchi": "Anya",
                "Yondiruvchi": "Yor",
                "Sehrgar": "Anya",
                "Aferist": "Loid",
                "Stukach": "Becky"
            }
        }
    },
    
    "Demon Slayer": {
        "icon": "🗡️",
        "characters": {
            "tinchlik": {
                "Komissar": "Giyu Tomioka",
                "Sergant": "Shinobu Kocho",
                "Mer": "Kagaya Ubuyashiki",
                "Shifokor": "Shinobu Kocho",
                "Sevgil": "Mitsuri Kanroji",
                "Bomj": "Yoriichi",
                "Oddiy fuqaro": "Zenitsu Agatsuma",
                "Omadli": "Inosuke Hashibira",
                "O'z joniga qasqon": "Kaigaku",
                "Kamikadze": "Gyomei"
            },
            "mafia": {
                "Don": "Muzan Kibutsuji",
                "Mafioz": "Kokushibo",
                "Advokat": "Doma",
                "Qotil": "Akaza",
                "Jurnalist": "Enmu"
            },
            "yolg'iz": {
                "Manyak": "Doma",
                "Aylanuvchi": "Nezuko",
                "Yondiruvchi": "Kyojuro",
                "Sehrgar": "Yoriichi",
                "Aferist": "Tanjiro",
                "Stukach": "Genya"
            }
        }
    }
}

# Anime nomlarini o'zbek tilida
ANIME_NAMES_UZ = {
    "Naruto": "🍥 Naruto",
    "One Piece": "🏴‍☠️ One Piece",
    "Attack on Titan": "⚔️ Attack on Titan",
    "Demon Slayer": "🗡️ Demon Slayer",
    "Jujutsu Kaisen": "👁️ Jujutsu Kaisen",
    "My Hero Academia": "💥 My Hero Academia",
    "Death Note": "📓 Death Note",
    "Tokyo Ghoul": "🩸 Tokyo Ghoul",
    "Fullmetal Alchemist": "⚗️ Fullmetal Alchemist",
    "Hunter x Hunter": "🎯 Hunter x Hunter",
    "Sailor Moon": "🌙 Sailor Moon",
    "Sword Art Online": "⚔️ Sword Art Online",
    "Bleach": "⚔️ Bleach",
    "Fairy Tail": "🔥 Fairy Tail",
    "Black Clover": "🍀 Black Clover",
    "Fire Force": "🔥 Fire Force",
    "Dr. Stone": "🧪 Dr. Stone",
    "The Promised Neverland": "🏠 The Promised Neverland",
    "Berserk": "⚔️ Berserk",
    "Vinland Saga": "⚔️ Vinland Saga",
    "Monster": "🧠 Monster",
    "Parasyte": "🦠 Parasyte",
    "Psycho-Pass": "🔫 Psycho-Pass",
    "Steins;Gate": "⏰ Steins;Gate",
    "Code Geass": "👑 Code Geass",
    "Gintama": "🍡 Gintama",
    "Re:Zero": "🔄 Re:Zero",
    "Overlord": "💀 Overlord",
    "No Game No Life": "🎮 No Game No Life",
    "KonoSuba": "💧 KonoSuba",
    "Mushoku Tensei": "🧙 Mushoku Tensei",
    "Chainsaw Man": "🪚 Chainsaw Man",
    "Spy x Family": "🕵️ Spy x Family",
}
'''

with open('/mnt/agents/output/animafia_bot/anime_worlds.py', 'w', encoding='utf-8') as f:
    f.write(anime_worlds_content)

print("✅ anime_worlds.py yaratildi! (30 ta anime olami)")
