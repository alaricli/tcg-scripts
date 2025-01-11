import os
import urllib.request

response = [
    {
        "id": "A1-1",
        "name": "Bulbasaur",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000010_00_FUSHIGIDANE_C.png",
        },
    },
    {
        "id": "A1a-001",
        "name": "Exeggcute",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_001_EN.webp",
        },
    },
    {
        "id": "P-A-1",
        "name": "Potion",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_90_000010_00_KIZUGUSURI_C.png",
        },
    },
    {
        "id": "A1-2",
        "name": "Ivysaur",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000020_00_FUSHIGISOU_U.png",
        },
    },
    {
        "id": "A1a-002",
        "name": "Exeggutor",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_002_EN.webp",
        },
    },
    {
        "id": "P-A-2",
        "name": "X Speed",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_90_000020_00_SPEEDER_C.png",
        },
    },
    {
        "id": "A1a-003",
        "name": "Celebi ex",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_003_EN.webp",
        },
    },
    {
        "id": "P-A-3",
        "name": "Hand Scope",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_90_000050_00_HANDSCOPE_C.png",
        },
    },
    {
        "id": "A1-3",
        "name": "Venusaur",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000030_00_FUSHIGIBANA_R.png",
        },
    },
    {
        "id": "P-A-4",
        "name": "Pokédex",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/P-A/P-A_004_EN.webp",
        },
    },
    {
        "id": "A1-4",
        "name": "Venusaur ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000040_00_FUSHIGIBANAex_RR.png",
        },
    },
    {
        "id": "A1a-004",
        "name": "Snivy",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_004_EN.webp",
        },
    },
    {
        "id": "A1a-005",
        "name": "Servine",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_005_EN.webp",
        },
    },
    {
        "id": "A1-5",
        "name": "Caterpie",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000050_00_CATERPIE_C.png",
        },
    },
    {
        "id": "P-A-5",
        "name": "Poké Ball",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_90_000030_00_MONSTERBALL_C.png",
        },
    },
    {
        "id": "A1-6",
        "name": "Metapod",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000060_00_TRANSEL_C.png",
        },
    },
    {
        "id": "A1a-006",
        "name": "Serperior",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_006_EN.webp",
        },
    },
    {
        "id": "P-A-6",
        "name": "Red Card",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_90_000070_00_REDCARD_C.png",
        },
    },
    {
        "id": "P-A-7",
        "name": "Professor’s Research",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_90_000040_00_HAKASENOKENKYU_C.png",
        },
    },
    {
        "id": "A1a-007",
        "name": "Morelull",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_007_EN.webp",
        },
    },
    {
        "id": "A1-7",
        "name": "Butterfree",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000070_00_BUTTERFREE_R.png",
        },
    },
    {
        "id": "A1a-008",
        "name": "Shiinotic",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_008_EN.webp",
        },
    },
    {
        "id": "A1-8",
        "name": "Weedle",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000080_00_BEEDLE_C.png",
        },
    },
    {
        "id": "A1-9",
        "name": "Kakuna",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000090_00_COCOON_C.png",
        },
    },
    {
        "id": "A1a-009",
        "name": "Dhelmise",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_009_EN.webp",
        },
    },
    {
        "id": "P-A-9",
        "name": "Pikachu",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_000940_02_PIKACHU_AR.png",
        },
    },
    {
        "id": "A1a-010",
        "name": "Ponyta",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_010_EN.webp",
        },
    },
    {
        "id": "A1-10",
        "name": "Beedrill",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000100_00_SPEAR_R.png",
        },
    },
    {
        "id": "P-A-10",
        "name": "Mewtwo",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_001280_00_MEWTWO_AR.png",
        },
    },
    {
        "id": "A1a-011",
        "name": "Rapidash",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_011_EN.webp",
        },
    },
    {
        "id": "A1-11",
        "name": "Oddish",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000110_00_NAZONOKUSA_C.png",
        },
    },
    {
        "id": "P-A-11",
        "name": "Chansey",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_002020_00_LUCKY_R.png",
        },
    },
    {
        "id": "A1a-012",
        "name": "Magmar",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_012_EN.webp",
        },
    },
    {
        "id": "A1-12",
        "name": "Gloom",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000120_00_KUSAIHANA_U.png",
        },
    },
    {
        "id": "P-A-12",
        "name": "Meowth",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_001960_00_NYARTH_R.png",
        },
    },
    {
        "id": "A1a-013",
        "name": "Larvesta",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_013_EN.webp",
        },
    },
    {
        "id": "A1-13",
        "name": "Vileplume",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000130_00_RUFFRESIA_R.png",
        },
    },
    {
        "id": "P-A-13",
        "name": "Butterfree",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_000070_00_BUTTERFREE_R.png",
        },
    },
    {
        "id": "P-A-14",
        "name": "Lapras ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_002760_00_LAPLACEex_RR.png",
        },
    },
    {
        "id": "A1a-014",
        "name": "Volcarona",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_014_EN.webp",
        },
    },
    {
        "id": "A1-14",
        "name": "Paras",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000140_00_PARAS_C.png",
        },
    },
    {
        "id": "P-A-15",
        "name": "Pikachu",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_000940_01_PIKACHU_C.png",
        },
    },
    {
        "id": "A1a-015",
        "name": "Salandit",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_015_EN.webp",
        },
    },
    {
        "id": "A1-15",
        "name": "Parasect",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000150_00_PARASECT_U.png",
        },
    },
    {
        "id": "A1-16",
        "name": "Venonat",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000160_00_KONGPANG_C.png",
        },
    },
    {
        "id": "P-A-16",
        "name": "Clefairy",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_001130_00_PIPPI_C.png",
        },
    },
    {
        "id": "A1a-016",
        "name": "Salazzle",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_016_EN.webp",
        },
    },
    {
        "id": "P-A-17",
        "name": "Mankey",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_002770_00_MANKEY_C.png",
        },
    },
    {
        "id": "A1-17",
        "name": "Venomoth",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000170_00_MORPHON_U.png",
        },
    },
    {
        "id": "A1a-017",
        "name": "Magikarp",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_017_EN.webp",
        },
    },
    {
        "id": "P-A-18",
        "name": "Venusaur",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_000030_00_FUSHIGIBANA_AR.png",
        },
    },
    {
        "id": "A1a-018",
        "name": "Gyarados ex",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_018_EN.webp",
        },
    },
    {
        "id": "A1-18",
        "name": "Bellsprout",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000180_00_MADATSUBOMI_C.png",
        },
    },
    {
        "id": "A1-19",
        "name": "Weepinbell",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000190_00_UTSUDON_U.png",
        },
    },
    {
        "id": "A1a-019",
        "name": "Vaporeon",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_019_EN.webp",
        },
    },
    {
        "id": "P-A-19",
        "name": "Greninja",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_000890_00_GEKKOUGA_R.png",
        },
    },
    {
        "id": "A1a-020",
        "name": "Finneon",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_020_EN.webp",
        },
    },
    {
        "id": "A1-20",
        "name": "Victreebel",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000200_00_UTSUBOT_R.png",
        },
    },
    {
        "id": "P-A-20",
        "name": "Haunter",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_002780_00_GHOST_C.png",
        },
    },
    {
        "id": "A1a-021",
        "name": "Lumineon",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_021_EN.webp",
        },
    },
    {
        "id": "A1-21",
        "name": "Exeggcute",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000210_00_TAMATAMA_C.png",
        },
    },
    {
        "id": "P-A-21",
        "name": "Onix",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_001500_00_IWARK_C.png",
        },
    },
    {
        "id": "A1-22",
        "name": "Exeggutor",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000220_00_NASSY_R.png",
        },
    },
    {
        "id": "A1a-022",
        "name": "Chewtle",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_022_EN.webp",
        },
    },
    {
        "id": "P-A-22",
        "name": "Jigglypuff",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_002790_00_PURIN_C.png",
        },
    },
    {
        "id": "P-A-23",
        "name": "Bulbasaur",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_000010_00_FUSHIGIDANE_R.png",
        },
    },
    {
        "id": "A1a-023",
        "name": "Drednaw",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_023_EN.webp",
        },
    },
    {
        "id": "A1-23",
        "name": "Exeggutor ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000230_00_NASSYex_RR.png",
        },
    },
    {
        "id": "A1-24",
        "name": "Tangela",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000240_00_MONJARA_C.png",
        },
    },
    {
        "id": "P-A-24",
        "name": "Magnemite",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_90_000970_00_COIL_R.png",
        },
    },
    {
        "id": "A1a-024",
        "name": "Cramorant",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_024_EN.webp",
        },
    },
    {
        "id": "A1a-025",
        "name": "Pikachu",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_025_EN.webp",
        },
    },
    {
        "id": "A1-25",
        "name": "Scyther",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000250_00_STRIKE_C.png",
        },
    },
    {
        "id": "A1-26",
        "name": "Pinsir",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000260_00_KAILIOS_U.png",
        },
    },
    {
        "id": "A1a-026",
        "name": "Raichu",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_026_EN.webp",
        },
    },
    {
        "id": "PROMO-027",
        "name": "Snivy",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/P-A/P-A_027_EN.webp",
        },
    },
    {
        "id": "A1a-027",
        "name": "Electabuzz",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_027_EN.webp",
        },
    },
    {
        "id": "A1-27",
        "name": "Cottonee",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000270_00_MONMEN_C.png",
        },
    },
    {
        "id": "PROMO-028",
        "name": "Volcarona",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/P-A/P-A_028_EN.webp",
        },
    },
    {
        "id": "A1a-028",
        "name": "Joltik",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_028_EN.webp",
        },
    },
    {
        "id": "A1-28",
        "name": "Whimsicott",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000280_00_ELFUUN_U.png",
        },
    },
    {
        "id": "A1-29",
        "name": "Petilil",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000290_00_CHURINE_C.png",
        },
    },
    {
        "id": "A1a-029",
        "name": "Galvantula",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_029_EN.webp",
        },
    },
    {
        "id": "PROMO-029",
        "name": "Blastoise",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/P-A/P-A_029_EN.webp",
        },
    },
    {
        "id": "PROMO-030",
        "name": "Eevee",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/P-A/P-A_030_EN.webp",
        },
    },
    {
        "id": "A1a-030",
        "name": "Dedenne",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_030_EN.webp",
        },
    },
    {
        "id": "A1-30",
        "name": "Lilligant",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000300_00_DREDEAR_U.png",
        },
    },
    {
        "id": "A1a-031",
        "name": "Mew",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_031_EN.webp",
        },
    },
    {
        "id": "A1-31",
        "name": "Skiddo",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000310_00_MEECLE_C.png",
        },
    },
    {
        "id": "PROMO-031",
        "name": "Cinccino",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/P-A/P-A_031_EN.webp",
        },
    },
    {
        "id": "PROMO-032",
        "name": "Charmander",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/P-A/P-A_032_EN.webp",
        },
    },
    {
        "id": "A1a-032",
        "name": "Mew ex",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_032_EN.webp",
        },
    },
    {
        "id": "A1-32",
        "name": "Gogoat",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000320_00_GOGOAT_C.png",
        },
    },
    {
        "id": "A1a-033",
        "name": "Sigilyph",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_033_EN.webp",
        },
    },
    {
        "id": "PROMO-033",
        "name": "Squirtle",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/P-A/P-A_033_EN.webp",
        },
    },
    {
        "id": "A1-33",
        "name": "Charmander",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000330_00_HITOKAGE_C.png",
        },
    },
    {
        "id": "A1a-034",
        "name": "Elgyem",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_034_EN.webp",
        },
    },
    {
        "id": "A1-34",
        "name": "Charmeleon",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000340_00_LIZARDO_U.png",
        },
    },
    {
        "id": "A1a-035",
        "name": "Beheeyem",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_035_EN.webp",
        },
    },
    {
        "id": "A1-35",
        "name": "Charizard",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000350_00_LIZARDON_R.png",
        },
    },
    {
        "id": "A1a-036",
        "name": "Flabébé",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_036_EN.webp",
        },
    },
    {
        "id": "A1-36",
        "name": "Charizard ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000360_00_LIZARDONex_RR.png",
        },
    },
    {
        "id": "A1a-037",
        "name": "Floette",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_037_EN.webp",
        },
    },
    {
        "id": "A1-37",
        "name": "Vulpix",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000370_00_ROKON_C.png",
        },
    },
    {
        "id": "A1a-038",
        "name": "Florges",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_038_EN.webp",
        },
    },
    {
        "id": "A1-38",
        "name": "Ninetales",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000380_00_KYUKON_U.png",
        },
    },
    {
        "id": "A1-39",
        "name": "Growlithe",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000390_00_GARDIE_C.png",
        },
    },
    {
        "id": "A1a-039",
        "name": "Swirlix",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_039_EN.webp",
        },
    },
    {
        "id": "A1a-040",
        "name": "Slurpuff",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_040_EN.webp",
        },
    },
    {
        "id": "A1-40",
        "name": "Arcanine",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000400_00_WINDIE_R.png",
        },
    },
    {
        "id": "A1a-041",
        "name": "Mankey",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_041_EN.webp",
        },
    },
    {
        "id": "A1-41",
        "name": "Arcanine ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000410_00_WINDIEex_RR.png",
        },
    },
    {
        "id": "A1-42",
        "name": "Ponyta",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000420_00_PONYTA_C.png",
        },
    },
    {
        "id": "A1a-042",
        "name": "Primeape",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_042_EN.webp",
        },
    },
    {
        "id": "A1-43",
        "name": "Rapidash",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000430_00_GALLOP_U.png",
        },
    },
    {
        "id": "A1a-043",
        "name": "Geodude",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_043_EN.webp",
        },
    },
    {
        "id": "A1a-044",
        "name": "Graveler",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_044_EN.webp",
        },
    },
    {
        "id": "A1-44",
        "name": "Magmar",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000440_00_BOOBER_C.png",
        },
    },
    {
        "id": "A1-45",
        "name": "Flareon",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000450_00_BOOSTER_R.png",
        },
    },
    {
        "id": "A1a-045",
        "name": "Golem",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_045_EN.webp",
        },
    },
    {
        "id": "A1a-046",
        "name": "Aerodactyl ex",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_046_EN.webp",
        },
    },
    {
        "id": "A1-46",
        "name": "Moltres",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000460_00_FIRE_R.png",
        },
    },
    {
        "id": "A1-47",
        "name": "Moltres ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000470_00_FIREex_RR.png",
        },
    },
    {
        "id": "A1a-047",
        "name": "Marshadow",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_047_EN.webp",
        },
    },
    {
        "id": "A1-48",
        "name": "Heatmor",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000480_00_KUITARAN_C.png",
        },
    },
    {
        "id": "A1a-048",
        "name": "Stonjourner",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_048_EN.webp",
        },
    },
    {
        "id": "A1-49",
        "name": "Salandit",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000490_00_YATOUMORI_C.png",
        },
    },
    {
        "id": "A1a-049",
        "name": "Koffing",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_049_EN.webp",
        },
    },
    {
        "id": "A1-50",
        "name": "Salazzle",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000500_00_ENNEWT_C.png",
        },
    },
    {
        "id": "A1a-050",
        "name": "Weezing",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_050_EN.webp",
        },
    },
    {
        "id": "A1-51",
        "name": "Sizzlipede",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000510_00_YAKUDE_C.png",
        },
    },
    {
        "id": "A1a-051",
        "name": "Purrloin",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_051_EN.webp",
        },
    },
    {
        "id": "A1a-052",
        "name": "Liepard",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_052_EN.webp",
        },
    },
    {
        "id": "A1-52",
        "name": "Centiskorch",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000520_00_MARUYAKUDE_U.png",
        },
    },
    {
        "id": "A1-53",
        "name": "Squirtle",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000530_00_ZENIGAME_C.png",
        },
    },
    {
        "id": "A1a-053",
        "name": "Venipede",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_053_EN.webp",
        },
    },
    {
        "id": "A1a-054",
        "name": "Whirlipede",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_054_EN.webp",
        },
    },
    {
        "id": "A1-54",
        "name": "Wartortle",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000540_00_KAMEIL_U.png",
        },
    },
    {
        "id": "A1a-055",
        "name": "Scolipede",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_055_EN.webp",
        },
    },
    {
        "id": "A1-55",
        "name": "Blastoise",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000550_00_KAMEX_R.png",
        },
    },
    {
        "id": "A1-56",
        "name": "Blastoise ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000560_00_KAMEXex_RR.png",
        },
    },
    {
        "id": "A1a-056",
        "name": "Druddigon",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_056_EN.webp",
        },
    },
    {
        "id": "A1-57",
        "name": "Psyduck",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000570_00_KODUCK_C.png",
        },
    },
    {
        "id": "A1a-057",
        "name": "Pidgey",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_057_EN.webp",
        },
    },
    {
        "id": "A1-58",
        "name": "Golduck",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000580_00_GOLDUCK_U.png",
        },
    },
    {
        "id": "A1a-058",
        "name": "Pidgeotto",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_058_EN.webp",
        },
    },
    {
        "id": "A1a-059",
        "name": "Pidgeot ex",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_059_EN.webp",
        },
    },
    {
        "id": "A1-59",
        "name": "Poliwag",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000590_00_NYOROMO_C.png",
        },
    },
    {
        "id": "A1a-060",
        "name": "Tauros",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_060_EN.webp",
        },
    },
    {
        "id": "A1-60",
        "name": "Poliwhirl",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000600_00_NYOROZO_U.png",
        },
    },
    {
        "id": "A1-61",
        "name": "Poliwrath",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000610_00_NYOROBON_R.png",
        },
    },
    {
        "id": "A1a-061",
        "name": "Eevee",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_061_EN.webp",
        },
    },
    {
        "id": "A1a-062",
        "name": "Chatot",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_062_EN.webp",
        },
    },
    {
        "id": "A1-62",
        "name": "Tentacool",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000620_00_MENOKURAGE_C.png",
        },
    },
    {
        "id": "A1-63",
        "name": "Tentacruel",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000630_00_DOKUKURAGE_U.png",
        },
    },
    {
        "id": "A1a-063",
        "name": "Old Amber",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_063_EN.webp",
        },
    },
    {
        "id": "A1-64",
        "name": "Seel",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000640_00_PAWOU_C.png",
        },
    },
    {
        "id": "A1a-064",
        "name": "Pokémon Flute",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_064_EN.webp",
        },
    },
    {
        "id": "A1-65",
        "name": "Dewgong",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000650_00_JUGON_U.png",
        },
    },
    {
        "id": "A1a-065",
        "name": "Mythical Slab",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_065_EN.webp",
        },
    },
    {
        "id": "A1a-066",
        "name": "Budding Expeditioner",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_066_EN.webp",
        },
    },
    {
        "id": "A1-66",
        "name": "Shellder",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000660_00_SHELLDER_C.png",
        },
    },
    {
        "id": "A1a-067",
        "name": "Blue",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_067_EN.webp",
        },
    },
    {
        "id": "A1-67",
        "name": "Cloyster",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000670_00_PARSHEN_U.png",
        },
    },
    {
        "id": "A1a-068",
        "name": "Leaf",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_068_EN.webp",
        },
    },
    {
        "id": "A1-68",
        "name": "Krabby",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000680_00_CRAB_C.png",
        },
    },
    {
        "id": "A1-69",
        "name": "Kingler",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000690_00_KINGLER_U.png",
        },
    },
    {
        "id": "A1a-069",
        "name": "Exeggutor",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_069_EN.webp",
        },
    },
    {
        "id": "A1a-070",
        "name": "Serperior",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_070_EN.webp",
        },
    },
    {
        "id": "A1-70",
        "name": "Horsea",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000700_00_TATTU_C.png",
        },
    },
    {
        "id": "A1a-071",
        "name": "Salandit",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_071_EN.webp",
        },
    },
    {
        "id": "A1-71",
        "name": "Seadra",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000710_00_SEADRA_U.png",
        },
    },
    {
        "id": "A1-72",
        "name": "Goldeen",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000720_00_TOSAKINTO_C.png",
        },
    },
    {
        "id": "A1a-072",
        "name": "Vaporeon",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_072_EN.webp",
        },
    },
    {
        "id": "A1a-073",
        "name": "Dedenne",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_073_EN.webp",
        },
    },
    {
        "id": "A1-73",
        "name": "Seaking",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000730_00_AZUMAO_C.png",
        },
    },
    {
        "id": "A1a-074",
        "name": "Marshadow",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_074_EN.webp",
        },
    },
    {
        "id": "A1-74",
        "name": "Staryu",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000740_00_HITODEMAN_C.png",
        },
    },
    {
        "id": "A1-75",
        "name": "Starmie",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000750_00_STARMIE_U.png",
        },
    },
    {
        "id": "A1a-075",
        "name": "Celebi ex",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_075_EN.webp",
        },
    },
    {
        "id": "A1-76",
        "name": "Starmie ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000760_00_STARMIEex_RR.png",
        },
    },
    {
        "id": "A1a-076",
        "name": "Gyarados ex",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_076_EN.webp",
        },
    },
    {
        "id": "A1a-077",
        "name": "Mew ex",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_077_EN.webp",
        },
    },
    {
        "id": "A1-77",
        "name": "Magikarp",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000770_00_KOIKING_C.png",
        },
    },
    {
        "id": "A1a-078",
        "name": "Aerodactyl ex",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_078_EN.webp",
        },
    },
    {
        "id": "A1-78",
        "name": "Gyarados",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000780_00_GYARADOS_R.png",
        },
    },
    {
        "id": "A1-79",
        "name": "Lapras",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000790_00_LAPLACE_R.png",
        },
    },
    {
        "id": "A1a-079",
        "name": "Pidgeot ex",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_079_EN.webp",
        },
    },
    {
        "id": "A1-80",
        "name": "Vaporeon",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000800_00_SHOWERS_R.png",
        },
    },
    {
        "id": "A1a-080",
        "name": "Budding Expeditioner",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_080_EN.webp",
        },
    },
    {
        "id": "A1a-081",
        "name": "Blue",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_081_EN.webp",
        },
    },
    {
        "id": "A1-81",
        "name": "Omanyte",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000810_00_OMNITE_U.png",
        },
    },
    {
        "id": "A1-82",
        "name": "Omastar",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000820_00_OMSTAR_R.png",
        },
    },
    {
        "id": "A1a-082",
        "name": "Leaf",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_082_EN.webp",
        },
    },
    {
        "id": "A1-83",
        "name": "Articuno",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000830_00_FREEZER_R.png",
        },
    },
    {
        "id": "A1a-083",
        "name": "Mew ex",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_083_EN.webp",
        },
    },
    {
        "id": "A1a-084",
        "name": "Aerodactyl ex",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_084_EN.webp",
        },
    },
    {
        "id": "A1-84",
        "name": "Articuno ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000840_00_FREEZERex_RR.png",
        },
    },
    {
        "id": "A1-85",
        "name": "Ducklett",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000850_00_KOARUHIE_C.png",
        },
    },
    {
        "id": "A1a-085",
        "name": "Celebi ex",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_085_EN.webp",
        },
    },
    {
        "id": "A1-86",
        "name": "Swanna",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000860_00_SWANNA_U.png",
        },
    },
    {
        "id": "A1a-086",
        "name": "Mew ex",
        "cardImages": {
            "small": "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/pocket/A1a/A1a_086_EN.webp",
        },
    },
    {
        "id": "A1-87",
        "name": "Froakie",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000870_00_KEROMATSU_C.png",
        },
    },
    {
        "id": "A1-88",
        "name": "Frogadier",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000880_00_GEKOGASHIRA_U.png",
        },
    },
    {
        "id": "A1-89",
        "name": "Greninja",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000890_00_GEKKOUGA_R.png",
        },
    },
    {
        "id": "A1-90",
        "name": "Pyukumuku",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000900_00_NAMAKOBUSHI_C.png",
        },
    },
    {
        "id": "A1-91",
        "name": "Bruxish",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000910_00_HAGIGISHIRI_U.png",
        },
    },
    {
        "id": "A1-92",
        "name": "Snom",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000920_00_YUKIHAMI_C.png",
        },
    },
    {
        "id": "A1-93",
        "name": "Frosmoth",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000930_00_MOTHNOW_U.png",
        },
    },
    {
        "id": "A1-94",
        "name": "Pikachu",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000940_00_PIKACHU_C.png",
        },
    },
    {
        "id": "A1-95",
        "name": "Raichu",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000950_00_RAICHU_R.png",
        },
    },
    {
        "id": "A1-96",
        "name": "Pikachu ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000960_00_PIKACHUex_RR.png",
        },
    },
    {
        "id": "A1-97",
        "name": "Magnemite",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000970_00_COIL_C.png",
        },
    },
    {
        "id": "A1-98",
        "name": "Magneton",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000980_00_RARECOIL_R.png",
        },
    },
    {
        "id": "A1-99",
        "name": "Voltorb",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_000990_00_BIRIRIDAMA_C.png",
        },
    },
    {
        "id": "A1-100",
        "name": "Electrode",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001000_00_MARUMINE_U.png",
        },
    },
    {
        "id": "A1-101",
        "name": "Electabuzz",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001010_00_ELEBOO_C.png",
        },
    },
    {
        "id": "A1-102",
        "name": "Jolteon",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001020_00_THUNDERS_R.png",
        },
    },
    {
        "id": "A1-103",
        "name": "Zapdos",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001030_00_THUNDER_R.png",
        },
    },
    {
        "id": "A1-104",
        "name": "Zapdos ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001040_00_THUNDERex_RR.png",
        },
    },
    {
        "id": "A1-105",
        "name": "Blitzle",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001050_00_SHIMAMA_C.png",
        },
    },
    {
        "id": "A1-106",
        "name": "Zebstrika",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001060_00_ZEBRAIKA_U.png",
        },
    },
    {
        "id": "A1-107",
        "name": "Tynamo",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001070_00_SHIBISHIRASU_C.png",
        },
    },
    {
        "id": "A1-108",
        "name": "Eelektrik",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001080_00_SHIBIBEEL_U.png",
        },
    },
    {
        "id": "A1-109",
        "name": "Eelektross",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001090_00_SHIBIRUDON_R.png",
        },
    },
    {
        "id": "A1-110",
        "name": "Helioptile",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001100_00_ERIKITERU_C.png",
        },
    },
    {
        "id": "A1-111",
        "name": "Heliolisk",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001110_00_ELEZARD_C.png",
        },
    },
    {
        "id": "A1-112",
        "name": "Pincurchin",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001120_00_BACHINUNI_U.png",
        },
    },
    {
        "id": "A1-113",
        "name": "Clefairy",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001130_00_PIPPI_C.png",
        },
    },
    {
        "id": "A1-114",
        "name": "Clefable",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001140_00_PIXY_U.png",
        },
    },
    {
        "id": "A1-115",
        "name": "Abra",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001150_00_CASEY_C.png",
        },
    },
    {
        "id": "A1-116",
        "name": "Kadabra",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001160_00_YUNGERER_U.png",
        },
    },
    {
        "id": "A1-117",
        "name": "Alakazam",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001170_00_FOODIN_R.png",
        },
    },
    {
        "id": "A1-118",
        "name": "Slowpoke",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001180_00_YADON_C.png",
        },
    },
    {
        "id": "A1-119",
        "name": "Slowbro",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001190_00_YADORAN_U.png",
        },
    },
    {
        "id": "A1-120",
        "name": "Gastly",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001200_00_GHOS_C.png",
        },
    },
    {
        "id": "A1-121",
        "name": "Haunter",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001210_00_GHOST_U.png",
        },
    },
    {
        "id": "A1-122",
        "name": "Gengar",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001220_00_GANGAR_R.png",
        },
    },
    {
        "id": "A1-123",
        "name": "Gengar ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001230_00_GANGARex_RR.png",
        },
    },
    {
        "id": "A1-124",
        "name": "Drowzee",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001240_00_SLEEPE_C.png",
        },
    },
    {
        "id": "A1-125",
        "name": "Hypno",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001250_00_SLEEPER_R.png",
        },
    },
    {
        "id": "A1-126",
        "name": "Mr. Mime",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001260_00_BARRIERD_U.png",
        },
    },
    {
        "id": "A1-127",
        "name": "Jynx",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001270_00_ROUGELA_C.png",
        },
    },
    {
        "id": "A1-128",
        "name": "Mewtwo",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001280_00_MEWTWO_R.png",
        },
    },
    {
        "id": "A1-129",
        "name": "Mewtwo ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001290_00_MEWTWOex_RR.png",
        },
    },
    {
        "id": "A1-130",
        "name": "Ralts",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001300_00_RALTS_C.png",
        },
    },
    {
        "id": "A1-131",
        "name": "Kirlia",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001310_00_KIRLIA_U.png",
        },
    },
    {
        "id": "A1-132",
        "name": "Gardevoir",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001320_00_SIRNIGHT_R.png",
        },
    },
    {
        "id": "A1-133",
        "name": "Woobat",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001330_00_KOROMORI_C.png",
        },
    },
    {
        "id": "A1-134",
        "name": "Swoobat",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001340_00_KOKOROMORI_C.png",
        },
    },
    {
        "id": "A1-135",
        "name": "Golett",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001350_00_GOBIT_C.png",
        },
    },
    {
        "id": "A1-136",
        "name": "Golurk",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001360_00_GOLOOG_U.png",
        },
    },
    {
        "id": "A1-137",
        "name": "Sandshrew",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001370_00_SAND_C.png",
        },
    },
    {
        "id": "A1-138",
        "name": "Sandslash",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001380_00_SANDPAN_U.png",
        },
    },
    {
        "id": "A1-139",
        "name": "Diglett",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001390_00_DIGDA_C.png",
        },
    },
    {
        "id": "A1-140",
        "name": "Dugtrio",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001400_00_DUGTRIO_U.png",
        },
    },
    {
        "id": "A1-141",
        "name": "Mankey",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001410_00_MANKEY_C.png",
        },
    },
    {
        "id": "A1-142",
        "name": "Primeape",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001420_00_OKORIZARU_U.png",
        },
    },
    {
        "id": "A1-143",
        "name": "Machop",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001430_00_WANRIKY_C.png",
        },
    },
    {
        "id": "A1-144",
        "name": "Machoke",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001440_00_GORIKY_U.png",
        },
    },
    {
        "id": "A1-145",
        "name": "Machamp",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001450_00_KAIRIKY_R.png",
        },
    },
    {
        "id": "A1-146",
        "name": "Machamp ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001460_00_KAIRIKYex_RR.png",
        },
    },
    {
        "id": "A1-147",
        "name": "Geodude",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001470_00_ISITSUBUTE_C.png",
        },
    },
    {
        "id": "A1-148",
        "name": "Graveler",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001480_00_GOLONE_U.png",
        },
    },
    {
        "id": "A1-149",
        "name": "Golem",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001490_00_GOLONYA_R.png",
        },
    },
    {
        "id": "A1-150",
        "name": "Onix",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001500_00_IWARK_U.png",
        },
    },
    {
        "id": "A1-151",
        "name": "Cubone",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001510_00_KARAKARA_C.png",
        },
    },
    {
        "id": "A1-152",
        "name": "Marowak",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001520_00_GARAGARA_U.png",
        },
    },
    {
        "id": "A1-153",
        "name": "Marowak ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001530_00_GARAGARAex_RR.png",
        },
    },
    {
        "id": "A1-154",
        "name": "Hitmonlee",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001540_00_SAWAMULAR_C.png",
        },
    },
    {
        "id": "A1-155",
        "name": "Hitmonchan",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001550_00_EBIWALAR_C.png",
        },
    },
    {
        "id": "A1-156",
        "name": "Rhyhorn",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001560_00_SIHORN_C.png",
        },
    },
    {
        "id": "A1-157",
        "name": "Rhydon",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001570_00_SIDON_U.png",
        },
    },
    {
        "id": "A1-158",
        "name": "Kabuto",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001580_00_KABUTO_U.png",
        },
    },
    {
        "id": "A1-159",
        "name": "Kabutops",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001590_00_KABUTOPS_R.png",
        },
    },
    {
        "id": "A1-160",
        "name": "Mienfoo",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001600_00_KOJOFU_C.png",
        },
    },
    {
        "id": "A1-161",
        "name": "Mienshao",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001610_00_KOJONDO_U.png",
        },
    },
    {
        "id": "A1-162",
        "name": "Clobbopus",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001620_00_TATAKKO_C.png",
        },
    },
    {
        "id": "A1-163",
        "name": "Grapploct",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001630_00_OTOSUPUS_U.png",
        },
    },
    {
        "id": "A1-164",
        "name": "Ekans",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001640_00_ARBO_C.png",
        },
    },
    {
        "id": "A1-165",
        "name": "Arbok",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001650_00_ARBOK_U.png",
        },
    },
    {
        "id": "A1-166",
        "name": "Nidoran♀",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001660_00_NIDORAN♀_C.png",
        },
    },
    {
        "id": "A1-167",
        "name": "Nidorina",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001670_00_NIDORINA_U.png",
        },
    },
    {
        "id": "A1-168",
        "name": "Nidoqueen",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001680_00_NIDOQUEEN_R.png",
        },
    },
    {
        "id": "A1-169",
        "name": "Nidoran♂",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001690_00_NIDORAN♂_C.png",
        },
    },
    {
        "id": "A1-170",
        "name": "Nidorino",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001700_00_NIDORINO_U.png",
        },
    },
    {
        "id": "A1-171",
        "name": "Nidoking",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001710_00_NIDOKING_R.png",
        },
    },
    {
        "id": "A1-172",
        "name": "Zubat",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001720_00_ZUBAT_C.png",
        },
    },
    {
        "id": "A1-173",
        "name": "Golbat",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001730_00_GOLBAT_U.png",
        },
    },
    {
        "id": "A1-174",
        "name": "Grimer",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001740_00_BETBETER_C.png",
        },
    },
    {
        "id": "A1-175",
        "name": "Muk",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001750_00_BETBETON_R.png",
        },
    },
    {
        "id": "A1-176",
        "name": "Koffing",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001760_00_DOGARS_C.png",
        },
    },
    {
        "id": "A1-177",
        "name": "Weezing",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001770_00_MATADOGAS_R.png",
        },
    },
    {
        "id": "A1-178",
        "name": "Mawile",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001780_00_KUCHEAT_C.png",
        },
    },
    {
        "id": "A1-179",
        "name": "Pawniard",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001790_00_KOMATANA_C.png",
        },
    },
    {
        "id": "A1-180",
        "name": "Bisharp",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001800_00_KIRIKIZAN_U.png",
        },
    },
    {
        "id": "A1-181",
        "name": "Meltan",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001810_00_MELTAN_C.png",
        },
    },
    {
        "id": "A1-182",
        "name": "Melmetal",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001820_00_MELMETAL_R.png",
        },
    },
    {
        "id": "A1-183",
        "name": "Dratini",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001830_00_MINIRYU_C.png",
        },
    },
    {
        "id": "A1-184",
        "name": "Dragonair",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001840_00_HAKURYU_U.png",
        },
    },
    {
        "id": "A1-185",
        "name": "Dragonite",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001850_00_KAIRYU_R.png",
        },
    },
    {
        "id": "A1-186",
        "name": "Pidgey",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001860_00_POPPO_C.png",
        },
    },
    {
        "id": "A1-187",
        "name": "Pidgeotto",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001870_00_PIGEON_C.png",
        },
    },
    {
        "id": "A1-188",
        "name": "Pidgeot",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001880_00_PIGEOT_R.png",
        },
    },
    {
        "id": "A1-189",
        "name": "Rattata",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001890_00_KORATTA_C.png",
        },
    },
    {
        "id": "A1-190",
        "name": "Raticate",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001900_00_RATTA_C.png",
        },
    },
    {
        "id": "A1-191",
        "name": "Spearow",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001910_00_ONISUZUME_C.png",
        },
    },
    {
        "id": "A1-192",
        "name": "Fearow",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001920_00_ONIDRILL_C.png",
        },
    },
    {
        "id": "A1-193",
        "name": "Jigglypuff",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001930_00_PURIN_C.png",
        },
    },
    {
        "id": "A1-194",
        "name": "Wigglytuff",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001940_00_PUKURIN_C.png",
        },
    },
    {
        "id": "A1-195",
        "name": "Wigglytuff ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001950_00_PUKURINex_RR.png",
        },
    },
    {
        "id": "A1-196",
        "name": "Meowth",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001960_00_NYARTH_C.png",
        },
    },
    {
        "id": "A1-197",
        "name": "Persian",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001970_00_PERSIAN_U.png",
        },
    },
    {
        "id": "A1-198",
        "name": "Farfetch’d",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001980_00_KAMONEGI_C.png",
        },
    },
    {
        "id": "A1-199",
        "name": "Doduo",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_001990_00_DODO_C.png",
        },
    },
    {
        "id": "A1-200",
        "name": "Dodrio",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002000_00_DODORIO_U.png",
        },
    },
    {
        "id": "A1-201",
        "name": "Lickitung",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002010_00_BERORINGA_U.png",
        },
    },
    {
        "id": "A1-202",
        "name": "Chansey",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002020_00_LUCKY_U.png",
        },
    },
    {
        "id": "A1-203",
        "name": "Kangaskhan",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002030_00_GARURA_R.png",
        },
    },
    {
        "id": "A1-204",
        "name": "Tauros",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002040_00_KENTAUROS_U.png",
        },
    },
    {
        "id": "A1-205",
        "name": "Ditto",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002050_00_METAMON_R.png",
        },
    },
    {
        "id": "A1-206",
        "name": "Eevee",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002060_00_EIEVUI_C.png",
        },
    },
    {
        "id": "A1-207",
        "name": "Eevee",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002060_01_EIEVUI_C.png",
        },
    },
    {
        "id": "A1-208",
        "name": "Eevee",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002060_02_EIEVUI_C.png",
        },
    },
    {
        "id": "A1-209",
        "name": "Porygon",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002070_00_PORYGON_U.png",
        },
    },
    {
        "id": "A1-210",
        "name": "Aerodactyl",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002080_00_PTERA_R.png",
        },
    },
    {
        "id": "A1-211",
        "name": "Snorlax",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002090_00_KABIGON_R.png",
        },
    },
    {
        "id": "A1-212",
        "name": "Minccino",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002100_00_CHILLARMY_C.png",
        },
    },
    {
        "id": "A1-213",
        "name": "Cinccino",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002110_00_CHILLACCINO_U.png",
        },
    },
    {
        "id": "A1-214",
        "name": "Wooloo",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002120_00_WOOLUU_C.png",
        },
    },
    {
        "id": "A1-215",
        "name": "Dubwool",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_10_002130_00_BAIWOOLUU_C.png",
        },
    },
    {
        "id": "A1-216",
        "name": "Helix Fossil",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_10_000080_00_KAINOKASEKI_C.png",
        },
    },
    {
        "id": "A1-217",
        "name": "Dome Fossil",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_10_000090_00_KOURANOKASEKI_C.png",
        },
    },
    {
        "id": "A1-218",
        "name": "Old Amber",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_10_000100_00_HIMITSUNOKOHAKU_C.png",
        },
    },
    {
        "id": "A1-219",
        "name": "Erika",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_10_000110_00_ERIKA_U.png",
        },
    },
    {
        "id": "A1-220",
        "name": "Misty",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_10_000120_00_KASUMI_U.png",
        },
    },
    {
        "id": "A1-221",
        "name": "Blaine",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_10_000130_00_KATSURA_U.png",
        },
    },
    {
        "id": "A1-222",
        "name": "Koga",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_10_000140_00_KYOU_U.png",
        },
    },
    {
        "id": "A1-223",
        "name": "Giovanni",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_10_000150_00_SAKAKI_U.png",
        },
    },
    {
        "id": "A1-224",
        "name": "Brock",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_10_000160_00_TAKESHI_U.png",
        },
    },
    {
        "id": "A1-225",
        "name": "Sabrina",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_10_000170_00_NATSUME_U.png",
        },
    },
    {
        "id": "A1-226",
        "name": "Lt. Surge",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_10_000180_00_MATISSE_U.png",
        },
    },
    {
        "id": "A1-227",
        "name": "Bulbasaur",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000010_00_FUSHIGIDANE_AR.png",
        },
    },
    {
        "id": "A1-228",
        "name": "Gloom",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000120_00_KUSAIHANA_AR.png",
        },
    },
    {
        "id": "A1-229",
        "name": "Pinsir",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000260_00_KAILIOS_AR.png",
        },
    },
    {
        "id": "A1-230",
        "name": "Charmander",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000330_00_HITOKAGE_AR.png",
        },
    },
    {
        "id": "A1-231",
        "name": "Rapidash",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000430_00_GALLOP_AR.png",
        },
    },
    {
        "id": "A1-232",
        "name": "Squirtle",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000530_00_ZENIGAME_AR.png",
        },
    },
    {
        "id": "A1-233",
        "name": "Gyarados",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000780_00_GYARADOS_AR.png",
        },
    },
    {
        "id": "A1-234",
        "name": "Lapras",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000790_00_LAPLACE_AR.png",
        },
    },
    {
        "id": "A1-235",
        "name": "Electrode",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001000_00_MARUMINE_AR.png",
        },
    },
    {
        "id": "A1-236",
        "name": "Alakazam",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001170_00_FOODIN_AR.png",
        },
    },
    {
        "id": "A1-237",
        "name": "Slowpoke",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001180_00_YADON_AR.png",
        },
    },
    {
        "id": "A1-238",
        "name": "Diglett",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001390_00_DIGDA_AR.png",
        },
    },
    {
        "id": "A1-239",
        "name": "Cubone",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001510_00_KARAKARA_AR.png",
        },
    },
    {
        "id": "A1-240",
        "name": "Nidoqueen",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001680_00_NIDOQUEEN_AR.png",
        },
    },
    {
        "id": "A1-241",
        "name": "Nidoking",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001710_00_NIDOKING_AR.png",
        },
    },
    {
        "id": "A1-242",
        "name": "Golbat",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001730_00_GOLBAT_AR.png",
        },
    },
    {
        "id": "A1-243",
        "name": "Weezing",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001770_00_MATADOGAS_AR.png",
        },
    },
    {
        "id": "A1-244",
        "name": "Dragonite",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001850_00_KAIRYU_AR.png",
        },
    },
    {
        "id": "A1-245",
        "name": "Pidgeot",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001880_00_PIGEOT_AR.png",
        },
    },
    {
        "id": "A1-246",
        "name": "Meowth",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001960_00_NYARTH_AR.png",
        },
    },
    {
        "id": "A1-247",
        "name": "Ditto",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_002050_00_METAMON_AR.png",
        },
    },
    {
        "id": "A1-248",
        "name": "Eevee",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_002060_00_EIEVUI_AR.png",
        },
    },
    {
        "id": "A1-249",
        "name": "Porygon",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_002070_00_PORYGON_AR.png",
        },
    },
    {
        "id": "A1-250",
        "name": "Snorlax",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_002090_00_KABIGON_AR.png",
        },
    },
    {
        "id": "A1-251",
        "name": "Venusaur ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000040_00_FUSHIGIBANAex_SR.png",
        },
    },
    {
        "id": "A1-252",
        "name": "Exeggutor ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000230_00_NASSYex_SR.png",
        },
    },
    {
        "id": "A1-253",
        "name": "Charizard ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000360_00_LIZARDONex_SR.png",
        },
    },
    {
        "id": "A1-254",
        "name": "Arcanine ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000410_00_WINDIEex_SR.png",
        },
    },
    {
        "id": "A1-255",
        "name": "Moltres ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000470_00_FIREex_SR.png",
        },
    },
    {
        "id": "A1-256",
        "name": "Blastoise ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000560_00_KAMEXex_SR.png",
        },
    },
    {
        "id": "A1-257",
        "name": "Starmie ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000760_00_STARMIEex_SR.png",
        },
    },
    {
        "id": "A1-258",
        "name": "Articuno ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000840_00_FREEZERex_SR.png",
        },
    },
    {
        "id": "A1-259",
        "name": "Pikachu ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000960_00_PIKACHUex_SR.png",
        },
    },
    {
        "id": "A1-260",
        "name": "Zapdos ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001040_00_THUNDERex_SR.png",
        },
    },
    {
        "id": "A1-261",
        "name": "Gengar ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001230_00_GANGARex_SR.png",
        },
    },
    {
        "id": "A1-262",
        "name": "Mewtwo ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001290_00_MEWTWOex_SR.png",
        },
    },
    {
        "id": "A1-263",
        "name": "Machamp ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001460_00_KAIRIKYex_SR.png",
        },
    },
    {
        "id": "A1-264",
        "name": "Marowak ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001530_00_GARAGARAex_SR.png",
        },
    },
    {
        "id": "A1-265",
        "name": "Wigglytuff ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001950_00_PUKURINex_SR.png",
        },
    },
    {
        "id": "A1-266",
        "name": "Erika",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_20_000110_00_ERIKA_SR.png",
        },
    },
    {
        "id": "A1-267",
        "name": "Misty",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_20_000120_00_KASUMI_SR.png",
        },
    },
    {
        "id": "A1-268",
        "name": "Blaine",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_20_000130_00_KATSURA_SR.png",
        },
    },
    {
        "id": "A1-269",
        "name": "Koga",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_20_000140_00_KYOU_SR.png",
        },
    },
    {
        "id": "A1-270",
        "name": "Giovanni",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_20_000150_00_SAKAKI_SR.png",
        },
    },
    {
        "id": "A1-271",
        "name": "Brock",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_20_000160_00_TAKESHI_SR.png",
        },
    },
    {
        "id": "A1-272",
        "name": "Sabrina",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_20_000170_00_NATSUME_SR.png",
        },
    },
    {
        "id": "A1-273",
        "name": "Lt. Surge",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cTR_20_000180_00_MATISSE_SR.png",
        },
    },
    {
        "id": "A1-274",
        "name": "Moltres ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000470_01_FIREex_SAR.png",
        },
    },
    {
        "id": "A1-275",
        "name": "Articuno ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000840_01_FREEZERex_SAR.png",
        },
    },
    {
        "id": "A1-276",
        "name": "Zapdos ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001040_01_THUNDERex_SAR.png",
        },
    },
    {
        "id": "A1-277",
        "name": "Gengar ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001230_01_GANGARex_SAR.png",
        },
    },
    {
        "id": "A1-278",
        "name": "Machamp ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001460_01_KAIRIKYex_SAR.png",
        },
    },
    {
        "id": "A1-279",
        "name": "Wigglytuff ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001950_01_PUKURINex_SAR.png",
        },
    },
    {
        "id": "A1-280",
        "name": "Charizard ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000360_01_LIZARDONex_IM.png",
        },
    },
    {
        "id": "A1-281",
        "name": "Pikachu ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000960_01_PIKACHUex_IM.png",
        },
    },
    {
        "id": "A1-282",
        "name": "Mewtwo ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001290_01_MEWTWOex_IM.png",
        },
    },
    {
        "id": "A1-283",
        "name": "Mew",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_002140_00_MEW_IM.png",
        },
    },
    {
        "id": "A1-284",
        "name": "Charizard ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000360_02_LIZARDONex_UR.png",
        },
    },
    {
        "id": "A1-285",
        "name": "Pikachu ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_000960_02_PIKACHUex_UR.png",
        },
    },
    {
        "id": "A1-286",
        "name": "Mewtwo ex",
        "cardImages": {
            "small": "https://s3.amazonaws.com/pocket-game-assets.codex.gg/cards/cPK_20_001290_02_MEWTWOex_UR.png",
        },
    },
]

output_dir = os.path.expanduser("~/Downloads/pokemon_cards")
os.makedirs(output_dir, exist_ok=True)

for c in response:
    try:
        image_url = c["cardImages"]["small"]
        image_name = f"{c['id']}_{c['name']}.png"
        image_path = os.path.join(output_dir, image_name)
        print(f"Downloading {image_url} to {image_path}")

        urllib.request.urlretrieve(image_url, image_path)
        print(f"Successfully downloaded: {image_name}")
    except KeyError as e:
        print(f"Missing key in response data: {e}")
    except Exception as e:
        print(f"Failed to download: {e}")

print("Download complete.")
