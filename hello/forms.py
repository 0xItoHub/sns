from django import forms

class HelloForm(forms.Form):
    check = forms.IntegerField(label='ID')