from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.core import serializers

from rest_framework import filters
from rest_framework import generics

from .models import Language
from .models import Exam
from .serializers import LanguageListSerializer
from .serializers import LanguageRetrieveSerializer
from .serializers import ExamRetrieveSerializer
from .serializers import ExamListSerializer


class index(TemplateView):
    template_name = 'index.html'


def languages(request):
    return render_to_response("language/language_list.html", {})


def languagesDetail(request):
    return render_to_response("language/language_detail.html", {})


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
