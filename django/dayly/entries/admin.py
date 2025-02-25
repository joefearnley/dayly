from django.contrib import admin
from .models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('body', 'user', 'date_created', 'date_published')

admin.site.register(Entry, EntryAdmin)