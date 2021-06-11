from django.urls import path,include
from .notification import Subscribe 




urlpatterns = [
    path('subscribe/',Subscribe.as_view(),name = 'subscribe'),
  
]