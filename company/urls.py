from django.urls import path,include
from .pages import Index,Services,TOS,About,Contact,Faq,LoanView
from .services import Services


urlpatterns = [
    path('',Index.as_view(),name = 'index'),
    path('test/',About.as_view(),name = 'about-us'),
    path('services/',Services.as_view(),name = 'info'),
    path('FAQ/',Faq.as_view(),name='faq'),
    #path('terms-of-service/',TOS.as_view(),name = 'tos'),  
    #path('loan-and-investment/',LoanView.as_view(),name = 'loan&investment'),
    path('services/',Services.as_view(),name='services')  
    
]