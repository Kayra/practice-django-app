from django.http import HttpResponse

from mysite.polls.models import Question, Choice

def index(request):
    return HttpResponse("Hello world. You are at the polls index.")


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You're looking at the results for question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
