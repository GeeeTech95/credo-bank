from django.contrib import admin
from .models import *


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
        
        

 
