from typing import Any

import pytest

from jumandic.sexp import parse


@pytest.mark.parametrize(
    "input_text, expected",
    [
        (r"(名詞 (見出し語 犬)(意味情報))", [["名詞", ["見出し語", "犬"], ["意味情報"]]]),
    ],
)
def test_parse(input_text: str, expected: Any) -> None:
    assert parse(input_text) == expected
