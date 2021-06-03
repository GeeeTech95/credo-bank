from core.views import Notification
import datetime
from django.utils import timezone
from .models import Transaction as transaction_model


class Transaction() :
    def __init__(self,user) :
        self.user = user



    def credit(self,amount,user=None)  :
        if not user : user = self.user
        wallet = user.wallet
        wallet.available_balance += amount 
        wallet.save()
        #ensure it added
        return
            

    def debit(self,amount,user=None) :
        if not user : user = self.user
        wallet = user.wallet
        wallet.available_balance -= amount 
        wallet.save()
        #ensure it added
        return

    def external_transfer(self,amount) : 
        try :
            self.debit(amount)
            #send mail
            #send message
            state = 0
        except :
            self.credit(amount)
            state =  "An Error occured"    
        return state




