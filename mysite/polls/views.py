from django.http import HttpResponse
from django.template import loader

from polls.models import Question, Choice


def index(request):

    latest_question_list = Question.objects.order_by('pub_date')[:5]
    index_template = loader.get_template('polls/index.html')

    context = {
        'latest_question_list': latest_question_list
    }

    return HttpResponse(index_template.render(context, request))


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You're looking at the results for question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
