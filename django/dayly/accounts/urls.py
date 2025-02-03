from django.contrib import admin
from django.urls import path
from .views import UserUpdateView

urlpatterns = [
    path('edit', UserUpdateView.as_view(), name='account-edit'),
]