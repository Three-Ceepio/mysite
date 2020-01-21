from django.urls import path
from . import views

urlpatterns = [
    path('', views.email_page, name='email_page'),
    path('success/', views.success_page, name='success_page'),
]