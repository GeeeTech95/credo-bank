from django.shortcuts import render
from django.views.generic import RedirectView,View
from django.http import JsonResponse
from .forms import SubscribeForm
from .models import NewsLaterSubscriber,Notification as Notification_model



class Subscribe(View) :
    form_class = SubscribeForm
    model = NewsLaterSubscriber
    def post(self,request,*args,**kwargs) :
        feedback = {}
        form = self.form_class(request.POST)
        if form.is_valid() :
            form.save()
            feedback['success'] = 'subscribed'
        else : feedback['error'] = form.errors['email']    
        return JsonResponse(feedback)


class Email() :
    pass




class Messages() :
    pass


class Notification() :
    @staticmethod
    def notify(user,message) :
        Notification_model.objects.create(user = user,message = message)




