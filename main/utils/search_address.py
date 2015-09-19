# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from yandex import search_yandex
from google import search_google
from mapservice import search_mapservice


def search_address(address):
    for func in [search_mapservice, search_yandex, search_google]:
        try:
            result = func(address)
            if result:
                return result
        except Exception:
            continue
    return {'is_success': False}
