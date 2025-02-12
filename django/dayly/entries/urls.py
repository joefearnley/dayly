from django.contrib import admin
from django.urls import path
from .views import IndexView, EntryCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='entries_index'),
    path('create', EntryCreateView.as_view(), name='create_entry'),
    path('<int:pk>/', EntryCreateView.as_view(), name='edit_entry'),
]
