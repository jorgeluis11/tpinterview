from django.contrib import admin

from .models import Language
from .models import Test
from .models import Question
from .models import Candidate
from .models import Answer


class QuestionsInlineChoiceInLine(admin.TabularInline):
    model = Question
    extra = 3


class LanguageAdmin(admin.ModelAdmin):
    fields = ('name', 'status')
    list_display = ('id', 'name', 'status')
    list_display_links = ['id', 'name']
    list_filter = ['status']
    search_fields = ['id', 'name']


class TestAdmin(admin.ModelAdmin):
    fields = ('language', 'name', 'status')
    list_display = ('id', 'language', 'name',
                    'status')
    list_display_links = ['id', 'name', 'status']
    list_filter = ['status', 'name']
    search_fields = ['id', 'name']
    inlines = [QuestionsInlineChoiceInLine]


class QuestionAdmin(admin.ModelAdmin):
    fields = ('test', 'question', 'order')
    list_display = ('id',  'question', 'test',
                    'order')
    list_display_links = ['id', 'question', 'test']
    list_filter = ['test']
    search_fields = ['id', 'question', 'test']


class CandidateAdmin(admin.ModelAdmin):
    fields = ('test', 'name')
    list_display = ('id', 'test', 'name',)
    list_display_links = ['id', 'test', 'name']
    list_filter = ['test']
    search_fields = ['id', 'name']


class AnswerAdmin(admin.ModelAdmin):
    fields = ('question', 'candidate', 'answer')
    list_display = ('id', 'question', 'candidate',
                    'answer')
    list_display_links = ['id', 'question',
                          'candidate']
    list_filter = ['candidate']
    search_fields = ['id', 'language']


admin.site.register(Language, LanguageAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Answer, AnswerAdmin)
