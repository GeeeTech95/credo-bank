from django.urls import path,include
from .views import Subscribe 




urlpatterns = [
    path('subscribe/',Subscribe.as_view(),name = 'subscribe'),
  
]