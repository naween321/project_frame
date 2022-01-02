from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ListRetrieveUpdateViewSetMixin(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    pass
