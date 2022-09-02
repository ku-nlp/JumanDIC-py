import tempfile

import pytest
from tinydb import Query

from jumandic import JumanDIC
from jumandic.entry import Entry


@pytest.fixture
def jumandic():
    return JumanDIC()


def test_init(jumandic: JumanDIC):
    pass


def test_len(jumandic: JumanDIC):
    assert len(jumandic) == 151861


def test_iter(jumandic: JumanDIC):
    for entry in jumandic:
        isinstance(entry, Entry)


def test_all(jumandic: JumanDIC):
    entries = jumandic.all()
    assert len(entries) == 151861
    assert all(isinstance(entry, Entry) for entry in entries)


def test_search(jumandic: JumanDIC):
    entries = jumandic.search(Query().pos == "名詞")
    assert len(entries) == 103904
    assert all(isinstance(e, Entry) for e in entries)


def test_export(jumandic: JumanDIC):
    with tempfile.NamedTemporaryFile() as f:
        jumandic.export(f.name)
        assert len(jumandic) == len(JumanDIC(f.name))
