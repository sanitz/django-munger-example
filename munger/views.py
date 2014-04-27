from django.shortcuts import render


def munge(request):
    txt = request.POST.get('content', '')
    if len(txt) <= 3:
        munged = txt
    else:
        munged = txt[0] + txt[-2:0:-1] + txt[-1]
    context = {
        'munged': munged,
        'txt': txt
    }
    return render(request, 'munged.html', context)
