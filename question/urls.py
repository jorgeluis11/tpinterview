from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls import include
# from .views import LanguageListView
# from .views import LanguageDetailView
from .views import index, languages , LanguageList


urlpatterns = patterns('',
    url(r'^$', index.as_view(),
        name='language-list'),
    url(r'^language/language_list.html/$', languages,
        name='language-list'),
    url(r'^language/language_detail.html/$', languages,
        name='language-list'),
    url(r'^language/$', languages,
        name='language-list'),
    url(r'^api/languages/$', LanguageList.as_view(), name='language-list'),

    # ul(r'^api/motels/filters/$', views.MotelListFilters.as_view(), name='motels-filters'),
    # url(r'^api/motels/(?P<motels_slug>[\w-]+)/$', views.MotelRetrieve.as_view(), name='motel-retrieve'),
    #   name='language-list'),
    # url(r'^language/(?P<language_slug>[\w-]+)/$', LanguageDetailView.as_view(),
    #   name="language-detail"),
)
