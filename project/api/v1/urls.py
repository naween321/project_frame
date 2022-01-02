"""
v1 API url for swagger view
"""
from django.urls import include, path

urlpatterns = [
    path('commons/', include('project.commons.api.v1.urls')),
    path('user/', include('project.user.api.v1.urls')),
    path('authentication/', include('project.authentication.api.v1.urls')),
]
