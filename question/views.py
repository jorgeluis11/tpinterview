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
from .serializers import LanguageListSerializer
import simplejson
import json



# class LanguageListView(ListView):
#     model = Language
#     template_name = 'language/language_list.html'
#     context_object_name = 'languages'

#     def get_queryset(self):
#         language = Language.objects.filter(status=True)
#         return language


# class LanguageDetailView(DetailView):
#     model = Language
#     template_name = 'language/language_detail.html'
#     context_object_name = 'language'

#     def get_object(self):
#         queryset = Language.objects.filter(status=True)
#         language = get_object_or_404(queryset, slug=self.kwargs['language_slug'])
#         return language

class index(TemplateView):
    template_name = 'index.html'

# def languages(request):
    # languages = serializers.serialize('json', Language.objects.all())
    # data = {'languages': languages}
    # dic = json.loads(languages)['fields']

    # return HttpResponse(simplejson.dumps(Language.objects.all()),
                        # content_type='application/json')

def languages(request):
    return render_to_response("language/language_list.html",{})

class LanguageList(generics.ListAPIView):
    """
    #Retrieves a list of all motels
    ---
    ### 1. Ordering Values Documentation
    > Order by name, town name, amenities name, rating and price

    - ####Examples:
        *  #####Ordering by name: [?ordering=name](?ordering=name)
        *  #####Ordering by town: [?ordering=town__name](?ordering=town__name)
        *  #####Ordering by amenities: [?ordering=amenities__name](?ordering=amenities__name)
        *  #####Ordering by rating: [?ordering=rating](?ordering=rating)
        *  #####Ordering by price: [?ordering=price](?ordering=price)
        *  #####Ordering by price: [?ordering=created_date](?ordering=created_date)

    The API may also specify reverse orderings by prefixing the field name with '-', like so:
        
        - http://example.com/api/motels?ordering=-name
    
    Multiple orderings may also be specified:
        
        - http://example.com/api/motels?ordering=name,town__name
    ---
    ### 2. Search Values Documentation
    > Search by motel name keyword

    - ####Example:
        *  #####Search by Motel Name: [?search=MotelName](?search=MotelName)
    ---
    """
    queryset = Language.objects.filter(status=True)
    serializer_class = LanguageListSerializer
    # filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    # ordering_fields = ('name', 'town__name', 'amenities__name',
    #                    'rating', 'price', 'created_date')
    # search_fields = ('^name', )