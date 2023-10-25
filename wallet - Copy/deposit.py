from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin



class Deposit(LoginRequiredMixin,View) :
    template_name = 'deposit.html'

    def get(self,request,*args,**kwargs) :
        return render(request,self.template_name,{})


    def post(self,request,*args,**kwargs) :
        return 



class Withdraw(LoginRequiredMixin,View) :
    template_name = 'withdraw.html'

    def get(self,request,*args,**kwargs) :
        ctx = {}
        if request.user.wallet.available_balance < 100000 :
            ctx['not_eligible'] = True
        return render(request,self.template_name,ctx)         