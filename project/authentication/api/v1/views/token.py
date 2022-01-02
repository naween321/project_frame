from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..serializers.token import CustomAuthTokenSerializer


class ObtainAuthTokenView(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])
        return Response({'token': token.key, 'groups': user.groups.all().values_list('name', flat=True)})
