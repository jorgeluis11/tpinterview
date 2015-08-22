from django.conf.urls import patterns
from django.conf.urls import url

from .views import index
from .views import languages
from .views import languagesDetail
from .views import languagesQuestionList
from .views import testList
from .views import testCandidatesList
from .views import user_login
from .views import user_logout
from .views import insert_question
from .views import testCandidatesTestRetrieve
from .views import HelloPDFView
from .views import user_login_redirect



urlpatterns = patterns('',
    url(r'^$', index, name='language-list'),
    url(r'^language/language_list.html/$', languages,
        name='language-list'),
    url(r'^language/language_detail.html/$', languagesDetail,
        name='language-detail'),
    url(r'^language/language_question.html/$', languagesQuestionList,
        name='language-test-detail'),
    url(r'^test/test_list.html/$', testList,
        name='test-list'),
    url(r'^test/test_candidates_list.html/$', testCandidatesList,
        name='test-candidates-list'),
    url(r'^test/test_candidates_retrieve.html/$', testCandidatesTestRetrieve,
        name='test-candidates-retrieve'),
    url(r"^easy_pdf/test-candidate.pdf/$", HelloPDFView.as_view(),
        name='test-candidate-pdf'),
    (r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    (r'^logout/$', user_logout),
    (r'^redirect/$', user_login_redirect),
    (r'^login/validation$', user_login),
    (r'^insert$', insert_question),
)
