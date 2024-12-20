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


names = set()

data = load_json("ripped2.json")
# filtered_data = [d for d in data if (d["dex"] == "A1a" or d["dex"] == "PROMOA3")]

for card in data:
    if card["type"] == "Pokemon":
        names.add(card["name"])

print(names)

# output_file = "ripped2.json"
# with open(output_file, "w") as file:
#     json.dump(filtered_data, file, indent=4)
