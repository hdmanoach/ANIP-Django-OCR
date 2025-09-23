from django import forms

class OCRForm(forms.Form):
    image = forms.ImageField(label="Image du document (carte/id, etc.)", required=True)
