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


class ExamListAPI(generics.ListAPIView):
    serializer_class = ExamListSerializer
    queryset = Exam.objects.filter(status=True)


class CandidatesListAPI(generics.ListAPIView):
    serializer_class = CandidatesListSerializer
    queryset = Candidate.objects.filter()


class CandidateInsertAPI(generics.CreateAPIView):
    serializer_class = CandidateInsertSerializer
    queryset = Candidate.objects.filter()


class AnswerInsertAPI(generics.CreateAPIView):
    serializer_class = AnswerInsertSerializer
    queryset = Answer.objects.filter()
