from django.shortcuts import render
from django.views.generic import TemplateView,View
from django.http import JsonResponse
from core.views import Email
from django.template.loader import render_to_string
from .forms import ContactForm
from core.views import Messages


class Index(TemplateView) :
    template_name = 'home.html'

    def get(self,request,*args,**kwargs) :
        mail = Email()
        mail.send_html_email(['geeetech.inc@gmail.com'],'gf','transaction-email.html')
        return render(request,self.template_name,locals())

    def get_context_data(self,*args,**kwargs) : 
        context = super(Index,self).get_context_data(*args,**kwargs) 
        return context
        

class About(TemplateView) :
    template_name = 'about.html'

    def get_context_data(self,*args,**kwargs) : 
        context = super(About,self).get_context_data(*args,**kwargs) 
       
        return context
        

class LoanView(TemplateView) :
    template_name = 'loan_and_investment.html' 
           

class Faq(TemplateView) :
    template_name = 'faq.html'

    def get_context_data(self,*args,**kwargs) : 
        context = super(Faq,self).get_context_data(*args,**kwargs) 
       
        return context        


class Services(TemplateView) :
    template_name = 'services-xchange.html'

    def get_context_data(self,*args,**kwargs) : 
        context = super(Services,self).get_context_data(*args,**kwargs) 
        context['sclass'] = 'active'
        return context
         

class TOS(TemplateView) :
    template_name  = 'privacy.html'

    def get_context_data(self,*args,**kwargs) : 
        context = super(TOS,self).get_context_data(*args,**kwargs) 
        context['tclass'] = 'active'
        return context



class Contact(View) :
    template_name = 'contact.html'
    form_class = ContactForm


    def get(self,request,*args,**kwargs) :
        return render(request,self.template_name,{'cclass' : 'active'})

    def post(self,request,*args,**kwargs) :
        feedback = {}
        form = self.form_class(request.POST)  
        
        if form.is_valid() :
            
            name = form.cleaned_data.get('name','') 
            if len(name) > 0  : 
                name = "my name is {}.".format(name)
            title = form.cleaned_data.get('title')
            message = "{} {}".format(name,form.cleaned_data.get('message'))
            email = form.cleaned_data.get('email')
          
            send_mail(
                title,
                message,
                email,
                ['mercy@j.com'],
                fail_silently = True

            )
            feedback['success'] = True
        else : feedback['error'] = form.errors.as_json()
        return JsonResponse(feedback)    
