# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from lxml.etree import fromstring


class MapServiceApiException(Exception):
    pass


class MapServiceApi(object):
    base_url = 'http://geo.24bpd.ru/services/service.php'
    api = '1.03'

    def __init__(self, ukey='jyclwyom3lwicuz0pf22sznx'):
        self.ukey = ukey
        self.skey = None

    def _make_request(self, params):
        """Сделать запрос к сервису с заданными параметрами
        и вернуть распарсеный xml
        """
        params['api'] = self.api
        response = requests.get(self.base_url, params=params)
        response = fromstring(response.content)
        status_code = int(response.xpath('/response/status/@code').pop())
        if status_code != 1:
            raise MapServiceApiException(response.xpath(
                '/response/status[1]/text()').pop())
        else:
            return response

    def auth(self):
        params = {
            'service': 'auth',
            'ukey': self.ukey,
            'call': 'open'  # ни одного описания этого параметра нет
            }
        response = self._make_request(params)
        self.skey = response.xpath('/response/session/@skey').pop()

    def geocode_simple(self, address, limit=10):
        """
        Простой адресный поиск, использующий только параметр q
        """
        params = {
            'service': 'geocode',
            'skey': self.skey,
            'q': address,
            'limit': limit
        }
        response = self._make_request(params)
        return response.xpath('/response/request/results').pop()
