from django.urls import include, path
from rest_framework.routers import DefaultRouter

from catalog.songs.api.views import (AlbumViewSet,  # isort:skip
                                     SingerViewSet, SongViewSet)

router = DefaultRouter()
router.register('singers', SingerViewSet)
router.register('songs', SongViewSet)
router.register('albums', AlbumViewSet)

app_name = 'api'
urlpatterns = [
    path('v1/', include(router.urls))
]
