# import logging

from api.users_serializers import (ReadOnlyUserSerializer, WriteOnlyUserSerializer)
# from loggers import formatter, logger
from rest_framework import status, viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from users.models import User
from api.permissions import CreateOrSelfOrAdminOrReadOnly

# LOG_NAME = 'users_views.log'
#
# file_handler = logging.FileHandler(LOG_NAME)
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)


class UserViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin
                  ):
    """Viewset to work with User model."""

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return ReadOnlyUserSerializer
        return WriteOnlyUserSerializer

    queryset = User.objects.all()
    permission_classes = [
        # AllowAny,
        # IsAuthenticatedOrReadOnly,
        CreateOrSelfOrAdminOrReadOnly,
        # IsAuthenticated,
    ]

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
