from django.db import models
from django.contrib.auth.models   import AbstractUser
from django.utils.text import  slugify
from django.contrib.auth import get_user_model
import random




class Country(models.Model) :
    name = models.CharField(max_length = 20)
    code = models.CharField(max_length = 5,blank = True)

    def __str__(self) :
        return self.name

    

class State(models.Model) :
    name = models.CharField(max_length = 20) 
    code = models.CharField(max_length = 5,blank = True) 
    country = models.ForeignKey(Country,on_delete = models.CASCADE,related_name='states') 

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
    state = models.ForeignKey(State,on_delete= models.SET_NULL,null = True,blank = True,related_name='users')
    address = models.TextField(null = True)
    account_number  = models.CharField(default=get_account_number,editable=False,null = False,max_length=14,unique=True,blank = True)
    account_type = models.CharField(default="SAVINGS",max_length=10,choices = ACCOUNT_TYPE)
    passport = models.FileField(upload_to = get_path,null = True)
    is_activated = models.BooleanField(default = False,blank = False,null = False)
    #admin controls account from here
    is_blocked = models.BooleanField(default = False)
    block_reason = models.TextField()

    def __str__(self)  :
        st = "{} {}".format(self.first_name,self.last_name) 
        if not len(st) > 1 : st = self.username
        return st

    def save(self,*args,**kwargs) :
        if not self.account_number :
            self.account_number = self.get_account_number()
        if  self.is_blocked :
            #notify user
            #email user
            #sms user
            pass

        super(User,self).save(*args,**kwargs)


class Dashboard(models.Model) :
    pass




