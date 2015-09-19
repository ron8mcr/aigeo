# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mapserviceapi import MapServiceApi, MapServiceApiException
import re

# Глобально создаем объект MapServiceApi
# Чтобы не было необходимости авторизовываться перед каждым запросом
mapservice = MapServiceApi('2t392pprlnfn8hgsd250gzl4')


def search_mapservice(address):
    global mapservice
    # В документации не указано, на какое время выдается
    # сессионный ключ, поэтому в случае ошибки выполнения запроса
    # пробуем авторизоваться снова
    try:
        results = mapservice.geocode_simple(address, 1)
    except MapServiceApiException:
        mapservice.auth()
        results = mapservice.geocode_simple(address, 1)

    count = int(results.xpath("@count").pop())
    if count == 0:
        return None
    text = results.xpath('./result/object/address/text[1]/text()').pop()
    geocenter = results.xpath('./result/object/geocenter/text()').pop()
    m = re.search("POINT\((?P<lng>.*?) (?P<lat>.*?)\)", geocenter)
    return {
            'is_success': True,
            'service': 'Енисей-ГИС API',
            'address': text,
            'latlng': {'lat': m.group('lat'),
                       'lng': m.group('lng')}
        }

try:
    mapservice.auth()
except MapServiceApiException:
    # Если авторизация не удалась, не будем делать лишние обращения
    # к сервису
    search_mapservice = lambda address: None
