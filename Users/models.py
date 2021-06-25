from django.db import models
from django.contrib.auth.models   import AbstractUser
from django.utils.text import  slugify
from django.utils import timezone
from core.views import Messages,Email
import random




class Country(models.Model) :
    name = models.CharField(max_length = 20)
    code = models.CharField(max_length = 5,blank = True)

    def __str__(self) :
        return self.name

    


class User(AbstractUser) :
    
    def get_path(instance,filename) :
        filename = "{}.{}".format(instance.username,filename.split('.')[1])
        return "users/{}/passport/{}".format(instance.username,filename)


    def get_account_number() :
        PREFIX = "67"
        number = random.randrange(10000000,999999999)
        number = PREFIX + str(number)
        if User.objects.filter(account_number  = number).exists() : 
            self.get_account_number()
        return number

    ACCOUNT_TYPE = (('Savings','SAVINGS'),('Current','CURRENT'))    
           
    
    email_verified = models.BooleanField(default=False,blank = True)
    phone_number = models.CharField(max_length = 30,blank = False,null = False)
    phone_number_verified = models.BooleanField(default=False,blank = True)
    occupation = models.CharField(max_length=30)
    date_of_birth = models.DateField(verbose_name="D.O.B",null = True)
    country = models.ForeignKey(Country,on_delete= models.SET_NULL,null = True,blank = True,related_name='users')
    address = models.TextField(null = True)
    account_number  = models.CharField(default=get_account_number,editable=False,null = False,max_length=14,unique=True,blank = True)
    account_type = models.CharField(default="SAVINGS",max_length=10,choices = ACCOUNT_TYPE)
    passport = models.FileField(upload_to = get_path,null = True)
    is_activated = models.BooleanField(default = False,blank = False,null = False)
    date_activated = models.DateTimeField(null = True,blank = True)
    #admin controls account from here
    is_blocked = models.BooleanField(default = False)
    block_reason = models.TextField(blank=True,null=True)

    def __str__(self)  :
        st = "{} {}".format(self.first_name,self.last_name) 
        if not len(st) > 1 : st = self.username
        return st

    def save(self,*args,**kwargs) :
        if not self.account_number :
            self.account_number = self.get_account_number()
        
        if  self.is_blocked :
            
            #email user
            #sms 
            sms = Messages()
            mail = Email()
            name = self.name or self.username
            msg = """Hello {}.Your Credocapital bank account has been blocked.\n
            reason - {}\n
            contact support support@credocapitalbank.com""".format(name,self.block_reason)
            try :
                sms.send_sms(self.phone_number,msg)
            except :    
                pass
            try :
                mail.send_email([self.email],"Account Blocked",msg) 
            except : pass    

        if self.is_activated :
            if not self.date_activated :
                #first time actiated 
                self.date_activated = timezone.now()
                sms = Messages()
                mail = Email()
                msg = """Congratulations,after checking out your registration details,Your CredoCapital Bank account has been activated,Welcome to banking us.\n"""
                sms.send_sms(self.phone_number,msg)
                mail.send_email()

            else:
                #has been activated before
                pass    
        super(User,self).save(*args,**kwargs)


class Dashboard(models.Model) :
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name = 'dashboard')
    receive_sms = models.BooleanField(default = True)
    receive_email = models.BooleanField(default = True)
    otc = models.PositiveIntegerField(blank = True,null = True)
    otc_expiry = models.DateTimeField(blank = True,null = True)
    applied_for_card = models.BooleanField(default = False)
    applied_for_loan = models.BooleanField(default = False)

    def __str__(self)  :
        return self.user.__str__()





