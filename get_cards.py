from pokemontcgsdk import Card, RestClient
import json

RestClient.configure('e04b950b-6e91-4c21-b820-06fd135d9b8a')

def get_cards_by_set(set_name):
  print(f"Fetching cards from set: {set_name}")
  query = f'set.name:"{set_name}"'
  cards = Card.where(q=query)
  return cards

if __name__ == "__main__":
    set_name = input("Enter the set name: ")
    cards = get_cards_by_set(set_name)

    cards_json = []

    for card in cards:
      card_json = json.dumps(card, default=lambda o: o.__dict__, indent=4)
      cards_json.append(card_json)
    
    print(cards_json)