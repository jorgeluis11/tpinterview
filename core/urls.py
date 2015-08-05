from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls import include
# from .views import LanguageListView
# from .views import LanguageDetailView
from .views import APIRoot



urlpatterns = patterns('',
    url(r'^api/$', APIRoot.as_view()),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    )