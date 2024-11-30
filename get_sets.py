import json

from pokemontcgsdk import Card, Set, RestClient

RestClient.configure('e04b950b-6e91-4c21-b820-06fd135d9b8a')

def map_legalities(legalities):
    return {
        "unlimited": legalities.unlimited == "Legal" if hasattr(legalities, "unlimited") else False,
        "expanded": legalities.expanded == "Legal" if hasattr(legalities, "expanded") else False,
        "standard": legalities.standard == "Legal" if hasattr(legalities, "standard") else False
    }

def transform_set(set):
   return {
      "id": set.id,
      "series": set.series,
      "name": set.name,
      "expansionCode": set.ptcgoCode,
      "expansionImages": vars(set.images) if set.images else None,
      "legalities": map_legalities(set.legalities),
      "printedTotal": set.printedTotal,
      "total": set.total,
      "releaseDate": set.releaseDate
   }

def get_all_sets():
  sets = Set.all()
  for s in sets:
    print(f"{s.id}")

def get_sets_by_series(series):
   print(f"Fetching sets from series: {series}")
   query = f'series:"{series}"'
   sets = Set.where(q=query)
   return sets

if __name__ == "__main__":
    series = input(f"Enter series name, eg. 'Sword & Shield': ")
    sets = get_sets_by_series(series)
    sets_json = []

    for set in sets:
       transformed_set = transform_set(set)
       set_json = json.dumps(transformed_set, default=lambda o: o.__dict__, indent=4)
       sets_json.append(json.loads(set_json))
    
    output_filename = f"{series.replace(' ', '_')}_expansions.json"
    with open(output_filename, "w") as file:
       json.dump(sets_json, file, indent=4)
      
    print(f"Saved all expansions to {output_filename}")