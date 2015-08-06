from django.core.paginator import Paginator

from .models import Language
from .models import Exam

from rest_framework import pagination
from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ExamListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = ('id', 'name', 'slug')


class LanguageListSerializer(serializers.ModelSerializer):
    # images = MotelImagesSerializer(many=True, read_only=True)
    # amenities = AmenitiesListSerializer(many=True, read_only=True)
    # town = TownListSerializer()

    # def get_motel_town(self, town):
    #     queryset = Language.objects.filter(status=True, town=town)
    #     serializer = TownListSerializer(instance=queryset, many=True)
    #     return serializer.data

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
