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
from .views import languagesQuestionList
from .views import ExamRetrieveAPI
from .views import ExamListAPI


urlpatterns = patterns('',
    url(r'^$', index.as_view(), name='language-list'),
    url(r'^language/language_list.html/$', languages,
        name='language-list'),
    url(r'^language/language_detail.html/$', languagesDetail,
        name='language-detail'),
    url(r'^language/language_question.html/$', languagesQuestionList,
        name='language-exam-detail'),

    #API
    url(r'^api/languages/$', LanguageListAPI.as_view(),
        name='rest-language-list'),
    url(r'^api/languages/(?P<slug>[\w-]+)/$',
        LanguageRetrieveAPI.as_view(),
        name='rest-language-detail'),
    url(r'^api/languages/(?P<language_slug>[\w-]+)/(?P<slug>[\w-]+)$',
        ExamRetrieveAPI.as_view(),
        name='rest-exam-detail'),
    url(r'^api/exams/',
        ExamListAPI.as_view(),
        name='rest-exam-list'),
)
