# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests


def search_google(address):
    api_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': address,
              'language': 'ru'
    }
    response = requests.get(api_url, params=params).json()
    if not response['results']:
        return None
    obj = response['results'][0]
    return {
        'is_success': True,
        'service': 'Google Maps API',
        'address': obj['formatted_address'],
        'latlng': obj['geometry']['location']
    }
