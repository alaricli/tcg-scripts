from pokemontcgsdk import Card, Set, RestClient

RestClient.configure('e04b950b-6e91-4c21-b820-06fd135d9b8a')

def get_all_sets():
  sets = Set.all()
  for s in sets:
    print(f"{s.ptcgoCode}")

if __name__ == "__main__":
    print("Fetching all sets...")
    get_all_sets()