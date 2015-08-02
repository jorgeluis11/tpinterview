from django.contrib import admin

from .models import Language
from .models import Exam
from .models import Question
from .models import Candidate
from .models import Answer


class LanguageAdmin(admin.ModelAdmin):
    fields = ('language', 'status')
    list_display = ('id', 'language', 'status')
    list_display_links = ['id', 'language']
    list_filter = ['status']
    search_fields = ['id', 'language']


class ExamAdmin(admin.ModelAdmin):
    fields = ('language', 'exam', 'status')
    list_display = ('id', 'language', 'exam',
    				'status')
    list_display_links = ['id', 'exam', 'status']
    list_filter = ['status', 'language']
    search_fields = ['id', 'exam']


class QuestionAdmin(admin.ModelAdmin):
    fields = ('exam', 'question', 'order')
    list_display = ('id',  'question', 'exam',
    				'order')
    list_display_links = ['id', 'question', 'exam']
    list_filter = ['exam']
    search_fields = ['id', 'question', 'exam']


class CandidateAdmin(admin.ModelAdmin):
    fields = ('exam', 'first_name', 'last_name')
    list_display = ('id', 'exam', 'first_name',
    				'last_name')
    list_display_links = ['id', 'exam', 'first_name',
    					 'last_name']
    list_filter = ['exam']
    search_fields = ['id', 'first_name', 'last_name']


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
