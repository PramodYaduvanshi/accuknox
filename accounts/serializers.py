from rest_framework import serializers
from .models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "mobile_number",
            "first_name",
            "last_name",
            "username",
            "password",
        ]

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["email", "password"]


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "mobile_number",
            "first_name",
            "last_name",
            "username",
        ]


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "mobile_number",
            "first_name",
            "last_name",
            "username",
        ]
