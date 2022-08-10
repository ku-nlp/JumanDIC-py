from typing import List

import pytest
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


@pytest.mark.parametrize(
    "index, surf, reading, pos, subpos, conjtype, semantics",
    [
        (0, ["ああ"], "ああ", "感動詞", "*", "*", '"代表表記:ああ/ああ"'),
        (4, ["相容れない", "あい容れない", "相いれない", "あいいれない"], "あいいれない", "形容詞", "*", "イ形容詞アウオ段", '"代表表記:相容れない/あいいれない"'),
    ],
)
def test_ContentW_item(
    index: int, surf: List[str], reading: str, pos: str, subpos: str, conjtype: str, semantics: str
) -> None:
    jumandic = JumanDIC()
    content_words = [w for w in jumandic.dic.ContentW]
    content_word = content_words[index]
    assert content_word.surf == surf
    assert content_word.reading == reading
    assert content_word.pos == pos
    assert content_word.subpos == subpos
    assert content_word.conjtype == conjtype
    assert content_word.semantics == semantics
