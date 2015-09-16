# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url
from main.views import SearchAddressView


urlpatterns = patterns(
    '',
    url(r'^$', SearchAddressView.as_view(), name='index'),
)
