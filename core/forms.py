from .models import NewsLaterSubscriber
from django import forms

class SubscribeForm(forms.ModelForm)  :
    
    class Meta() :
        model = NewsLaterSubscriber
        fields = '__all__'

    def clean_email(self)   :
        email = self.cleaned_data['email'] 
        if self.Meta.model.objects.filter(email = email).exists() :
            raise forms.ValidationError("You have already subscribed !")
        return email