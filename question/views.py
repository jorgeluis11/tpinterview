from django.shortcuts import render_to_response
from django.views.generic import TemplateView


class index(TemplateView):
    template_name = 'index.html'


def languages(request):
    return render_to_response("language/language_list.html", {})


def languagesDetail(request):
    return render_to_response("language/language_detail.html", {})


def languagesQuestionList(request):
    return render_to_response("language/language_question.html", {})
