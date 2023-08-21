from django.urls import include, path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

app_name = 'api'
urlpatterns = [
    path('v1/', include(router.urls))
]
