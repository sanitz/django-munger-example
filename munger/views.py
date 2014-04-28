from django.shortcuts import render


def index(request):
    text = request.POST.get('content', '')
    munged_words = []
    munged_words = [_munge_word(word) for word in text.split(' ')]

    context = {
        'munged': ' '.join(munged_words),
        'txt': text
    }
    return render(request, 'munged.html', context)


def _munge_word(text):
    if len(text) >= 4:
        return text[0] + text[-2:0:-1] + text[-1]
    return text
