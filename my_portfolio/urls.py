from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('index')), 
]