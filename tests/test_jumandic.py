import pytest
from tinydb import Query

from jumandic import JumanDIC
from jumandic.entry import Entry


def test_init():
    _ = JumanDIC()


def test_init_error():
    with pytest.raises(FileNotFoundError):
        _ = JumanDIC(path="not_a_path")


def test_len():
    jumandic = JumanDIC()
    assert len(jumandic) == 31952


def test_iter():
    jumandic = JumanDIC()
    for entry in jumandic:
        isinstance(entry, Entry)


def test_all():
    jumandic = JumanDIC()
    entries = jumandic.all()
    assert len(entries) == 31952
    assert all(isinstance(entry, Entry) for entry in entries)


def test_search():
    jumandic = JumanDIC()
    entries = jumandic.search(Query().pos == "名詞")
    assert len(entries) == 22562
    assert all(isinstance(e, Entry) for e in entries)
