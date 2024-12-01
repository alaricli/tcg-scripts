import json


def load_json(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    return None


def map_pack(pack_id):
    pack_map = {
        "AN001_0010_00_000": "A1-1",  # Mewtwo
        "AN001_0020_00_000": "A1-2",  # Charizard
        "AN001_0030_00_000": "A1-3",  # Pikachu
        "AP001_0010_00_000": "PA1-1",  # Promo A
        "AP001_0020_00_000": "PA1-2",  # Promo B
    }
    return pack_map.get(pack_id, "UNKNOWN")


def map_weakness(superType, name):
    special_cases = {
        "Zapdos": "Lightning",
        "Zapdos ex": "Lightning",
        "Snom": "Metal",
        "Frosmoth": "Metal",
        "Moltres ex": "Lightning",
        "Moltres": "Lightning",
        "Clefairy": "Metal",
        "Clefable": "Metal",
        "Mankey": "Psychic",
        "Primeape": "Psychic",
        "Hitmonlee": "Psychic",
        "Hitmonchan": "Psychic",
        "Machop": "Psychic",
        "Machoke": "Psychic",
        "Machamp": "Psychic",
        "Machamp ex": "Psychic",
        "Mienfoo": "Psychic",
        "Mienshao": "Psychic",
        "Clobbopus": "Psychic",
        "Grapploct": "Psychic",
        "Pidgey": "Lightning",
        "Pidgeotto": "Lightning",
        "Pidgeot": "Lightning",
        "Pidgeot ex": "Lightning",
        "Spearow": "Lightning",
        "Fearow": "Lightning",
        "Farfetch'd": "Lightning",
        "Doduo": "Lightning",
        "Dodrio": "Lightning",
        "Aerodactyl": "Lightning",
    }

    if name in special_cases:
        return special_cases[name]

    weakness_map = {
        "Darkness": "Fighting",
        "Colorless": "Fighting",
        "Fighting": "Grass",
        "Grass": "Fire",
        "Lightning": "Fighting",
        "Metal": "Fire",
        "Psychic": "Darkness",
        "Water": "Lightning",
        "Fire": "Water",
    }
    return weakness_map.get(superType, None)


def map_pokemon_data(name):
    pokemon_data_map = {
        "Abra": {"dexNumber": 63, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Aerodactyl": {
            "dexNumber": 142,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 100,
        },
        "Alakazam": {
            "dexNumber": 65,
            "subtype": ["Stage 2"],
            "retreatCost": 2,
            "HP": 130,
        },
        "Arbok": {"dexNumber": 24, "subtype": ["Stage 1"], "retreatCost": 2, "HP": 100},
        "Arcanine": {
            "dexNumber": 59,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 130,
        },
        "Arcanine ex": {
            "dexNumber": 59,
            "subtype": ["Stage 1", "ex"],
            "retreatCost": 2,
            "HP": 150,
        },
        "Articuno": {
            "dexNumber": 144,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 100,
        },
        "Articuno ex": {
            "dexNumber": 144,
            "subtype": ["Basic", "ex"],
            "retreatCost": 2,
            "HP": 140,
        },
        "Beedrill": {
            "dexNumber": 15,
            "subtype": ["Stage 2"],
            "retreatCost": 1,
            "HP": 120,
        },
        "Bellsprout": {
            "dexNumber": 69,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 60,
        },
        "Bisharp": {
            "dexNumber": 625,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 90,
        },
        "Blastoise": {
            "dexNumber": 9,
            "subtype": ["Stage 2"],
            "retreatCost": 3,
            "HP": 150,
        },
        "Blastoise ex": {
            "dexNumber": 9,
            "subtype": ["Stage 2", "ex"],
            "retreatCost": 3,
            "HP": 180,
        },
        "Blitzle": {"dexNumber": 522, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Bruxish": {"dexNumber": 779, "subtype": ["Basic"], "retreatCost": 1, "HP": 90},
        "Bulbasaur": {"dexNumber": 1, "subtype": ["Basic"], "retreatCost": 1, "HP": 70},
        "Butterfree": {
            "dexNumber": 12,
            "subtype": ["Stage 2"],
            "retreatCost": 1,
            "HP": 120,
        },
        "Caterpie": {"dexNumber": 10, "subtype": ["Basic"], "retreatCost": 1, "HP": 50},
        "Centiskorch": {
            "dexNumber": 851,
            "subtype": ["Stage 1"],
            "retreatCost": 3,
            "HP": 130,
        },
        "Chansey": {
            "dexNumber": 113,
            "subtype": ["Basic"],
            "retreatCost": 3,
            "HP": 120,
        },
        "Charizard": {
            "dexNumber": 6,
            "subtype": ["Stage 2"],
            "retreatCost": 2,
            "HP": 150,
        },
        "Charizard ex": {
            "dexNumber": 6,
            "subtype": ["Stage 2", "ex"],
            "retreatCost": 2,
            "HP": 180,
        },
        "Charmander": {
            "dexNumber": 4,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 60,
        },
        "Charmeleon": {
            "dexNumber": 5,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 90,
        },
        "Cinccino": {
            "dexNumber": 573,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 90,
        },
        "Clefairy": {"dexNumber": 35, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Clefable": {
            "dexNumber": 36,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 100,
        },
        "Clobbopus": {
            "dexNumber": 852,
            "subtype": ["Basic"],
            "retreatCost": 2,
            "HP": 80,
        },
        "Cloyster": {
            "dexNumber": 91,
            "subtype": ["Stage 1"],
            "retreatCost": 3,
            "HP": 120,
        },
        "Cottonee": {
            "dexNumber": 546,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 50,
        },
        "Cubone": {"dexNumber": 104, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Dewgong": {
            "dexNumber": 87,
            "subtype": ["Stage 1"],
            "retreatCost": 3,
            "HP": 120,
        },
        "Diglett": {"dexNumber": 50, "subtype": ["Basic"], "retreatCost": 1, "HP": 50},
        "Ditto": {"dexNumber": 132, "subtype": ["Basic"], "retreatCost": 1, "HP": 70},
        "Dodrio": {"dexNumber": 85, "subtype": ["Stage 1"], "retreatCost": 0, "HP": 80},
        "Doduo": {"dexNumber": 84, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Dragonair": {
            "dexNumber": 148,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 100,
        },
        "Dragonite": {
            "dexNumber": 149,
            "subtype": ["Stage 2"],
            "retreatCost": 3,
            "HP": 160,
        },
        "Dratini": {"dexNumber": 147, "subtype": ["Basic"], "retreatCost": 1, "HP": 70},
        "Drowzee": {"dexNumber": 96, "subtype": ["Basic"], "retreatCost": 2, "HP": 70},
        "Dubwool": {
            "dexNumber": 832,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 120,
        },
        "Ducklett": {
            "dexNumber": 580,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 50,
        },
        "Dugtrio": {
            "dexNumber": 51,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 70,
        },
        "Eelektrik": {
            "dexNumber": 603,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 80,
        },
        "Eelektross": {
            "dexNumber": 604,
            "subtype": ["Stage 2"],
            "retreatCost": 3,
            "HP": 140,
        },
        "Eevee": {"dexNumber": 133, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Ekans": {"dexNumber": 23, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Electabuzz": {
            "dexNumber": 125,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 70,
        },
        "Electrode": {
            "dexNumber": 101,
            "subtype": ["Stage 1"],
            "retreatCost": 0,
            "HP": 80,
        },
        "Exeggcute": {
            "dexNumber": 102,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 50,
        },
        "Exeggutor": {
            "dexNumber": 103,
            "subtype": ["Stage 1"],
            "retreatCost": 3,
            "HP": 130,
        },
        "Exeggutor ex": {
            "dexNumber": 103,
            "subtype": ["Stage 1", "ex"],
            "retreatCost": 3,
            "HP": 160,
        },
        "Farfetch'd": {
            "dexNumber": 83,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 60,
        },
        "Fearow": {
            "dexNumber": 22,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 100,
        },
        "Flareon": {
            "dexNumber": 136,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 120,
        },
        "Froakie": {"dexNumber": 656, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Frogadier": {
            "dexNumber": 657,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 80,
        },
        "Frosmoth": {
            "dexNumber": 873,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 90,
        },
        "Gardevoir": {
            "dexNumber": 282,
            "subtype": ["Stage 2"],
            "retreatCost": 2,
            "HP": 110,
        },
        "Gastly": {"dexNumber": 92, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Gengar": {
            "dexNumber": 94,
            "subtype": ["Stage 2"],
            "retreatCost": 2,
            "HP": 130,
        },
        "Gengar ex": {
            "dexNumber": 94,
            "subtype": ["Stage 2", "ex"],
            "retreatCost": 2,
            "HP": 170,
        },
        "Geodude": {"dexNumber": 74, "subtype": ["Basic"], "retreatCost": 2, "HP": 70},
        "Gogoat": {
            "dexNumber": 673,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 120,
        },
        "Goldeen": {"dexNumber": 118, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Golbat": {"dexNumber": 42, "subtype": ["Stage 1"], "retreatCost": 1, "HP": 70},
        "Golett": {"dexNumber": 622, "subtype": ["Basic"], "retreatCost": 3, "HP": 90},
        "Golurk": {
            "dexNumber": 623,
            "subtype": ["Stage 1"],
            "retreatCost": 4,
            "HP": 140,
        },
        "Golem": {"dexNumber": 76, "subtype": ["Stage 2"], "retreatCost": 4, "HP": 160},
        "Grapploct": {
            "dexNumber": 853,
            "subtype": ["Stage 1"],
            "retreatCost": 3,
            "HP": 130,
        },
        "Graveler": {
            "dexNumber": 75,
            "subtype": ["Stage 1"],
            "retreatCost": 3,
            "HP": 100,
        },
        "Greninja": {
            "dexNumber": 658,
            "subtype": ["Stage 2"],
            "retreatCost": 1,
            "HP": 120,
        },
        "Grimer": {"dexNumber": 88, "subtype": ["Basic"], "retreatCost": 3, "HP": 70},
        "Growlithe": {
            "dexNumber": 58,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 70,
        },
        "Gyarados": {
            "dexNumber": 130,
            "subtype": ["Stage 1"],
            "retreatCost": 4,
            "HP": 150,
        },
        "Haunter": {
            "dexNumber": 93,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 70,
        },
        "Heatmor": {"dexNumber": 631, "subtype": ["Basic"], "retreatCost": 1, "HP": 80},
        "Helioptile": {
            "dexNumber": 694,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 60,
        },
        "Heliolisk": {
            "dexNumber": 695,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 90,
        },
        "Hitmonlee": {
            "dexNumber": 106,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 80,
        },
        "Hitmonchan": {
            "dexNumber": 107,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 80,
        },
        "Horsea": {"dexNumber": 116, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Hypno": {"dexNumber": 97, "subtype": ["Stage 1"], "retreatCost": 2, "HP": 100},
        "Ivysaur": {"dexNumber": 2, "subtype": ["Stage 1"], "retreatCost": 2, "HP": 90},
        "Jigglypuff": {
            "dexNumber": 39,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 50,
        },
        "Jolteon": {
            "dexNumber": 135,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 90,
        },
        "Jynx": {"dexNumber": 124, "subtype": ["Basic"], "retreatCost": 1, "HP": 80},
        "Kakuna": {"dexNumber": 14, "subtype": ["Stage 1"], "retreatCost": 2, "HP": 80},
        "Kadabra": {
            "dexNumber": 64,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 80,
        },
        "Kangaskhan": {
            "dexNumber": 115,
            "subtype": ["Basic"],
            "retreatCost": 3,
            "HP": 100,
        },
        "Kabutops": {
            "dexNumber": 141,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 140,
        },
        "Kabuto": {"dexNumber": 140, "subtype": ["Basic"], "retreatCost": 1, "HP": 90},
        "Kingler": {
            "dexNumber": 99,
            "subtype": ["Stage 1"],
            "retreatCost": 3,
            "HP": 120,
        },
        "Koffing": {"dexNumber": 109, "subtype": ["Basic"], "retreatCost": 1, "HP": 70},
        "Krabby": {"dexNumber": 98, "subtype": ["Basic"], "retreatCost": 2, "HP": 70},
        "Lapras": {"dexNumber": 131, "subtype": ["Basic"], "retreatCost": 2, "HP": 100},
        "Lapras ex": {
            "dexNumber": 131,
            "subtype": ["Basic", "ex"],
            "retreatCost": 3,
            "HP": 140,
        },
        "Lickitung": {
            "dexNumber": 108,
            "subtype": ["Basic"],
            "retreatCost": 3,
            "HP": 90,
        },
        "Lilligant": {
            "dexNumber": 549,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 100,
        },
        "Machamp": {
            "dexNumber": 68,
            "subtype": ["Stage 2"],
            "retreatCost": 3,
            "HP": 150,
        },
        "Machamp ex": {
            "dexNumber": 68,
            "subtype": ["Stage 2", "ex"],
            "retreatCost": 3,
            "HP": 180,
        },
        "Machoke": {
            "dexNumber": 67,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 100,
        },
        "Machop": {"dexNumber": 66, "subtype": ["Basic"], "retreatCost": 2, "HP": 70},
        "Magikarp": {
            "dexNumber": 129,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 30,
        },
        "Magmar": {"dexNumber": 126, "subtype": ["Basic"], "retreatCost": 2, "HP": 80},
        "Magnemite": {
            "dexNumber": 81,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 60,
        },
        "Magneton": {
            "dexNumber": 82,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 80,
        },
        "Mankey": {"dexNumber": 56, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Mawile": {"dexNumber": 303, "subtype": ["Basic"], "retreatCost": 1, "HP": 70},
        "Marowak": {
            "dexNumber": 105,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 100,
        },
        "Marowak ex": {
            "dexNumber": 105,
            "subtype": ["Stage 1", "ex"],
            "retreatCost": 1,
            "HP": 140,
        },
        "Meowth": {"dexNumber": 52, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Minccino": {
            "dexNumber": 572,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 60,
        },
        "Mienfoo": {
            "dexNumber": 619,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 60,
        },
        "Mewtwo": {"dexNumber": 150, "subtype": ["Basic"], "retreatCost": 2, "HP": 120},
        "Mewtwo ex": {
            "dexNumber": 150,
            "subtype": ["Basic", "ex"],
            "retreatCost": 2,
            "HP": 150,
        },
        "Mienshao": {
            "dexNumber": 620,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 80,
        },
        "Melmetal": {
            "dexNumber": 809,
            "subtype": ["Stage 1"],
            "retreatCost": 3,
            "HP": 130,
        },
        "Meltan": {"dexNumber": 808, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Mew": {"dexNumber": 151, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Metapod": {
            "dexNumber": 11,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 80,
        },
        "Mr. Mime": {
            "dexNumber": 122,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 80,
        },
        "Moltres": {
            "dexNumber": 146,
            "subtype": ["Basic"],
            "retreatCost": 2,
            "HP": 100,
        },
        "Moltres ex": {
            "dexNumber": 146,
            "subtype": ["Basic", "ex"],
            "retreatCost": 2,
            "HP": 140,
        },
        "Muk": {"dexNumber": 89, "subtype": ["Stage 1"], "retreatCost": 3, "HP": 130},
        "Nidoking": {
            "dexNumber": 34,
            "subtype": ["Stage 2"],
            "retreatCost": 3,
            "HP": 150,
        },
        "Nidoran♂": {"dexNumber": 32, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Nidoran♀": {"dexNumber": 29, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Nidorina": {
            "dexNumber": 30,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 80,
        },
        "Nidorino": {
            "dexNumber": 33,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 90,
        },
        "Nidoqueen": {
            "dexNumber": 31,
            "subtype": ["Stage 2"],
            "retreatCost": 2,
            "HP": 140,
        },
        "Ninetales": {
            "dexNumber": 38,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 90,
        },
        "Oddish": {"dexNumber": 43, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Omanyte": {"dexNumber": 138, "subtype": ["Basic"], "retreatCost": 1, "HP": 90},
        "Omastar": {
            "dexNumber": 139,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 140,
        },
        "Onix": {"dexNumber": 95, "subtype": ["Basic"], "retreatCost": 4, "HP": 110},
        "Paras": {"dexNumber": 46, "subtype": ["Basic"], "retreatCost": 1, "HP": 70},
        "Parasect": {
            "dexNumber": 47,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 120,
        },
        "Pawniard": {
            "dexNumber": 624,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 50,
        },
        "Persian": {
            "dexNumber": 53,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 90,
        },
        "Pidgey": {"dexNumber": 16, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Pidgeotto": {
            "dexNumber": 17,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 80,
        },
        "Pidgeot": {
            "dexNumber": 18,
            "subtype": ["Stage 2"],
            "retreatCost": 1,
            "HP": 130,
        },
        "Pikachu": {"dexNumber": 25, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Pikachu ex": {
            "dexNumber": 25,
            "subtype": ["Basic", "ex"],
            "retreatCost": 1,
            "HP": 120,
        },
        "Pincurchin": {
            "dexNumber": 871,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 70,
        },
        "Pinsir": {"dexNumber": 127, "subtype": ["Basic"], "retreatCost": 2, "HP": 90},
        "Poliwag": {"dexNumber": 60, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Poliwhirl": {
            "dexNumber": 61,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 90,
        },
        "Poliwrath": {
            "dexNumber": 62,
            "subtype": ["Stage 2"],
            "retreatCost": 2,
            "HP": 150,
        },
        "Ponyta": {"dexNumber": 77, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Porygon": {"dexNumber": 137, "subtype": ["Basic"], "retreatCost": 1, "HP": 50},
        "Primeape": {
            "dexNumber": 57,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 90,
        },
        "Psyduck": {"dexNumber": 54, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Pyukumuku": {
            "dexNumber": 771,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 70,
        },
        "Raichu": {
            "dexNumber": 26,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 100,
        },
        "Ralts": {
            "dexNumber": 280,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 60,
        },
        "Kirlia": {
            "dexNumber": 281,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 80,
        },
        "Rapidash": {
            "dexNumber": 78,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 100,
        },
        "Raticate": {
            "dexNumber": 20,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 80,
        },
        "Rattata": {"dexNumber": 19, "subtype": ["Basic"], "retreatCost": 1, "HP": 40},
        "Rhyhorn": {"dexNumber": 111, "subtype": ["Basic"], "retreatCost": 3, "HP": 80},
        "Rhydon": {
            "dexNumber": 112,
            "subtype": ["Stage 1"],
            "retreatCost": 4,
            "HP": 120,
        },
        "Salandit": {
            "dexNumber": 757,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 60,
        },
        "Salazzle": {
            "dexNumber": 758,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 90,
        },
        "Sandshrew": {
            "dexNumber": 27,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 70,
        },
        "Sandslash": {
            "dexNumber": 28,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 100,
        },
        "Scyther": {"dexNumber": 123, "subtype": ["Basic"], "retreatCost": 1, "HP": 70},
        "Seadra": {
            "dexNumber": 117,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 70,
        },
        "Seaking": {
            "dexNumber": 119,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 100,
        },
        "Seel": {"dexNumber": 86, "subtype": ["Basic"], "retreatCost": 2, "HP": 80},
        "Shellder": {"dexNumber": 90, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Sizzlipede": {
            "dexNumber": 850,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 60,
        },
        "Skiddo": {"dexNumber": 672, "subtype": ["Basic"], "retreatCost": 1, "HP": 70},
        "Slowbro": {
            "dexNumber": 80,
            "subtype": ["Stage 1"],
            "retreatCost": 3,
            "HP": 130,
        },
        "Slowpoke": {"dexNumber": 79, "subtype": ["Basic"], "retreatCost": 2, "HP": 70},
        "Snom": {"dexNumber": 872, "subtype": ["Basic"], "retreatCost": 1, "HP": 50},
        "Snorlax": {
            "dexNumber": 143,
            "subtype": ["Basic"],
            "retreatCost": 4,
            "HP": 150,
        },
        "Spearow": {"dexNumber": 21, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Squirtle": {"dexNumber": 7, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Starmie": {
            "dexNumber": 121,
            "subtype": ["Stage 1"],
            "retreatCost": 0,
            "HP": 90,
        },
        "Starmie ex": {
            "dexNumber": 121,
            "subtype": ["Stage 1", "ex"],
            "retreatCost": 0,
            "HP": 130,
        },
        "Staryu": {"dexNumber": 120, "subtype": ["Basic"], "retreatCost": 1, "HP": 50},
        "Swoobat": {
            "dexNumber": 528,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 90,
        },
        "Swanna": {
            "dexNumber": 581,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 90,
        },
        "Tangela": {"dexNumber": 114, "subtype": ["Basic"], "retreatCost": 2, "HP": 80},
        "Tauros": {"dexNumber": 128, "subtype": ["Basic"], "retreatCost": 2, "HP": 100},
        "Tentacool": {
            "dexNumber": 72,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 60,
        },
        "Tentacruel": {
            "dexNumber": 73,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 110,
        },
        "Tynamo": {"dexNumber": 602, "subtype": ["Basic"], "retreatCost": 1, "HP": 30},
        "Vaporeon": {
            "dexNumber": 134,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 130,
        },
        "Venomoth": {
            "dexNumber": 49,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 80,
        },
        "Venonat": {"dexNumber": 48, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Venusaur": {
            "dexNumber": 3,
            "subtype": ["Stage 2"],
            "retreatCost": 3,
            "HP": 160,
        },
        "Venusaur ex": {
            "dexNumber": 3,
            "subtype": ["Stage 2", "ex"],
            "retreatCost": 3,
            "HP": 190,
        },
        "Victreebel": {
            "dexNumber": 71,
            "subtype": ["Stage 2"],
            "retreatCost": 2,
            "HP": 140,
        },
        "Vileplume": {
            "dexNumber": 45,
            "subtype": ["Stage 2"],
            "retreatCost": 3,
            "HP": 140,
        },
        "Voltorb": {
            "dexNumber": 100,
            "subtype": ["Basic"],
            "retreatCost": 1,
            "HP": 60,
        },
        "Vulpix": {"dexNumber": 37, "subtype": ["Basic"], "retreatCost": 1, "HP": 50},
        "Wartortle": {
            "dexNumber": 8,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 80,
        },
        "Weepinbell": {
            "dexNumber": 70,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 90,
        },
        "Weedle": {"dexNumber": 13, "subtype": ["Basic"], "retreatCost": 1, "HP": 50},
        "Weezing": {
            "dexNumber": 110,
            "subtype": ["Stage 1"],
            "retreatCost": 3,
            "HP": 110,
        },
        "Whimsicott": {
            "dexNumber": 547,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 80,
        },
        "Wigglytuff": {
            "dexNumber": 40,
            "subtype": ["Stage 1"],
            "retreatCost": 2,
            "HP": 100,
        },
        "Wigglytuff ex": {
            "dexNumber": 40,
            "subtype": ["Stage 1", "ex"],
            "retreatCost": 2,
            "HP": 140,
        },
        "Woobat": {"dexNumber": 527, "subtype": ["Basic"], "retreatCost": 1, "HP": 60},
        "Wooloo": {"dexNumber": 831, "subtype": ["Basic"], "retreatCost": 1, "HP": 70},
        "Zebstrika": {
            "dexNumber": 523,
            "subtype": ["Stage 1"],
            "retreatCost": 1,
            "HP": 90,
        },
        "Zubat": {"dexNumber": 41, "subtype": ["Basic"], "retreatCost": 1, "HP": 50},
        "Zapdos": {"dexNumber": 145, "subtype": ["Basic"], "retreatCost": 1, "HP": 100},
        "Zapdos ex": {
            "dexNumber": 145,
            "subtype": ["Basic", "ex"],
            "retreatCost": 1,
            "HP": 130,
        },
    }
    return pokemon_data_map.get(name, None)


cards_with_abilities = {
    "PK_10_000070_00",
    "PK_90_000070_00",
    "PK_10_001320_00",
    "PK_20_001230_00",
    "PK_10_001230_00",
    "PK_20_001230_01",
    "PK_10_000890_00",
    "PK_10_000890_00",
    "PK_10_001250_00",
    "PK_10_000980_00",
    "PK_10_000610_00",
    "PK_10_002070_00",
    "PK_20_002070_00",
    "PK_10_000200_00",
    "PK_10_001770_00",
    "PK_20_001770_00",
    "PK_20_001880_00",
    "PK_10_001880_00",
}


def map_abilities(externalId):
    ability_map = {
        "PK_10_000070_00": "Powder Heal: Once during your turn, you may heal 20 damage from each of your Pokémon.",
        "PK_90_000070_00": "Powder Heal: Once during your turn, you may heal 20 damage from each of your Pokémon.",
        "PK_10_001320_00": "Psy Shadow: Once during your turn, you may take a Psychic Energy from your Energy Zone and attach it to the Psychic Pokémon in the Active Spot.",
        "PK_20_001230_00": "Shadowy Spellbind: As long as this Pokémon is in the Active Spot, your opponent can't use any Supporter cards from their hand.",
        "PK_10_001230_00": "Shadowy Spellbind: As long as this Pokémon is in the Active Spot, your opponent can't use any Supporter cards from their hand.",
        "PK_20_001230_01": "Shadowy Spellbind: As long as this Pokémon is in the Active Spot, your opponent can't use any Supporter cards from their hand.",
        "PK_10_000890_00": "Water Shuriken: Once during your turn, you may do 20 damage to 1 of your opponent's Pokémon.",
        "PK_10_000890_00": "Water Shuriken: Once during your turn, you may do 20 damage to 1 of your opponent's Pokémon.",
        "PK_10_001250_00": "Sleep Pendulum: Once during your turn, you may flip a coin. If heads, your opponent's Active Pokémon is now asleep.",
        "PK_10_000980_00": "Volt Charge: Once during your turn, you may take a Lightning Energy from your Energy Zone and attach it to this Pokémon.",
        "PK_10_000610_00": "Counterattack: If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon, do 20 damage to the Attacking Pokémon.",
        "PK_20_001880_00": "Drive Off: Once during your turn, you may switch out your opponent's Active Pokémon to the Bench. (Your Opponent chooses the new Active Pokémon.)",
        "PK_10_001880_00": "Drive Off: Once during your turn, you may switch out your opponent's Active Pokémon to the Bench. (Your Opponent chooses the new Active Pokémon.)",
        "PK_10_002070_00": "Data Scan: Once during your turn, you may look at the top card of your deck.",
        "PK_20_002070_00": "Data Scan: Once during your turn, you may look at the top card of your deck.",
        "PK_10_000200_00": "Fragrance Trap: If this Pokémon is in the Active Spot, once during your turn, you may switch in 1 of your opponent's Benched Basic Pokémon to the Active Spot.",
        "PK_10_001770_00": "Gas Leak: Once during your turn, if this Pokémon is in the Active Spot, you may make your opponent's Active Pokémon Poisoned.",
        "PK_20_001770_00": "Gas Leak: Once during your turn, if this Pokémon is in the Active Spot, you may make your opponent's Active Pokémon Poisoned.",
    }
    return ability_map.get(externalId, None)


def transform_card(card):
    pokemon_data = map_pokemon_data(card["name"])

    return {
        "id": (
            ("P-A-" + str(card["collectionNumber"]))
            if card["expansionKey"] == "PROMO-A"
            else card["expansionKey"] + "-" + str(card["collectionNumber"])
        ),
        "name": card["name"],
        "hp": (
            pokemon_data["HP"] if pokemon_data and card["type"] == "Pokemon" else None
        ),
        "retreatCost": (
            pokemon_data["retreatCost"]
            if pokemon_data and card["type"] == "Pokemon"
            else None
        ),
        "artist": card["artists"][0]["name"] if card.get("artists") else None,
        "regulationMark": card.get("series", None),
        "cardNumber": card["collectionNumber"] if "collectionNumber" in card else None,
        "nationalPokedexNumber": (
            pokemon_data["dexNumber"]
            if pokemon_data and card["type"] == "Pokemon"
            else None
        ),
        "hasRuleBox": " ex" in f" {card['name']} ",
        "hasAbility": card["externalId"] in cards_with_abilities,
        "ability": map_abilities(card["externalId"]),
        "trainerCardText": card["description"] if "description" in card else None,
        "rarity": card["rarityName"] if "rarityName" in card else None,
        "superType": "Trainer" if card.get("trainerType") else card.get("type"),
        "subTypes": (
            [card.get("trainerType")]
            or (pokemon_data["subtype"] if pokemon_data else None)
        ),
        "expansionId": (
            "P-A" if card.get("expansionKey") == "PROMO-A" else card.get("expansionKey")
        ),
        "energyTypes": card["types"] if "types" in card else [],
        "attackEnergyTypes": (card["types"] if "types" in card else []),
        "weakness": (
            [map_weakness(card["types"][0], card["name"])] if card.get("types") else []
        ),
        "resistance": [],
        "rules": (
            ["When your Pokémon ex is Knocked Out, your opponent gets 2 points"]
            if (" ex" in f" {card.get('name', '')} ")
            else []
        ),
        "cardImages": {
            "small": card["displayImageUrl"] if "displayImageUrl" in card else None,
            "large": card["displayImageUrl"] if "displayImageUrl" in card else None,
        },
        "isPocket": True,
        "attacks": [],
        "foundInPacks": [map_pack(pack_id) for pack_id in card.get("foundInPacks", [])],
        "dustCost": card.get("dustCost", None),  # Added based on provided data
    }


if __name__ == "__main__":
    data = load_json("pocket.json")
    if data is None:
        print("Failed to load JSON data.")
        exit(1)

    transformed_cards = []

    for card in data:
        transformed_card = transform_card(card)
        transformed_cards.append(transformed_card)

    output = "upload.json"
    with open(output, "w") as file:
        json.dump(transformed_cards, file, indent=4)

    print(f"Saved all pocket cards to {output}")
