from django import forms

class SearchForm(forms.Form):
	ciudad = forms.CharField(max_length=100)
