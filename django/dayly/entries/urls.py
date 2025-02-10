from django.contrib import admin
from django.urls import path
from .views import IndexView, EditView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('/edit', EditView.as_view(), name='index'),
]
