from  django.urls import path,include
from .accounts import Register,LoginRedirect
from .dashboard import Dashboard,Profile,TransactionHistory,RequestCreditCard,LoanApply,AccountStatement
from .views import ValidatePhoneNumber,VerifyEmail

urlpatterns = [
    path('',Dashboard.as_view(),name = 'dashboard'),
    path('create/',Register.as_view(),name = 'register'),
    path('info/',Profile.as_view(),name = 'profile'),
    
    #transaction
    path('transaction-history/',TransactionHistory.as_view(),name ='transaction-history'),
    path('request-credit-card/',RequestCreditCard.as_view(),name='credit-card-request'),
    path('loan/apply/',LoanApply.as_view(),name='loan-apply'),
    path('statement/',AccountStatement.as_view(),name='account-statement'),

    path('login/',LoginRedirect.as_view(),name="login-redirect"),

    #account
    #path('verify-phone-number/',ValidatePhoneNumber.as_view(),name='validate-phone-number'),
    #path('verify-phone-number/send-code/',ValidatePhoneNumber.SendCode.as_view(),name= 'validate-phone-number-send-code'),

    path('verify-email/',VerifyEmail.as_view(),name='validate-email'),
    path('verify-email/send-code',VerifyEmail.SendCode.as_view(),name= 'validate-email-send-code')

]