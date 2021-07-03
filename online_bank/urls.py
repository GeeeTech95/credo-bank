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
    path('34q3rtqgt54qtgrtqg46q4r/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',include('company.urls')),
    path('',include('Users.urls')) ,
    path('',include('core.urls')),
    path('transaction/',include('wallet.urls')),
    path('account/',include('Users.urls')),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
