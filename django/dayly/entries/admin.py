from django.contrib import admin
from .models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date_created')

admin.site.register(Entry, EntryAdmin)