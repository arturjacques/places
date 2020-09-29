import requests
from time import sleep
import pandas as pd


class Maps:
    def __init__(self, key):
        self.key = key
        self.places = dict()
        self.url_text_search = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
        self.url_details_search = 'https://maps.googleapis.com/maps/api/place/details/json'

    def find_places(self, text, location, radius=50000):
        params = {'query': text,
                  'location': location,
                  'radius': radius,
                  'key': self.key}

        place = dict()

        resp = requests.get(self.url_text_search, params=params)
        resp_json = resp.json()
        next_page = True

        while next_page:
            for store in resp_json['results']:
                place['business_status'] = store['business_status']
                place['formatted_address'] = store['formatted_address']
                place['location'] = store['geometry']['location']
                place['rating'] = store['rating']
                place['name'] = store['name']

                self.places[store['place_id']] = place.copy()
                place.clear()

            next_page = 'next_page_token' in resp_json.keys()
            if next_page:
                params['pagetoken'] = resp_json['next_page_token']
                status = 'INVALID_REQUEST'
                while status == 'INVALID_REQUEST':
                    sleep(0.5)
                    resp = requests.get(self.url_text_search, params=params)
                    resp_json = resp.json()
                    status = resp.json()['status']

        return self.places

    def more_information_places(self):
        params_store = {'key': self.key,
                        'fields': 'rating,formatted_phone_number,formatted_address,business_status,type,url,type,user_ratings_total'}

        for place_id in self.places.keys():
            if 'formatted_phone_number' not in self.places[place_id]:
                params_store['placeid'] = place_id
                resp = requests.get(self.url_details_search, params=params_store)
                self.places[place_id] = {**resp.json()['result'], **self.places[place_id]}
                self.save_to_csv('places_temp.csv')

    def to_dataframe(self):
        return pd.DataFrame(self.places).T

    def save_to_csv(self, name):
        self.to_dataframe().to_csv(name)

    def read_places_from_csv(self, name):
        self.places = {**self.places,
                       **pd.read_csv(name, index_col='Unnamed: 0').T.to_dict()}

    def city_coordinates(self, city, state='santa catarina', country='brazil'):
        params = {'query': f'{city} {state} {country}',
                  'radius': 50000,
                  'key': self.key}
        resp = requests.get(self.url_text_search, params=params)
        if 'results' in resp.json():
            return resp.json()['results'][0]['geometry']['location']

    def portuguese_dataframe(self, df):
        df['cidade'] = df.formatted_address.apply(find_city)
        df = df.rename({'name': 'nome', 'location': 'coordenadas',
                          'url': 'link_maps', 'rating': 'avaliação',
                          'formatted_phone_number': 'telefone',
                          'formatted_address': 'endereço'}, axis=1)
        df = df.loc[:, ['nome', 'telefone', 'endereço', 'cidade', 'coordenadas', 'link_maps', 'avaliação']]
        return df


def find_city(text):
    list_text = text.split(',')
    if len(list_text)>3:
        return list_text[-3].split(' - ')[0]