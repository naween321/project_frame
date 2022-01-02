from rest_framework.routers import DefaultRouter
from .views.user import UserViewSet

ROUTER = DefaultRouter()

ROUTER.register('', UserViewSet, basename='users')

urlpatterns = ROUTER.urls
