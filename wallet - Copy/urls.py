from django.urls import path,include
from .transaction import Transfer,CompleteTransaction
from .settings import ChangePin
from .deposit import Withdraw,Deposit



urlpatterns = [
    #TRANSACTION
    path('transfer/',Transfer.as_view(),name='transfer'),
    path('<str:transact_id>/complete-transacton/',CompleteTransaction.as_view(),name='complete-transaction'),
    
    #SETTINGS
    path('change-pin/',ChangePin.as_view(),name= 'change-pin'),

    #ACCOUNTS 
    path('deposit37276qr4/',Deposit.as_view(),name='deposit'),
    path('withdraw3q4q34q4q/',Withdraw.as_view(),name='withdraw'),


]