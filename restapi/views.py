import django_filters
from django.core import serializers

from rest_framework import filters
from rest_framework import generics

from question.models import Language
from question.models import Test
from question.models import Answer
from question.models import Candidate
from .serializers import LanguageListSerializer
from .serializers import LanguageRetrieveSerializer
from .serializers import TestRetrieveSerializer
from .serializers import TestListSerializer
from .serializers import CandidatesListSerializer
from .serializers import AnswerInsertSerializer
from .serializers import CandidateInsertSerializer
from .serializers import TestCandidateAnswersSerializer

class AnswerFilter(django_filters.FilterSet):
    """
    Filter Answer by Test and candidate
    """
    test = django_filters.CharFilter(name="question__test__slug")
    candidate = django_filters.CharFilter(name="candidate__slug")

    class Meta:
        model = Answer
        fields = ['test', 'candidate']


class LanguageListAPI(generics.ListAPIView):
    queryset = Language.objects.filter(status=True)
    serializer_class = LanguageListSerializer


class LanguageRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = LanguageRetrieveSerializer
    queryset = Language.objects.filter(status=True)
    lookup_field = 'slug'


class TestRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = TestRetrieveSerializer
    queryset = Test.objects.filter(status=True)
    lookup_field = 'slug'


class TestCandidateAnswersListAPI(generics.ListAPIView):
    """
    # Retrieves a list of all Answers
    ---
    ### Filters Values
    > Filters by test slug and candidate slug

    - ####Examples:
        *  #####Filter by test: [?test=beginner-stuff](?test=beginner-stuff)
        *  #####Filter by candidate: [?candidate=Wifi](?candidate=Wifi)
    ---
    """
    serializer_class = TestCandidateAnswersSerializer
    queryset = Answer.objects.filter()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AnswerFilter


class TestListAPI(generics.ListAPIView):
    serializer_class = TestListSerializer
    queryset = Test.objects.filter(status=True)


class CandidatesListAPI(generics.ListAPIView):
    serializer_class = CandidatesListSerializer
    queryset = Candidate.objects.filter()


class CandidateInsertAPI(generics.CreateAPIView):
    serializer_class = CandidateInsertSerializer
    queryset = Candidate.objects.filter()


class AnswerInsertAPI(generics.ListCreateAPIView):
    serializer_class = AnswerInsertSerializer
    queryset = Answer.objects.filter()
