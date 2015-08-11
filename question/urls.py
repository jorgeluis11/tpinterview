from django.conf.urls import patterns
from django.conf.urls import url

from .views import index
from .views import languages
from .views import languagesDetail
from .views import languagesQuestionList
from .views import testList
from .views import user_login

urlpatterns = patterns('',
    url(r'^$', index.as_view(), name='language-list'),
    url(r'^language/language_list.html/$', languages,
        name='language-list'),
    url(r'^language/language_detail.html/$', languagesDetail,
        name='language-detail'),
    url(r'^language/language_question.html/$', languagesQuestionList,
        name='language-exam-detail'),
    url(r'^test/test_list.html/$', testList,
        name='test-list'),
    (r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    (r'^login/validation$', user_login),
)
