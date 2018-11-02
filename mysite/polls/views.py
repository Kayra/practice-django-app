from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice


class IndexView(generic.ListView):

    template_name = 'polls/index.html'
    context_object_name = 'last_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

# def index(request):
#
#     latest_question_list = Question.objects.order_by('pub_date')[:5]
#     polls_index_template = 'polls/index.html'
#     template_context = {
#         'latest_question_list': latest_question_list
#     }
#
#     return render(request, polls_index_template, template_context)


class DetailView(generic.DetailView):

    model = Question
    template_name = 'polls/detail.html'

# def detail(request, question_id):
#
#     polls_detail_template = 'polls/detail.html'
#     template_context = {
#         'question': get_object_or_404(Question, pk=question_id)
#     }
#
#     return render(request, polls_detail_template, template_context)


class ResultsView(generic.DetailView):

    model = Question
    template_name = 'polls/results.html'

# def results(request, question_id):
#
#     question = get_object_or_404(Question, pk=question_id)
#     results_template = 'polls/results.html'
#     template_context = {
#         'question': question
#     }
#
#     return render(request, results_template, template_context)


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
