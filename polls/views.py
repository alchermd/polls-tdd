from django.shortcuts import render


def polls_index(request):
    return render(request, 'polls/index.html')
