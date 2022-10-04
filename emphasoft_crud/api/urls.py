from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from api.users_views import UserViewSet

router = SimpleRouter()

router.register('users', UserViewSet, basename='user')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
