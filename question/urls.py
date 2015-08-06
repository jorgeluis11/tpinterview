from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls import include
# from .views import LanguageListView
# from .views import LanguageDetailView
from .views import index
from .views import languages
from .views import languagesDetail
from .views import LanguageListAPI
from .views import LanguageRetrieveAPI


urlpatterns = patterns('',
    url(r'^$', index.as_view(), name='language-list'),
    url(r'^language/language_list.html/$', languages,
        name='language-list'),
    url(r'^language/language_detail.html/$', languagesDetail,
        name='language-detail'),

    url(r'^api/languages/$', LanguageListAPI.as_view(),
        name='rest-language-list'),
    url(r'^api/languages/(?P<slug>[\w-]+)/$',
        LanguageRetrieveAPI.as_view(),
        name='rest-language-detail'),
)
