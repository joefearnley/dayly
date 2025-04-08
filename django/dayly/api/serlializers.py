from django.contrib.auth.models import User
from rest_framework import serializers
from entries.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'body', 'slug', 'date_created', 'date_published', 'date_updated']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'last_login']
