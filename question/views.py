import reportlab
import ast

from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.template import RequestContext

from .models import Answer

from reportlab.pdfgen import canvas
from easy_pdf.views import PDFTemplateView


class index(TemplateView):
    login_required = True
    template_name = 'index.html'


@login_required
def languages(request):
    return render_to_response("language/language_list.html", {})


@login_required
def languagesDetail(request):
    return render_to_response("language/language_detail.html", {})


@login_required
def languagesQuestionList(request):
    return render_to_response("language/language_question.html", {})


@login_required
def testList(request):
    return render_to_response("test/test_list.html", {})


@login_required
def testCandidatesList(request):
    return render_to_response("test/test_candidates_list.html", {})


@login_required
def testCandidatesTestRetrieve(request):
    return render_to_response("test/test_candidates_retrieve.html", {})


class HelloPDFView(PDFTemplateView):
    template_name = "easy_pdf/test-candidate.html"

    def get_context_data(self, **kwargs):
        candidate = self.request.GET.get("candidate")
        test = self.request.GET.get('exam')
        answers = Answer.objects.filter(candidate__slug=candidate, question__exam__slug=test).order_by('question__order')
        return super(HelloPDFView, self).get_context_data(
        pagesize="A4",
        title="Hi there!",
        answers=answers,
        **kwargs)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value),
        #no user with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your TP account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return render_to_response('login.html', {'error': True}, context)
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login.html', {}, context)


def insert_question(request):
    # Like before, obtain the context for the user's request.
    answers = dict(request.POST)
    # print answers['{"answers":"text"}']
    # print request.POST.post['answers']
    for key, value in request.POST.iteritems():
        answer = key
    print ast.literal_eval(answer)[0]
    return HttpResponse(answers)
