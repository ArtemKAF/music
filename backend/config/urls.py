from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='index.html',
    ), name='index'),
    path('admin/', admin.site.urls),
    path('api_schema', get_schema_view(title='API Schema'), name='api_schema'),
    path('swagger-ui', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'api_schema'}
    ), name='swagger-ui'),
]

urlpatterns += [
    path('api/', include('config.api_router')),
]
