from django.contrib import admin
from django.urls import path
from .views import IndexView, EntryCreateView, EntryUpdateView, EntryView, EntryDeleteView, EntryPreviewView

urlpatterns = [
    path('', IndexView.as_view(), name='entries_index'),
    path('create/', EntryCreateView.as_view(), name='create_entry'),
    path('preview/', EntryPreviewView.as_view(), name='preview_entry'),
    path('<int:pk>/', EntryUpdateView.as_view(), name='edit_entry'),
    path('<slug:slug>/', EntryView.as_view(), name='view_entry'),
    path('delete/<slug:slug>/', EntryDeleteView.as_view(), name='delete_entry'),
]
