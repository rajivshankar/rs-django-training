# myproject/polls/views.py
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
# from django.template import RequestContext
# from django.template import loader
# from django.http import HttpResponse
# from django.http import Http404

from .models import Choice
from .models import Question

# def index (request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template("polls/index.html")
#     output = ', '.join([p.question_text for p in latest_question_list])
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last 5 published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).\
            order_by('-pub_date')[:5]

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question':question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question':question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)    
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the voting Form
        return render(
                      request,
                      'polls/detail.html',
                      {
                       'question': p,
                       'error_message': "You didn't select a choice",
                       }
                      )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always retuurn an HTTPResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits a back button
        return HttpResponseRedirect(reverse('polls:results', args = (p.id,)))