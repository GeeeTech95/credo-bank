from core.notification import Notification
import datetime
from django.utils import timezone
from djmoney.money import 
from .models import Transaction as transaction_model


class Transaction() :
    def __init__(self,user) :
        self.user = user


    
    def currency_convert(self,amount,_from,_to) :

        """ 
        converts from one currency to another 
        _from and _to should be in currency object
        amount should be in the _from currency"""
        return amount

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

    def external_transfer(self,amount,currency) : 
        amount = self.currency_convert(amount,currency,self.user.wallet.currency)
        try :
            self.debit(amount)
            #send mail
            #send message
            state = 0
        except :
            self.credit(amount)
            state =  "An Error occured"    
        return state

    def internal_transfer(self,receiver,amount,currency) : 
        """
        currency is the receiving account currency"""
        #convert to sending acc curr
        amount = self.currency_convert(amount,currency,receiver.wallet.currency)
        try :
            self.debit(amount)
            self.credit(amount,receiver)
            #send mail
            #send message
            state = 0
        except :
            self.credit(amount,user = self.user)
            self.debit(amount,user = receiver)
            state =  "An Error occured"    
        return state    




