from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('dashboard', views.view_profile),
    path('dashboard/library', views.view_library),
    path('dashboard/library/add', views.add_book),
]