from pokemontcgsdk import Set, RestClient

RestClient.configure('e04b950b-6e91-4c21-b820-06fd135d9b8a')

def get_set(code):
  print(f"Finding set: {code}")
  try:
    set_data = Set.find(code)
    return set_data
  except Exception as e:
    return f"An error occured: {e}"

if __name__ == "__main__":
  code = input("Enter set code, eg. 'base1': ")
  set_info = get_set(code)
  print(set_info)