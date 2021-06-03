from  django.urls import path,include
from .accounts import Register,LoginRedirect
from .dashboard import Dashboard,Profile,TransactionHistory

urlpatterns = [
    path('',Dashboard.as_view(),name = 'dashboard'),
    path('create/',Register.as_view(),name = 'register'),
    path('info/',Profile.as_view(),name = 'profile'),
    
    #transaction
    path('transaction-history',TransactionHistory.as_view(),name ='transaction-history'),


    path('login/',LoginRedirect.as_view(),name="login-redirect")

]