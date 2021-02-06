from django import forms

class CreateKriskras(forms.Form):
    tak = forms.CharField(label="tak", max_length=200)