"""zapravka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("info/", InfoView.as_view()),
    path("info/update/<int:pk>/", InfoUpdate.as_view()),
    path("client/", ClientView.as_view()),
    path("client/update/<int:pk>/", ClientUpdate.as_view()),
    path("benzin/get/", BenzinGet.as_view()),
    path("benzin/update/<int:pk>/", BenzinUpdate.as_view()),
    path("benzin/production/", BenzinProductionView.as_view()),
    path("benzin/production/post/", BenzinProductionPost.as_view()),
    path("cash/get/", CashGet.as_view()),
    path("pay/", PayView.as_view()),
    path("pay/client/get/", PayClientGet.as_view()),
    path("pay/time/get/", PayTimeGet.as_view()),
    path("news/<int:pk>/", NewsView.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
