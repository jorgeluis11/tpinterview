from django.core.paginator import Paginator

from question.models import Language
from question.models import Test
from question.models import Question
from question.models import Answer
from question.models import Candidate

from rest_framework import pagination
from rest_framework import serializers


class TestListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
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
    test = serializers.SerializerMethodField('get_test_list')

    def get_test_list(self, language):
        queryset = Test.objects.filter(status=True, language=language)
        serializer = TestListSerializer(instance=queryset, many=True)
        return serializer.data

    class Meta:
        model = Language
        fields = ('id', 'name', 'slug', 'test')


class TestListSerializer(serializers.ModelSerializer):
    language = LanguageListSerializer()
    created_date = serializers.DateTimeField(format='%m/%d/%Y %H:%M')

    class Meta:
        model = Test
        fields = ('id', 'name', 'slug', 'language',
                  'created_date')


class TestRetrieveSerializer(serializers.ModelSerializer):
    language = LanguageListSerializer()
    questions = serializers.SerializerMethodField('get_question_list')

    def get_question_list(self, test):
        queryset = Question.objects.filter(test=test)
        serializer = QuestionListSerializer(instance=queryset, many=True)
        return serializer.data

    class Meta:
        model = Test
        fields = ('id', 'name', 'slug', 'language', 'questions')


class CandidatesListSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%m/%d/%Y %H:%M')
    test = TestListSerializer()

    class Meta:
        model = Candidate
        fields = ('id', 'test', 'name', 'slug', 'created_date')


class CandidateInsertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = ('id', 'test', 'name')


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer')


class AnswerInsertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'answer', 'question', 'candidate')


class TestCandidateAnswersSerializer(serializers.ModelSerializer):
    question = QuestionListSerializer()
    candidate = CandidatesListSerializer()

    class Meta:
        model = Answer
        fields = ('id', 'answer', 'question', 'candidate')
