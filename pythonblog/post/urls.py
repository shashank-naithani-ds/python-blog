from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.home, name="homepage"),
    path('<slug:blogid>', views.detailpage, name='page_detail'),
]