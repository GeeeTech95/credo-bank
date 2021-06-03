from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User
from wallet.models import Currency



class UserCreateForm(UserCreationForm) :
    currency =  forms.ModelChoiceField(queryset=Currency.objects.all(),required=True)
  
    class Meta(UserCreationForm.Meta) :
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','username','email','account_type','country','state','address','phone_number','occupation','passport','date_of_birth')
        
        widgets = {
            'date_of_birth' : forms.TextInput(attrs={'type': 'date'})
        }
        

class ProfileUpdateForm(ModelForm) :
    class Meta() :
        model  = User
        fields = ['first_name','last_name','phone_number','country','occupation']
        widgets = {
            
            'first_name' : forms.TextInput(attrs={'readonly':True}),
            'last_name' : forms.TextInput(attrs={'readonly':True}),
            'phone_number' : forms.TextInput(attrs={'readonly':True}),
            'country' : forms.TextInput(attrs={'readonly':True}),
            'occupation' : forms.TextInput(attrs={'readonly':True}),
            
        }
