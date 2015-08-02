from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Language


class LanguageListView(ListView):
    model = Language
    template_name = 'language/language_list.html'
    context_object_name = 'languages'

    def get_queryset(self):
        language = Language.objects.filter(status=True)
        return language


class LanguageDetailView(DetailView):
    model = Language
    template_name = 'language/language_detail.html'
    context_object_name = 'language'

    def get_object(self):
        queryset = Language.objects.filter(status=True)
        language = get_object_or_404(queryset, slug=self.kwargs['language_slug'])
        return language