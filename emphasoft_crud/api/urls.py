from api.users_views import UserViewSet
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views


router = SimpleRouter()

router.register('users', UserViewSet, basename='user')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
