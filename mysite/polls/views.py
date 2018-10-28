from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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

    question = get_object_or_404(Quetion, pk=question_id)
    results_template = 'polls/results.html'
    template_context = {
        'question': question
    }

    return render(request, results_template, template_context)


def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):

        polls_detail_template = 'polls/detail.html'
        template_context = {
            'question': question,
            'error_message': "You didn't select a choice."
        }

        return render(request, polls_detail_template, template_context)

    else:

        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
