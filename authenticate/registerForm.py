from django import forms
from authenticate.models import *

class userRegForm(forms.ModelForm):

    class Meta:
        model = RegisterData
        fields=['name','address','password']
        widgets= {
            'name':forms.TextInput(attrs={
                'class':'mt-1 p-2 w-full border rounded'
            }),
            'address':forms.TextInput(attrs={
                'class':'mt-1 p-2 w-full border rounded'
            }),
            'password':forms.PasswordInput(attrs={
                'class':'mt-1 p-2 w-full border rounded'
            }),
        }