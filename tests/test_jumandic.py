from tinydb import Query

from jumandic import JumanDIC
from jumandic.dic.entries import ContentWord


def test_init():
    _ = JumanDIC()


def test_ContentW():
    jumandic = JumanDIC()
    assert len(jumandic.dic.ContentW) == 31952


def test_ContentW_all():
    jumandic = JumanDIC()
    content_words = jumandic.dic.ContentW.all()
    assert len(content_words) == 31952
    assert all(isinstance(c, ContentWord) for c in content_words)


def test_ContentW_get():
    jumandic = JumanDIC()
    content_word = jumandic.dic.ContentW.get(doc_id=0)
    assert content_word is None


def test_ContentW_iter():
    jumandic = JumanDIC()
    for content_word in jumandic.dic.ContentW:
        isinstance(content_word, ContentWord)


def test_ContentW_search():
    jumandic = JumanDIC()
    content_words = jumandic.dic.ContentW.search(Query().pos == "名詞")
    assert len(content_words) == 22562
    assert all(isinstance(c, ContentWord) for c in content_words)
