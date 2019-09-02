from django.conf.urls import url, include
from django.http import HttpResponseRedirect

urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('api/')),
    url(r'^', include('api.urls')),
]
