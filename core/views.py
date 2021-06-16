from django.shortcuts import render
from django.views.generic import RedirectView,View
from django.http import JsonResponse
from django.core.mail import send_mail

from django.conf import settings
from django.utils import timezone
import random
from twilio.rest import Client


class ValidationCode()     :
    @staticmethod
    def generate_code(user,email=None,phone_number=None,offset = None,send_type = 'message') :
        """ offset is the active time for the code,
        """
        offset = offset or 5
        expiry = timezone.now() + timezone.timedelta(minutes=offset)
        code = random.randrange(99999,999999)
        
        db = user.dashboard
        db.otc = int(code)
        db.otc_expiry = expiry
        db.save()
        msg = "Your verification code is {},active till {}".format(code,expiry.time())
        
        if send_type == 'message' :
            sms = Messages()
            sms.send_sms(phone_number,msg)

        elif send_type == 'email' :
            receipient = [email] 
            mail = Email() 
            mail.send_email(receipient,"email Verification",msg)  


    @staticmethod
    def validate_otc(user,code) :
        """
        returns a tuple of the validations state and error  if theres any or None as 2nd index
        """
        if user.dashboard.otc == int(code) :
            if not timezone.now() < user.dashboard.otc_expiry :
                error = "The entered code is correct,but has expired"
                return (False,error)
            else : 
                return (True,None)  

        else :
            return (False,"The entered code is incorrect")  

        return (False,"unknown error occured")           






class Email() :
    def __init__(self) :
        self.send_from = settings.EMAIL_HOST_USER

    def send_email(self,receivce_email_list,subject,message) :
        try : 
            send_mail(subject,message,self.send_from,receivce_email_list,fail_silently=False)
        except :
            pass
    def internal_transfer_debit_email(self,transaction) :
        acc_number = "{}***..*{}{}".format(
            transaction.user.account_number[0],
            transaction.user.account_number[-2],
            transaction.user.account_number[-1]
            )
        msg = """
        Txn : Debit\n
        Acc : {}\n
        Amt : {}\n
        Desc : Internal Transfer to {},{}\n
        Bal : {}\n
        Date  : {}""".format(acc_number,
        transaction.amount,
        transaction.user,
        transaction.user.account_number,
        transaction.user.wallet.available_balance,
        timezone.now()
        )
        self.send_email([transaction.user.email,],'transaction alert',msg)

    def internal_transfer_credit_email(self,transaction) :
        acc_number = "{}***..*{}{}".format(
            transaction.receiver.account_number[0],
            transaction.receiver.account_number[-2],
            transaction.receiver.account_number[-1]
            )

        msg = """
        Txn : Credit\n
        Acc : {}\n
        Amt : {}\n
        Desc : Received funds from {},{}\n
        Bal : {}\n
        Date  : {}""".format(acc_number,
        transaction.amount,
        transaction.receiver,
        transaction.receiver.account_number,
        transaction.receiver.wallet.available_balance,
        timezone.now()
        )
        self.send_email([transaction.receiver.email,],'transaction alert',msg)

    def external_transfer_debit_email(self,transaction) :
        acc_number = "{}***..*{}{}".format(
            transaction.user.account_number[0],
            transaction.user.account_number[-2],
            transaction.user.account_number[-1]
            )
        msg = """
        Txn : Debit\n
        Acc : {}\n
        Amt : {}\n
        Desc : International Transfer to {},A/C - {},iban - {},bank - {}\n
        Bal : {}\n
        Date  : {}""".format(acc_number,
        transaction.amount,
        transaction.user,
        transaction.user.account_number,
        transaction.iban,
        transaction.bank_name,
        transaction.user.wallet.available_balance,
        timezone.now()
        )
        self.send_email([transaction.user.email],'transaction alert',msg)    
 
class Messages() :

    def __init__(self) :
        self.client = Client(settings.TWILLO_ACCOUNT_SID,settings.TWILLO_AUTH_TOKEN)
    

    def send_sms(self,phone_number,message) :
        try :
            message = str(message)
            phone_number = str(phone_number)
            if not phone_number.startswith('+') : 
                raise ValueError("Phone number must be in international format")
        except : 
            raise ValueError("message and phone number must be in string format")    
        try :
            self.client.messages.create(
                to = phone_number,
                from_= settings.SMS_PHONE_NUMBER,
                body = message
                )
        except : pass
                    


    def internal_transfer_debit_sms(self,transaction) :
        acc_number = "{}***..*{}{}".format(
            transaction.user.account_number[0],
            transaction.user.account_number[-2],
            transaction.user.account_number[-1]
            )
        msg = """
        Txn : Debit\n
        Acc : {}\n
        Amt : {}\n
        Desc : Internal Transfer to {},{}\n
        Bal : {}\n
        Date  : {}""".format(acc_number,
        transaction.amount,
        transaction.user,
        transaction.user.account_number,
        transaction.user.wallet.available_balance,
        timezone.now()
        )
        self.send_sms(transaction.user.phone_number,msg)


    def internal_transfer_credit_sms(self,transaction) :
        acc_number = "{}***..*{}{}".format(
            transaction.receiver.account_number[0],
            transaction.receiver.account_number[-2],
            transaction.receiver.account_number[-1]
            )

        msg = """
        Txn : Credit\n
        Acc : {}\n
        Amt : {}\n
        Desc : Received funds from {},{}\n
        Bal : {}\n
        Date  : {}""".format(acc_number,
        transaction.amount,
        transaction.receiver,
        transaction.receiver.account_number,
        transaction.receiver.wallet.available_balance,
        timezone.now()
        )
        self.send_sms(transaction.receiver.phone_number,msg) 

    
    def external_transfer_debit_sms(self,transaction) :
        acc_number = "{}***..*{}{}".format(
            transaction.user.account_number[0],
            transaction.user.account_number[-2],
            transaction.user.account_number[-1]
            )
        msg = """
        Txn : Debit\n
        Acc : {}\n
        Amt : {}\n
        Desc : International Transfer to {},A/C - {},iban - {},bank - {}\n
        Bal : {}\n
        Date  : {}""".format(acc_number,
        transaction.amount,
        transaction.user,
        transaction.user.account_number,
        transaction.iban,
        transaction.bank_name,
        transaction.user.wallet.available_balance,
        timezone.now()
        )
        self.send_sms(transaction.user.phone_number,msg)







