from django.shortcuts import render
from django.views.generic import ListView,View,RedirectView,TemplateView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.forms.models import model_to_dict
from wallet.models import Wallet
from .forms import ProfileUpdateForm
from wallet.models import Transaction


class Dashboard(LoginRequiredMixin,TemplateView) :
    template_name = 'dashboard.html'

    def get_context_data(self,*args,**kwargs) :
        ctx = super(Dashboard,self).get_context_data(*args,**kwargs)  
        if 'wthl' in self.request.GET : 
            ctx['redirect_message'] = "Your withdrawal request was successful"
        elif 'dpt' in self.request.GET :
            ctx['redirect_message'] = "Your deposit has been acknowledged,awaiting approval." 
        
        ctx['transaction_history'] = self.request.user.transaction.all()[:5]
        return ctx


    def get(self,request,*args,**kwargs)  :
        if not request.user.is_activated :
            return render(request,"account_not_activated.html",{})
        elif request.user.is_blocked :
            return render(request,"account_blocked.html",{})

        else :
            return render(request,self.template_name,self.get_context_data())               




class AccountStatement() :
    pass



class TransactionHistory(TemplateView) :
    template_name = 'transaction-history.html'
    def get_context_data(self,*args,**kwargs) :
        ctx = super(TransactionHistory,self).get_context_data(*args,**kwargs)  
        ctx['transaction_history'] = self.request.user.transaction.all()
        return ctx

    def get(self,request,*args,**kwargs)  :
        if not request.user.is_activated :
            return render(request,"account_not_activated.html",{})  
        elif request.user.is_blocked :
            return render(request,"account_blocked.html",{}) 
        else :
            return render(request,self.template_name,self.get_context_data())          


class TransactionDetail() :
    pass


class Profile(LoginRequiredMixin,UpdateView) :
    template_name = 'profile.html'
    model = get_user_model()
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('dashboard')
    
    def get_object(self) :
        return self.request.user

    def get(self,request,*args,**kwargs) :
        if not request.user.is_activated :
            return render(request,"account_not_activated.html",{})
        
        if request.user.is_blocked :
            return render(request,"account_blocked.html",{})     
        form = self.form_class(initial = model_to_dict(request.user))
        return render(request,self.template_name,locals())

