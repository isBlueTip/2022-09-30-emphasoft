from api.users_views import UserViewSet
from django.urls import include, path
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register('users', UserViewSet, basename='user')


urlpatterns = [
    path('v1/', include(router.urls)),
]
