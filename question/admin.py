from django.contrib import admin

from .models import Language
from .models import Exam
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


class ExamAdmin(admin.ModelAdmin):
    fields = ('language', 'name', 'status')
    list_display = ('id', 'language', 'name',
                    'status')
    list_display_links = ['id', 'name', 'status']
    list_filter = ['status', 'name']
    search_fields = ['id', 'name']
    inlines = [QuestionsInlineChoiceInLine]


class QuestionAdmin(admin.ModelAdmin):
    fields = ('exam', 'question', 'order')
    list_display = ('id',  'question', 'exam',
                    'order')
    list_display_links = ['id', 'question', 'exam']
    list_filter = ['exam']
    search_fields = ['id', 'question', 'exam']


class CandidateAdmin(admin.ModelAdmin):
    fields = ('exam', 'name')
    list_display = ('id', 'exam', 'name',)
    list_display_links = ['id', 'exam', 'name']
    list_filter = ['exam']
    search_fields = ['id', 'name']


class AnswerAdmin(admin.ModelAdmin):
    fields = ('question', 'candidate', 'answer',
              'order')
    list_display = ('id', 'question', 'candidate',
                    'answer', 'order')
    list_display_links = ['id', 'question',
                          'candidate']
    list_filter = ['candidate', 'answer']
    search_fields = ['id', 'language']


admin.site.register(Language, LanguageAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Answer, AnswerAdmin)
