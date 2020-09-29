from search.models import Maps
import pandas as pd

cities_dict = pd.read_csv('cities.csv', index_col=0).T.to_dict()
search_words = [
    'pneu'
]


f = open('key.txt', mode='r')
key = f.read()
f.close()

maps = Maps(key)

maps.read_places_from_csv('places.csv')

for word in search_words:
    for city in cities_dict.values():
        maps.find_places(text=word, location=f"{city['lat']},{city['lng']}")

maps.more_information_places()

maps.save_to_csv('places.csv')