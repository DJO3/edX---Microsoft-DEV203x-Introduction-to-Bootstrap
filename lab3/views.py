from django.shortcuts import render


def modal(request):
    context_dict = {}
    return render(request, 'lab3/modal.html', context_dict)


def final(request):
    context_dict = {}
    return render(request, 'lab3/final.html', context_dict)