from django.conf.urls import patterns
from django.conf.urls import url
from .views import APIRoot

urlpatterns = patterns('',
    url(r'^api/$', APIRoot.as_view()),
)
