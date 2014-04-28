from munger import munge


def test_leaves_short_words_unchanged():
    assert munge('abc') == 'abc'


def test_reverses_middle_in_longer_words():
    assert munge('abcd') == 'acbd'


def test_munges_sentence_word_by_word():
    assert munge('abc abc') == 'abc abc'
