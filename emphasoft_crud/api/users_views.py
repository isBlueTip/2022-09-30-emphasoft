from django.contrib.auth.hashers import make_password
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from api.permissions import CreateOrSelfOrAdminOrReadOnly
from api.users_serializers import (ReadOnlyUserSerializer,
                                   WriteOnlyUserSerializer)
from users.models import User


class UserViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin
                  ):
    """Viewset to work with User model."""

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return ReadOnlyUserSerializer
        return WriteOnlyUserSerializer

    queryset = User.objects.all()
    permission_classes = [
        CreateOrSelfOrAdminOrReadOnly,
    ]
