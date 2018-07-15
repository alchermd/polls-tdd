from django.shortcuts import get_object_or_404, render

from .models import Question


def polls_index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'polls/index.html', context={'questions': questions})


def polls_show(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/show.html', context={'question': question})
