from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views
from api.views import UserViewSet, EntryViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', authtoken_views.obtain_auth_token, name='api-token-auth'),
]