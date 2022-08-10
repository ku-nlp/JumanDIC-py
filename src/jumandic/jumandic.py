from dataclasses import asdict
from pathlib import Path
from typing import Iterator, List, Optional, Union

from tinydb import TinyDB
from tinydb.queries import QueryLike
from tinydb.storages import MemoryStorage

from jumandic.entry import Entry
from jumandic.sexp import parse


class JumanDIC(TinyDB):
    """JumanDIC API.

    Args:
        path: Path to the JumanDIC repository.

    Example::

        from jumandic import JumanDIC
        from tinydb import Query

        d = JumanDIC()
        q = Query()

        # Find nouns:
        nouns = d.search(q.pos == "名詞")
    """

    def __init__(self, path: Optional[Union[str, Path]] = None) -> None:
        super().__init__(storage=MemoryStorage)
        if path is None:
            path = Path(__file__).parent / "data" / "JumanDIC"
        else:
            path = Path(path)
        self.add_dictionary(path / "dic/ContentW.dic")

    def add_dictionary(self, path: Union[str, Path]) -> None:
        """Add a dictionary to the JumanDIC repository.

        Args:
            path: Path to the dictionary.
        """
        entries = []
        with open(path) as f:
            for entry in parse(f.read()):
                entries.append(asdict(Entry.from_sexp(entry)))
        self.insert_multiple(entries)

    def all(self) -> List[Entry]:
        return [Entry(**doc) for doc in super().__getattr__("all")()]

    def get(self, cond: Optional[QueryLike] = None, doc_id: Optional[int] = None) -> Optional[Entry]:
        doc = super().__getattr__("get")(cond, doc_id)
        if doc is None:
            return None
        return Entry(**doc)

    def search(self, cond: QueryLike) -> List[Entry]:
        return [Entry(**doc) for doc in super().__getattr__("search")(cond)]

    def __iter__(self) -> Iterator[Entry]:
        for doc in super().__iter__():
            yield Entry(**doc)
