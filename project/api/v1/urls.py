"""
v1 API url for swagger view
"""
from django.urls import include, path

urlpatterns = [
    path('commons/', include('project.commons.api.v1.urls'))
]
