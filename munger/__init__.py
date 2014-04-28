def munge(text):
    if ' ' in text:
        return ' '.join(map(munge, text.split(' ')))
    if len(text) >= 4:
        return text[0] + text[-2:0:-1] + text[-1]
    return text
