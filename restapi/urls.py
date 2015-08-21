from django.conf.urls import patterns
from django.conf.urls import url

from .views import LanguageListAPI
from .views import LanguageRetrieveAPI
from .views import TestRetrieveAPI
from .views import TestListAPI
from .views import CandidatesListAPI
from .views import AnswerInsertAPI
from .views import CandidateInsertAPI
from .views import TestCandidateAnswersListAPI


urlpatterns = patterns('',
    url(r'^api/languages/$', LanguageListAPI.as_view(),
        name='api-language-list'),
    url(r'^api/languages/(?P<slug>[\w-]+)/$',
        LanguageRetrieveAPI.as_view(),
        name='api-language-detail'),
    url(r'^api/languages/(?P<language_slug>[\w-]+)/(?P<slug>[\w-]+)$',
        TestRetrieveAPI.as_view(),
        name='api-test-detail'),
    url(r'^api/candidate/answers/$',
        TestCandidateAnswersListAPI.as_view(),
        name='api-test-answers-list'),
    url(r'^api/test/$',
        TestListAPI.as_view(),
        name='api-test-list'),
    url(r'^api/candidate/list/$',
        CandidatesListAPI.as_view(),
        name='api-candidates-list'),
    url(r'^api/candidate/insert/$',
        CandidateInsertAPI.as_view(),
        name='api-candidates-insert'),
    url(r'^api/answer/insert/$',
        AnswerInsertAPI.as_view(),
        name='api-test-insert'),
)
