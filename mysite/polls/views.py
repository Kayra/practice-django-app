from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from polls.models import Question, Choice


def index(request):

    latest_question_list = Question.objects.order_by('pub_date')[:5]
    polls_index_template = 'polls/index.html'
    template_context = {
        'latest_question_list': latest_question_list
    }

    return render(request, polls_index_template, template_context)


def detail(request, question_id):

    polls_detail_template = 'polls/detail.html'
    template_context = {
        'question': get_object_or_404(Question, pk=question_id)
    }

    return render(request, polls_detail_template, template_context)


def results(request, question_id):
    return HttpResponse(f"You're looking at the results for question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
