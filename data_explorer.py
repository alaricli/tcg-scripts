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


def process_item(item, rarities, expansions, series, packs):
    if "rarityName" in item:
        rarities.add(d["rarityName"])
    if "expansionName" in item:
        expansions.add(d["expansionName"])
    if "series" in item:
        series.add(d["series"])
    if "foundInPacks" in item and isinstance(item["foundInPacks"], list):
        for pack in item["foundInPacks"]:
            packs.add(pack)

    if "variants" in item and isinstance(item["variants"], list):
        for v in item["variants"]:
            process_item(v, rarities, expansions, series, packs)


rarities = set()
expansions = set()
series = set()
packs = set()

data1 = load_json("pocket1.json")
data2 = load_json("pocket2.json")
data3 = load_json("pocket3.json")
data4 = load_json("pocket4.json")
data = data1 + data2 + data3 + data4

for d in data:
    process_item(d, rarities, expansions, series, packs)

print(len(data))
print(rarities)
print(expansions)
print(series)
print(packs)

output_file = "pocket.json"
with open(output_file, "w") as file:
    json.dump(data, file, indent=4)

# PACKS
# AN001_0010_00_000 = mewtwo
# AN001_0020_00_000 = charizard
# AN001_0030_00_000 = pikachu
# AP001_0010_00_000 = PROMO A
# AN001_0020_00_000 = charizard
