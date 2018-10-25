from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question, Choice


def index(request):

    latest_question_list = Question.objects.order_by('pub_date')[:5]
    polls_index_template = 'polls/index.html'
    context = {
        'latest_question_list': latest_question_list
    }

    return render(request, polls_index_template, context)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You're looking at the results for question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
