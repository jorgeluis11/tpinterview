from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
class APIRoot(APIView):
    def get(self, request):
        return Response({
            'questions': reverse('api-language-list', request=request),
        })