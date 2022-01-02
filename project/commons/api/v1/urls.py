from django.urls import path

from .views.file import FileView

urlpatterns = [
    path('file/', FileView.as_view())
]
