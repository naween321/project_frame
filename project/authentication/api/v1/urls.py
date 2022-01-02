from django.urls import path
from .views.token import ObtainAuthTokenView

urlpatterns = [
    path('auth/obtain/', ObtainAuthTokenView.as_view(), name='obtain'),
]
