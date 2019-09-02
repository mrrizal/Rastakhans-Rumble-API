from django.conf.urls import include, url
from rest_framework import routers
from api.views import CardViewSet

router = routers.DefaultRouter()
router.register(r'card', CardViewSet, r'card')

urlpatterns = [url(r'^api/', include(router.urls, namespace='api'))]
