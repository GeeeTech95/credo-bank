from django.contrib import admin
from django.views.generic import View
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .communication import Email
from .models import *
from .forms import SendMailForm


admin.site.register(Notification)
admin.site.register(NewsLaterSubscriber)
admin.site.register(AdminControl)



class AdminControls() :
    @staticmethod
    def allow_transactions() :
        try :
            return AdminControl.objects.all()[0].allow_transactions
        except :
            return False  


class SendCustomMail(UserPassesTestMixin,LoginRequiredMixin,View) :
    form_class = SendMailForm
    success_url = reverse_lazy('dashboard')
    template_name = 'form.html'
    email_template = 'custom-mail-new.html'

    def test_func(self) :
        if not self.request.user.is_staff :
            return False
        return True    

    def  get(self,request,*args,**kwargs)  :
        form = self.form_class
        form_title = 'Send Custom Email'
        return render(request,self.template_name,locals())

    def  post(self,request,*args,**kwargs)  :
        form = self.form_class(request.POST) 
        ctx = {}
        if form.is_valid() :
            sub = form.cleaned_data['subject']  
            email = form.cleaned_data['receiver_email']
            message = form.cleaned_data['message']
            receiver_name = form.cleaned_data['receiver_name']
            mail = Email(send_type="support")
            ctx['text'] = message
            ctx['name'] = receiver_name
            ctx['subject'] = sub

            mail.send_html_email(
                receive_email_list=[email],
                template=self.email_template,
                subject= sub,
                ctx=ctx
                )
            return HttpResponseRedirect(self.success_url)

        else : 
            return render(request,self.template_name,locals())



        
        

 
