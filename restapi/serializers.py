from django.core.paginator import Paginator

from question.models import Language
from question.models import Exam
from question.models import Question
from question.models import Answer
from question.models import Candidate

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
    created_date = serializers.DateTimeField(format='%m/%d/%Y %H:%M')

    class Meta:
        model = Exam
        fields = ('id', 'name', 'slug', 'language', 'created_date')


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


class CandidatesListSerializer(serializers.ModelSerializer):
    exam = ExamListSerializer()
    created_date = serializers.DateTimeField(format='%m/%d/%Y %H:%M')

    class Meta:
        model = Candidate
        fields = ('id', 'exam', 'name', 'slug', 'created_date')


class CandidateInsertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = ('id', 'exam', 'name')


class AnswersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = ('id', 'answer')


class AnswerInsertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'answer', 'question', 'candidate')


class ExamCandidateAnswersSerializer(serializers.ModelSerializer):
    question = QuestionListSerializer()
    candidate = CandidatesListSerializer()

    class Meta:
        model = Answer
        fields = ('id', 'answer', 'question', 'candidate')


