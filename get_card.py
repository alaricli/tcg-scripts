from pokemontcgsdk import Card, RestClient

RestClient.configure('e04b950b-6e91-4c21-b820-06fd135d9b8a')

def get_card(card_id):
  try:
    card = Card.find(card_id)
    return card
  except Exception as e:
    return f"An error occured: {e}"

if __name__ == "__main__":
  card_id = input("enter a card id, eg:'xy1-1': ")
  card = get_card(card_id)
  
  print(card)