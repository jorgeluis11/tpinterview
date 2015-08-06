from django.core.paginator import Paginator

from .models import Language
from .models import Exam
from .models import Question

from rest_framework import pagination
from rest_framework import serializers


class ExamListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = ('id', 'name', 'slug')


class QuestionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'question', 'order')


class LanguageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'name', 'slug')


class LanguageRetrieveSerializer(serializers.ModelSerializer):
    exam = serializers.SerializerMethodField('get_exam_list')

    def get_exam_list(self, language):
        queryset = Exam.objects.filter(status=True, language=language)
        serializer = ExamListSerializer(instance=queryset, many=True)
        return serializer.data

    class Meta:
        model = Language
        fields = ('id', 'name', 'slug', 'exam')


class ExamListSerializer(serializers.ModelSerializer):
    language = LanguageListSerializer()

    class Meta:
        model = Exam
        fields = ('id', 'name', 'slug', 'language')


class ExamRetrieveSerializer(serializers.ModelSerializer):
    language = LanguageListSerializer()
    questions = serializers.SerializerMethodField('get_question_list')

    def get_question_list(self, exam):
        queryset = Question.objects.filter(exam=exam)
        serializer = QuestionListSerializer(instance=queryset, many=True)
        return serializer.data

    class Meta:
        model = Exam
        fields = ('id', 'name', 'slug', 'language', 'questions')
