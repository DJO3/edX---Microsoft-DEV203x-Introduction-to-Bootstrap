from django.shortcuts import render


def album_details(request):
    context_dict = {}
    return render(request, 'lab1/album_details.html', context_dict)