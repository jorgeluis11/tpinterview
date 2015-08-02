from django.conf.urls import patterns
from django.conf.urls import url

from .views import LanguageListView
from .views import LanguageDetailView

urlpatterns = patterns('',
    url(r'^language/$', LanguageListView.as_view(), name='wines-list'),
    url(r'^language/(?P<wine_slug>[\w-]+)/$', LanguageDetailView.as_view()),
)
