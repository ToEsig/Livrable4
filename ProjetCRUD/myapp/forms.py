# forms.py
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Rechercher', max_length=100)
