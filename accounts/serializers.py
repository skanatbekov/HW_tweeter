import re

from rest_framework import serializers
from django.contrib.auth import password_validation as pv

from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'profile_avatar']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def validate_password(form, value):
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError('Пароль должен содержать хотя бы 1 цифру')
        if not any(char.isalpha() for char in value):
            raise serializers.ValidationError('Пароль должен содержать хотя бы 1 букву')
        if len(value) < 8:
            raise serializers.ValidationError("пароль должен состоять из 8 или более символов")
        if re.search('[!@#$%&*?<>{}[]', value):
            raise serializers.ValidationError("пароль не должен содержать специальных символов")
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data.get('username'),
            profile_avatar=validated_data.get('profile_avatar')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


