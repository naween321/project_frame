from django.contrib.auth import get_user_model

from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from project.commons.mixins.viewsets import ListRetrieveUpdateViewSetMixin

from ..serializers.user import UserSerializer

User = get_user_model()


class UserViewSet(ListRetrieveUpdateViewSetMixin):
    serializer_class = UserSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filter_fields = 'groups__name', 'is_active', 'is_locked', 'is_suspended'
    search_fields = ('first_name', 'middle_name', 'last_name')
    ordering_fields = 'first_name', 'created_at', 'updated_at', 'email', 'groups', 'time_zone', 'last_activity'

    def get_queryset(self):
        return User.objects.all()

    def get_object(self):
        if self.kwargs['username'] == 'me':
            self.kwargs['username'] = self.request.user.username.hex
        return super().get_object()
