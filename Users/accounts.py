from django.urls import reverse_lazy,reverse
from django.shortcuts import render
from django.views.generic import CreateView,View
from django.views.generic.base  import RedirectView
from django.http import HttpResponseRedirect
from wallet.models import Wallet
from .models import  User
from .forms import UserCreateForm

class Register(CreateView) :
    template_name = 'register.html'
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('login')

    def auto_create_wallet(self,user) :
        Wallet.objects.get_or_create(user = user)
        return

    def post(self,request,*args,**kwargs) :
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid() :
            user  = form.save()
            self.auto_create_wallet(user)
            #send thank you email and message
            #redirect to validate email and phone number 
            return render(request,"just_created.html",{})
        else :
            return render(request,self.template_name,locals())    
        return HttpResponseRedirect(self.success_url)


class LoginRedirect(View)   :
    template_name = 'login_account_blocked.html'
    template_name2 = 'account_not_activated.html'
    
    def get(self,request,*args,**kwargs)  :
        #check if user is prevented from loggin in
        if request.user.is_activated : 
            return HttpResponseRedirect(reverse('dashboard'))
        else :
            return render(request,self.template_name2,locals())




    