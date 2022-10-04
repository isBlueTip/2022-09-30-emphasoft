# import logging
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
# from .loggers import logger, formatter
from users.models import User
import re

# LOG_NAME = 'serializers.log'
#
# file_handler = logging.FileHandler(LOG_NAME)
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)


class ReadOnlyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'is_active',
            'last_login',
            'is_superuser',
        ]


class WriteOnlyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'is_active',
        ]
        extra_kwargs = {'is_active': {'required': True},
                        'first_name': {'required': False},
                        'last_name': {'required': False},
                        }

    def validate_username(self, value):
        pattern = r'^[\w.@+-]+$'
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                'Login can contain lowercase, uppercase letters, digits, _, -, +, @ and .')
        return value

    def validate_password(self, value):
        pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                'Password must be longer than 8 symbols'
                ' and include lower-case and upper-case letter, digits and special characters')
        return value
