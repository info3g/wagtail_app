from django import forms

class HomeForm(forms.Form):
    text_json = forms.CharField(label="Enter JSON", widget=forms.Textarea)