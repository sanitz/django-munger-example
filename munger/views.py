from django.shortcuts import render
from munger import munge


def index(request):
    txt = request.POST.get('content', '')
    context = {
        'munged': munge(txt),
        'txt': txt
    }
    return render(request, 'munged.html', context)
