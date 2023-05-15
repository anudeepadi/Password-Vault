from rest_framework import serializers
from passwords.models import Password

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = ('id', 'username', 'website', 'password')
