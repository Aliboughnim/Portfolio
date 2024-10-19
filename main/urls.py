from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='index'),  
    path('send-email/', views.send_email, name='send_email'),  
]