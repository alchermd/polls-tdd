from django.shortcuts import render

from .models import Question


def polls_index(request):
    return render(request, 'polls/index.html', context={'questions': Question.objects.all()})


def polls_show(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'polls/show.html', context={'question': question})
