from django.conf.urls import patterns
from django.conf.urls import url

from .views import index
from .views import languages
from .views import languagesDetail
from .views import languagesQuestionList

urlpatterns = patterns('',
    url(r'^$', index.as_view(), name='language-list'),
    url(r'^language/language_list.html/$', languages,
        name='language-list'),
    url(r'^language/language_detail.html/$', languagesDetail,
        name='language-detail'),
    url(r'^language/language_question.html/$', languagesQuestionList,
        name='language-exam-detail'),
)
