from anagram import anagrams, read_word_list


def test_read_word_list():
    assert len(read_word_list()) == 45425


def test_anagrams():
    assert len(anagrams('documenting', read_word_list())) == 12

