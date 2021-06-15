from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User
from wallet.models import Currency
from core.views import ValidationCode


class UserCreateForm(UserCreationForm) :
    currency =  forms.ModelChoiceField(queryset=Currency.objects.all(),required=True)
  
    class Meta(UserCreationForm.Meta) :
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','username','email','account_type','country','address','phone_number','occupation','passport','date_of_birth')
        
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

class PhoneNumberForm(ModelForm) :
    code = forms.CharField(required=True,help_text="Enter the code sent to you,click resend if you dint get any after some time")
    
    def __init__(self,user=None,*args,**kwargs) :
        self.user = user
        super(PhoneNumberForm,self).__init__(*args,**kwargs)
    
    class Meta() :
        model = User
        fields  = ['phone_number'] 

        widgets = {
            'phone_number' : forms.TextInput(attrs={'id' : "phone_number"}),
        }  

        help_texts = {
            'phone_number' : "We are sending a verification code to this phone number,you can edit it before hitting the send button"
        } 

    def clean_code(self) :
        code = self.cleaned_data['code']  
        validated,error = ValidationCode.validate_otc(self.user,code)
        if not validated :
            raise forms.ValidationError(error)
        return code



class EmailForm(ModelForm) :
    code = forms.CharField(required=True,help_text="Enter the code sent to your email,click resend if you dint get any after some time")
    
    def __init__(self,user=None,*args,**kwargs) :
        self.user = user
        super(EmailForm,self).__init__(*args,**kwargs)
    
    class Meta() :
        model = User
        fields  = ['email'] 

        widgets = {
            'email' : forms.TextInput(attrs={'id' : "email"}),
        }  

        help_texts = {
            'email' : "We are sending a verification code to this email address,you can edit it before hitting the send button"
        } 

    def clean_code(self) :
        code = self.cleaned_data['code']  
        validated,error = ValidationCode.validate_otc(self.user,code)
        if not validated :
            raise forms.ValidationError(error)
        return code        

         

