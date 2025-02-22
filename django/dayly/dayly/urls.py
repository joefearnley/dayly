from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('allauth.urls')),
    path('entries/', include('entries.urls')),
    path('account/', include('accounts.urls')),
    path('', include('core.urls')),
]
