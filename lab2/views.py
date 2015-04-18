from django.shortcuts import render


def submit_album(request):
    context_dict = {}
    return render(request, 'lab2/submit_album.html', context_dict)