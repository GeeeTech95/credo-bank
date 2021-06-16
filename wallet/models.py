from django.db import models
from django.contrib.auth import get_user_model
import random


class Currency(models.Model) :
    name  = models.CharField(max_length=30)
    code = models.CharField(max_length=5)
    symbol = models.CharField(max_length=5)

    def __str__(self) :
        return self.code




class Wallet(models.Model) :
    
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE,related_name = 'wallet')
    transaction_pin = models.CharField(max_length=6,null = False,default="0000")
    #iban_number = models.CharField(max_length=30)
    otp = models.CharField(max_length=8,blank = True,null = True)
    currency = models.ForeignKey(Currency,related_name = 'wallets',on_delete = models.CASCADE,null = False)
    balance = models.FloatField(default = 0.0)
    available_balance = models.FloatField(default = 0.0)
    
    #control spot
    allowed_to_transact = models.BooleanField(default=True)
    #when user is disaaalowed from makimg transactions
    disallow_reason = models.TextField(null = False,blank = True)
    is_frozen  = models.BooleanField(default = False)

    def __str__(self) :
        return self.user.username

    def save(self,*args,**kwargs) :
        if not self.allowed_to_transact :
            pass
            #email user
            #sms user
            #notifiy user
        super(Wallet,self).save(*args,**kwargs)     



class Transaction(models.Model) :
    def get_transaction_id(self) :
        PREFIX = "TD"
        number = random.randrange(10000000,999999999)
        number = PREFIX + str(number)
        if Transaction.objects.filter(transaction_id  = number).exists() : 
            self.get_transaction_id()
        return number

    TRANSACTION_TYPE = (('Debit','Debit'),('Credit','Credit'))
    TRANSACTION_NATURE  = (('Withdrawal','Withdrawal'),
    ('Deposit','Deposit'),
    ('Internal Transfer','Internal Transfer'),
    ('Domestic Transfer','Domestic Transfer'),
    ('International Transfer','International Transfer'))

    STATUS = (('Failed','Failed'),
    ('Processing','Processing'),
    ('Successful',"Successful"))
    
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,
    related_name = 'transaction')
    transaction_id = models.CharField(editable=False,null = False,max_length = 20)
    amount = models.FloatField()
    transaction_type = models.CharField(choices = TRANSACTION_TYPE,max_length= 10)
    nature = models.CharField(choices = TRANSACTION_NATURE,max_length= 32,null = False,blank = False)
    status = models.CharField(choices = STATUS,max_length= 10)
    description = models.TextField(null = True,blank = False)
    
    #if transfer,can be blank for international transfer
    receiver = models.ForeignKey(get_user_model(),related_name = 'transfer_receiver',on_delete = models.CASCADE,null = True,blank = True)
    status_message = models.TextField()
    charge = models.FloatField(blank = True,default=0.0,null = False)

    #for international transfer
    iban = models.CharField(max_length=40,blank = True,null = True)
    bic = models.CharField(max_length=40,blank = True,null = True)
    swift_number = models.CharField(max_length=15,blank = True,null = True)
    account_number = models.CharField(max_length=20,blank = True,null = True)
    account_name  = models.CharField(max_length=20,blank = True,null = True)
    bank_name = models.CharField(max_length=20,blank = True,null = True)
    country =  models.CharField(max_length=20,blank = True,null = True)
    currency = models.ForeignKey(Currency,related_name ='transactions',on_delete = models.SET_NULL,null = True)
    #for controlling transactions
    failure_reason = models.TextField(null = True,blank = True)
    
    date = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs) :
        if not self.transaction_id :
            self.transaction_id = self.get_transaction_id()

        if self.status == 'Failed' :
            #notify user
            #email user
            #sms user
            pass    
        super(Transaction,self).save(*args,**kwargs)   

    def __str__(self) :
        return self.transaction_id

    class Meta() :
        ordering = ['-date']

