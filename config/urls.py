from django.conf import settings
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import views
from django.urls import include, path, re_path


AdminSite.login_template = 'rest_framework/login.html'
views.LogoutView.template_name = 'rest_framework/login.html'


urlpatterns = [
    path('dj-adm/', admin.site.urls),
    path('api/v1/', include('project.api.v1.urls')),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]
if settings.DEBUG:
    # swagger config

    from project.api.v1.swagger import SwaggerSchemaView
    from django.views.generic import RedirectView

    urlpatterns += [
        path('api/root/', SwaggerSchemaView.as_view()),
        path('', RedirectView.as_view(url='/api/root/', permanent=False))
    ]
    import debug_toolbar

    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
