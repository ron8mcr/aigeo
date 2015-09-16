# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests


def search_yandex(address):
    api_url = 'https://geocode-maps.yandex.ru/1.x/'
    params = {'geocode': address,
              'format': 'json',
              'results': 1
    }
    response = requests.get(api_url, params=params).json()
    collection = response['response']['GeoObjectCollection']
    found = collection['metaDataProperty']['GeocoderResponseMetaData']['found']
    found = int(found)
    if found == 0:
        return None
    obj = collection['featureMember'][0]['GeoObject']
    point_str = obj['Point']['pos']
    lng, lat = point_str.split(' ')
    text = obj['metaDataProperty']['GeocoderMetaData']['text']

    return {
        'is_success': True,
        'service': 'Yandex Maps API',
        'address': text,
        'latlng': {'lat': lat,
                   'lng': lng}
    }
