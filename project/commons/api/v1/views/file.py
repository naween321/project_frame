from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.file import FileSerializer


class FileView(APIView):
    permission_classes = (AllowAny, )

    def post(self, *args, **kwargs):
        serializer = FileSerializer(data=self.request.data, context=dict(request=self.request))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
