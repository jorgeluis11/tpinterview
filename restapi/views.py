import django_filters
from django.core import serializers

from rest_framework import filters
from rest_framework import generics

from question.models import Language
from question.models import Exam
from question.models import Answer
from question.models import Candidate
from .serializers import LanguageListSerializer
from .serializers import LanguageRetrieveSerializer
from .serializers import ExamRetrieveSerializer
from .serializers import ExamListSerializer
from .serializers import CandidatesListSerializer
from .serializers import AnswerInsertSerializer
from .serializers import CandidateInsertSerializer
from .serializers import ExamCandidateAnswersSerializer

class AnswerFilter(django_filters.FilterSet):
    """
    Filter Answer by exam and candidate
    """
    exam = django_filters.CharFilter(name="question__exam__slug")
    candidate = django_filters.CharFilter(name="candidate__slug")

    class Meta:
        model = Answer
        fields = ['exam', 'candidate']


class LanguageListAPI(generics.ListAPIView):
    queryset = Language.objects.filter(status=True)
    serializer_class = LanguageListSerializer


class LanguageRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = LanguageRetrieveSerializer
    queryset = Language.objects.filter(status=True)
    lookup_field = 'slug'


class ExamRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = ExamRetrieveSerializer
    queryset = Exam.objects.filter(status=True)
    lookup_field = 'slug'


class ExamCandidateAnswersListAPI(generics.ListAPIView):
    """
    # Retrieves a list of all Answers
    ---
    ### Filters Values
    > Filters by test slug and candidate slug

    - ####Examples:
        *  #####Filter by test: [?exam=beginner-stuff](?exam=beginner-stuff)
        *  #####Filter by candidate: [?candidate=Wifi](?candidate=Wifi)
    ---
    """
    serializer_class = ExamCandidateAnswersSerializer
    queryset = Answer.objects.filter()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AnswerFilter


class ExamListAPI(generics.ListAPIView):
    serializer_class = ExamListSerializer
    queryset = Exam.objects.filter(status=True)


class CandidatesListAPI(generics.ListAPIView):
    serializer_class = CandidatesListSerializer
    queryset = Candidate.objects.filter()
    filter_backends = (filters.OrderingFilter,)
    ordering = ('created_date',)


class CandidateInsertAPI(generics.CreateAPIView):
    serializer_class = CandidateInsertSerializer
    queryset = Candidate.objects.filter()


class AnswerInsertAPI(generics.ListCreateAPIView):
    serializer_class = AnswerInsertSerializer
    queryset = Answer.objects.filter()
