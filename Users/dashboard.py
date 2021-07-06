from django.shortcuts import render
from django.views.generic import ListView,View,RedirectView,TemplateView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime
from wallet.models import Wallet,Transaction
from .forms import ProfileUpdateForm,CreditCardForm,AccountStatementForm,LoanForm
from wallet.models import Transaction
from django.conf import settings
import time
import warnings




class Dashboard(LoginRequiredMixin,TemplateView) :
    template_name = 'dashboard.html'

    def get_context_data(self,*args,**kwargs) :
        ctx = super(Dashboard,self).get_context_data(*args,**kwargs)  
        if 'wthl' in self.request.GET : 
            ctx['redirect_message'] = "Your withdrawal request was successful"
        elif 'dpt' in self.request.GET :
            ctx['redirect_message'] = "Your deposit has been acknowledged,awaiting approval." 
        
        ctx['transaction_history'] = self.request.user.transaction.all()[:6]
        return ctx


    def get(self,request,*args,**kwargs)  :
        if not request.user.is_activated :
            return render(request,"account_not_activated.html",{})
        elif request.user.is_blocked :
            return render(request,"account_blocked.html",{})

        else :
            return render(request,self.template_name,self.get_context_data())               




class AccountStatement(LoginRequiredMixin,View) :
    template_name = 'account_statement_form.html'
    template2 = 'account_statement.html'
    form_class = AccountStatementForm
    model = Transaction

    def get(self,request,*args,**kwargs) :
        if not request.user.is_activated :
            return render(request,"account_not_activated.html",{})  
        elif request.user.is_blocked :
            return render(request,"account_blocked.html",{}) 
        else :
            form = self.form_class
            return render(request,self.template_name,locals())

    def post(self,request,*args,**kwargs) :
        #warnings.filterwarnings('error')
        form = self.form_class(request.POST)

        if form.is_valid() :
            start = form.cleaned_data['start'] 
            #start = datetime.combine(start,datetime.min.time(),)
            #start = timezone.make_aware(start,timezone.get_default_timezone())
            end = form.cleaned_data['end']
            #end = datetime.combine(end,datetime.min.time())
            #end = timezone.make_aware(end,timezone.get_default_timezone())
            try :
                if not self.model.objects.filter(date__gte = start,date__lte = end).exists() :
                    time.sleep(1)
                    return JsonResponse({'error' : "Sorry !,This account has no statement available for the specified date range"})
                else :
                    time.sleep(4)
                    return JsonResponse({'success' : "Generated !"})
            except RuntimeWarning :
                time.sleep(4)
                return JsonResponse({'success' : "Generated !"})

     
        else :  
            return JsonResponse({'form_error' : 'The details you entered is invalid,please crosscheck'})


class RequestCreditCard(LoginRequiredMixin,View) :
    template_name = 'request_credit_card.html'
    form_class = CreditCardForm

    def get(self,request,*args,**kwargs) :
        if not request.user.is_activated :
            return render(request,"account_not_activated.html",{})  
        elif request.user.is_blocked :
            return render(request,"account_blocked.html",{}) 
        else :
            form = self.form_class
            return render(request,self.template_name,locals())


    def post(self,request,*args,**kwargs) :
        form = self.form_class(request.POST)
        if form.is_valid() :
            if not request.user.dashboard.applied_for_card :
                request.user.dashboard.applied_for_card = True
                request.user.dashboard.save()
                return JsonResponse({'success' : 'Your request was placed successfully and has been placed for processing ,You will be notified once its complete'})
            else :
                return JsonResponse({'error' : 'You already have a pending request, which is still in process please exercise some patience.'})    
            
        else :
            return JsonResponse({'form_error' : 'details failed validation'})    




class LoanApply(LoginRequiredMixin,View) :
    template_name = 'apply_loan.html'
    form_class = LoanForm

    def get(self,request,*args,**kwargs) :
        if not request.user.is_activated :
            return render(request,"account_not_activated.html",{})  
        elif request.user.is_blocked :
            return render(request,"account_blocked.html",{}) 
        else :
            form = self.form_class
            return render(request,self.template_name,locals())


    def post(self,request,*args,**kwargs) :
        form = self.form_class(request.POST)
        if form.is_valid() :
            if not request.user.dashboard.applied_for_card :
                request.user.dashboard.applied_for_loan = True
                request.user.dashboard.save()
                return JsonResponse({'success' : 'Your request was placed successfully and has been placed for processing ,You will be notified once its complete'})
            else :
                return JsonResponse({'error' : 'You already have a pending loan request, which is still in process please exercise some patience.'})    
            
        else :
            return JsonResponse({'form_error' : 'details failed validation'})






class TransactionHistory(LoginRequiredMixin,TemplateView) :
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
        instance = model_to_dict(request.user)  
        instance['country'] = request.user.country.name      
        form = self.form_class(initial = instance)
        form.instance.country = request.user.country
        return render(request,self.template_name,locals())

