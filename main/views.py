# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.views.generic import FormView
from django.http import HttpResponse
from main.forms import SearchAddressForm
from main.utils import search_address


class SearchAddressView(FormView):
    template_name = 'search_address.html'
    form_class = SearchAddressForm

    def form_valid(self, form):
        response = search_address(form.cleaned_data['address'])
        return HttpResponse(json.dumps(response))

    def form_invalid(self, form):
        return HttpResponse(json.dumps({'is_success': False}))
