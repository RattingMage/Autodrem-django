from django import forms


class SQLImportForm(forms.Form):
    file = forms.FileField()
