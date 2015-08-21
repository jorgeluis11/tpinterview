from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class APIRoot(APIView):
    def get(self, request):
        return Response({
            'language': reverse('api-language-list', request=request),
            'candidate-answers': reverse('api-exam-answers-list', request=request),
            'test-list': reverse('api-exam-list', request=request),
            'candidates-list': reverse('api-candidates-list', request=request),
        })
