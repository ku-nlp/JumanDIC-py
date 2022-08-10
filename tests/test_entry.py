from textwrap import dedent
from typing import Any

import pytest

from jumandic.entry import Entry
from jumandic.sexp import parse

sexps = parse(
    dedent(
        """\
        (名詞 (普通名詞 ((読み あい)(見出し語 愛 (あい 1.6))(意味情報 "代表表記:愛/あい 漢字読み:音 カテゴリ:抽象物"))))
        (形容詞 ((読み あいいれない)(見出し語 相容れない あい容れない 相いれない あいいれない)(活用型 イ形容詞アウオ段)(意味情報 "代表表記:相容れない/あいいれない")))
        (動詞 ((読み あいする)(見出し語 愛する あいする)(活用型 サ変動詞)(意味情報 "代表表記:愛する/あいする 反義:動詞:憎む/にくむ")))
        """
    )
)


@pytest.mark.parametrize("sexp", sexps)
def test_from_sexp(sexp: Any) -> None:
    _ = Entry.from_sexp(sexp)


@pytest.mark.parametrize("sexp", sexps)
def test_to_sexp(sexp: Any) -> None:
    entry = Entry.from_sexp(sexp)
    assert entry == Entry.from_sexp(parse(entry.to_sexp())[0])


def test_attribute_0():
    entry = Entry.from_sexp(sexps[0])
    assert entry.surf == ["愛", "あい"]
    assert entry.reading == "あい"
    assert entry.pos == "名詞"
    assert entry.subpos == "普通名詞"
    assert entry.conjtype == "*"
    assert entry.semantics == "代表表記:愛/あい 漢字読み:音 カテゴリ:抽象物"


def test_attribute_1():
    entry = Entry.from_sexp(sexps[1])
    assert entry.surf == ["相容れない", "あい容れない", "相いれない", "あいいれない"]
    assert entry.reading == "あいいれない"
    assert entry.pos == "形容詞"
    assert entry.subpos == "*"
    assert entry.conjtype == "イ形容詞アウオ段"
    assert entry.semantics == "代表表記:相容れない/あいいれない"


def test_attribute_2():
    entry = Entry.from_sexp(sexps[2])
    assert entry.surf == ["愛する", "あいする"]
    assert entry.reading == "あいする"
    assert entry.pos == "動詞"
    assert entry.subpos == "*"
    assert entry.conjtype == "サ変動詞"
    assert entry.semantics == "代表表記:愛する/あいする 反義:動詞:憎む/にくむ"
