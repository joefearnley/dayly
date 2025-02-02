from django.contrib import admin
from django.urls import path
from .views import UserUpdateView

urlpatterns = [
    path('', UserUpdateView.as_view(), name='account-edit'),
]