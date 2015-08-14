from django.conf.urls import patterns
from django.conf.urls import url

from .views import LanguageListAPI
from .views import LanguageRetrieveAPI
from .views import ExamRetrieveAPI
from .views import ExamListAPI
from .views import CandidatesListAPI
from .views import AnswerInsertAPI
from .views import CandidateInsertAPI


urlpatterns = patterns('',
    url(r'^api/languages/$', LanguageListAPI.as_view(),
        name='api-language-list'),
    url(r'^api/languages/(?P<slug>[\w-]+)/$',
        LanguageRetrieveAPI.as_view(),
        name='api-language-detail'),
    url(r'^api/languages/(?P<language_slug>[\w-]+)/(?P<slug>[\w-]+)$',
        ExamRetrieveAPI.as_view(),
        name='api-exam-detail'),
    url(r'^api/test/$',
        ExamListAPI.as_view(),
        name='api-exam-list'),
    url(r'^api/candidate/insert/$',
        CandidateInsertAPI.as_view(),
        name='api-candidates-insert'),
    url(r'^api/candidate/list/$',
        CandidatesListAPI.as_view(),
        name='api-candidates-list'),
    url(r'^api/answer/$',
        AnswerInsertAPI.as_view(),
        name='api-exam-insert'),
)
