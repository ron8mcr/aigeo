# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms


class SearchAddressForm(forms.Form):
    address = forms.CharField(label='Адрес',
                              widget=forms.TextInput(attrs={
                                'placeholder': 'Введите адрес',
                                'class': 'form-control input'
                                }))
