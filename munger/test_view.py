def test_munging(client):
    response = client.post('/', {'content': '1234'})
    assert response.context['munged'] == '1324'


def test_leaves_short_words_unchanged(client):
    response = client.post('/', {'content': 'abc'})
    assert response.context['munged'] == 'abc'


def test_reverses_middle_in_longer_words(client):
    response = client.post('/', {'content': 'abcd'})
    assert response.context['munged'] == 'acbd'


def test_munges_sentence_word_by_word(client):
    response = client.post('/', {'content': 'a bc'})
    assert response.context['munged'] == 'a bc'
