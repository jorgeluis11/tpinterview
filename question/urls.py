from django.conf.urls import patterns
from django.conf.urls import url

# from .views import LanguageListView
# from .views import LanguageDetailView
from .views import index, languages


urlpatterns = patterns('',
	 url(r'^$', index.as_view(),
    	name='language-list'),
	 url(r'^languages$', languages,
    	name='language-list'),
    # url(r'^language/$', LanguageListView.as_view(),
    # 	name='language-list'),
    # url(r'^language/(?P<language_slug>[\w-]+)/$', LanguageDetailView.as_view(),
    # 	name="language-detail"),
)
