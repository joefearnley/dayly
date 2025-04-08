from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from .serlializers import UserSerializer, EntrySerializer
from entries.models import Entry


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class EntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user's entries to be viewed.
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super(EntryViewSet, self).get_queryset()
        return queryset.filter(user=self.request.user).order_by('-date_published')
