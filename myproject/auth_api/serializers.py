from rest_framework import serializers
from auth_api.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'email', 'password', 'role_id')

