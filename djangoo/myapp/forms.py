from django import forms
from django.core.exceptions import ValidationError

def check_z(value):
    if value[0].lower != 'z':
        raise forms.ValidationError('name needs z')
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text= forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,
    # validators=[validators.MaxLengthValidator(0)])

       