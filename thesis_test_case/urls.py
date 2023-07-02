# Django imports
from django.contrib import admin
from django.urls import path, include

# custom objects imports
from api.router import router

# Swagger imports
from thesis_test_case import yasg

# JWT imports
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView

urlpatterns = [
    # admin URL
    path('admin/', admin.site.urls),
    # API URLs
    path('', include(router.urls)),
    # Swagger URLs
    path('', include(yasg.urlpatterns)),
    # JWT URLs
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view())
]
