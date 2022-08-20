"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import Author_List

urlpatterns = [
    path('chat/', include('chat.urls')),
    #path('', include('chat.urls')),
    path('api/', include('myapi.urls')),
    path('admin/', admin.site.urls),
    path('', views.start, name='start'),
    path('room_select/', views.room_select, name='room_select'),
    #path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    path('mailing/<str:room_name>/<str:user_email>/', Author_List.as_view(), name='mailing'), # ссылка на рассылку приглашений
    #path('mailing/<str:room_name>/', views.room, name='mailing'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)