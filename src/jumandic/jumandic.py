from dataclasses import asdict
from logging import getLogger
from pathlib import Path
from typing import Iterator, List, Optional, Union

from tinydb import TinyDB
from tinydb.queries import QueryLike
from tinydb.storages import MemoryStorage

from jumandic.entry import Entry
from jumandic.sexp import parse
from jumandic.utils import DuplicateFilter

logger = getLogger(__name__)
logger.addFilter(DuplicateFilter())


class JumanDIC(TinyDB):
    """JumanDIC API.

    Args:
        path: Path to the JumanDIC repository.

    Example::

        # Create a JumanDIC object.
        from jumandic import JumanDIC
        d = JumanDIC()

        # Iterate over entries
        for entry in d:
            ...

        # Search entries
        from tinydb import Query
        q = Query()
        nouns = d.search(q.pos == "名詞")
    """

    def __init__(self, path: Optional[Union[str, Path]] = None) -> None:
        super().__init__(storage=MemoryStorage)
        if path is None:
            self.path = Path(__file__).parent / "data" / "JumanDIC"
        else:
            self.path = Path(path)
        if self.path.is_dir():
            for path in self.path.glob("**/*.dic"):
                self.add_dictionary(path)
        elif self.path.is_file():
            self.add_dictionary(self.path)
        else:
            raise FileNotFoundError(f"File or directory not found: {self.path}")

    def export(self, path: Union[str, Path]) -> None:
        """Export entries to a file.

        Args:
            path: Path to the file.
        """
        buff = "\n".join([entry.to_sexp() for entry in self.all()])
        with open(path, "w") as f:
            f.write(buff)

    def add_dictionary(self, path: Union[str, Path]) -> None:
        """Add entries in a dictionary.

        Args:
            path: Path to the dictionary.
        """
        entries = []
        with open(path) as f:
            try:
                sexps = parse(f.read())
            except Exception as e:
                logger.error(f"Failed to parse {path}: {e}")
                return
            for sexp in sexps:
                try:
                    entries.append(asdict(Entry.from_sexp(sexp, path)))
                except NotImplementedError as e:
                    logger.warning(f"Failed to parse an entry in {path}: {e}")
                except Exception as e:
                    logger.error(f"Failed to parse an entry in {path}: {e}")
        self.insert_multiple(entries)

    def all(self) -> List[Entry]:
        """Return all entries."""
        return [Entry(**doc) for doc in super().__getattr__("all")()]

    def get(self, cond: Optional[QueryLike] = None, doc_id: Optional[int] = None) -> Optional[Entry]:
        """Get an entry."""
        doc = super().__getattr__("get")(cond, doc_id)
        if doc is None:
            return None
        return Entry(**doc)

    def search(self, cond: QueryLike) -> List[Entry]:
        """Search entries."""
        return [Entry(**doc) for doc in super().__getattr__("search")(cond)]

    def __iter__(self) -> Iterator[Entry]:
        """Iterate over entries."""
        for doc in super().__iter__():
            yield Entry(**doc)
