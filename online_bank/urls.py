"""online_bank URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

#oscar
from django.apps import apps


urlpatterns = [
    path('yrgyegryeyrgtw3g473gyr7wger4/', admin.site.urls),
   path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('users.urls')),
    path("", include("company.urls")),
    path('', include('core.urls')),
    path('accounts/', include('wallet.urls')),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


handler404 = 'core.views.error_404_handler'
handler500 = 'core.views.error_500_handler'
handler403 = 'core.views.error_403_handler'