from pokemontcgsdk import Card, RestClient, Set
import json
import unicodedata

RestClient.configure('e04b950b-6e91-4c21-b820-06fd135d9b8a')

def map_legalities(legalities):
    return {
        "unlimited": legalities.unlimited == "Legal" if hasattr(legalities, "unlimited") else False,
        "expanded": legalities.expanded == "Legal" if hasattr(legalities, "expanded") else False,
        "standard": legalities.standard == "Legal" if hasattr(legalities, "standard") else False
    }

def transform_card(card):
    return {
        "name": card.name,
        "hp": int(card.hp) if card.hp else None,
        "retreatCost": card.convertedRetreatCost,
        "artist": card.artist,
        "regulationMark": card.regulationMark,
        "identifier": card.set.id + "-" + card.number,
        "cardNumber": int(card.number) if card.number else None,
        "nationalPokedexNumber": card.nationalPokedexNumbers[0] if card.nationalPokedexNumbers else None,
        "hasRuleBox": bool(card.rules),
        "hasAbility": bool(card.abilities),
        "ability": " ".join(f"{ability.name} {ability.text}" for ability in card.abilities) if card.abilities else None,
        "trainerCardText": card.rules[0] if card.rules else None,
        "rarity": card.rarity,
        "superType": unicodedata.normalize('NFKD', card.supertype).replace('é', 'e'),
        "subTypes": card.subtypes,
        "expansionId": card.set.id if card.set else None,
        "energyTypes": [t for t in card.types] if card.types else [],
        "attackEnergyTypes": list({e for attack in card.attacks for e in attack.cost}) if card.attacks else [],
        "weakness": [w.type for w in card.weaknesses] if card.weaknesses else [],
        "resistance": [r.type for r in card.resistances] if card.resistances else [],
        "rules": card.rules if card.rules else [],
        "cardImages": {
            "small": card.images.small if card.images else None,
            "large": card.images.large if card.images else None,
        },
        "legalities": map_legalities(set.legalities),
        "isMobile": False,
        "attacks": [
            {
                "name": attack.name,
                "text": attack.text,
                "cost": ",".join(c for c in attack.cost),
                "numericalEnergyCost": attack.convertedEnergyCost,
                "damage": attack.damage,
            } for attack in card.attacks
        ] if card.attacks else []
    }

# Function to fetch cards by set
def get_cards_by_set(set_id):
    print(f"Fetching cards from set: {set_id}")
    query = f'set.id:"{set_id}"'
    cards = Card.where(q=query)
    return cards

if __name__ == "__main__":
    set_id = input("Enter set id, eg. sv8 for Surging Sparks: ")
    cards = get_cards_by_set(set_id)
    cards_json = []

    for card in cards:
        # Transform each card before adding it to the JSON list
        transformed_card = transform_card(card)
        card_json = json.dumps(transformed_card, default=lambda o: o.__dict__, indent=4)
        cards_json.append(json.loads(card_json))

    # Save all cards to a single JSON file
    output_filename = f"{set_id}_cards.json"
    with open(output_filename, "w") as file:
        json.dump(cards_json, file, indent=4)

    print(f"Saved all transformed cards to {output_filename}")
