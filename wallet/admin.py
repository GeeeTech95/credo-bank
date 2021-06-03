from django.contrib import admin
from .models import Wallet,Transaction,Currency


admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(Transaction)
