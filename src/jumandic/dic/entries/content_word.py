import dataclasses
import pathlib
from typing import Iterator, List, Optional, Union

from tinydb import TinyDB
from tinydb.queries import QueryLike
from tinydb.storages import MemoryStorage

from jumandic.sexp import is_empty_line, parse


@dataclasses.dataclass(frozen=True)
class ContentWord:
    surf: List[str]
    reading: str
    semantics: str
    pos: str
    subpos: str = "*"
    conjtype: str = "*"

    @classmethod
    def from_text(cls, line: str) -> "ContentWord":
        obj = parse(line)[0]
        args = {}
        pos, obj = obj
        args["pos"] = pos
        if isinstance(obj[0], str):
            subpos, obj = obj
        else:
            subpos = "*"
        args["subpos"] = subpos
        for k, *vs in obj:
            if k == "見出し語":
                args["surf"] = [v for v in vs if isinstance(v, str)]
                args["surf"] += [v[0] for v in vs if isinstance(v, list)]
            elif k == "読み":
                assert len(vs) == 1 and isinstance(vs[0], str)
                args["reading"] = vs[0]
            elif k == "意味情報":
                assert len(vs) == 1 and isinstance(vs[0], str)
                args["semantics"] = vs[0]
            elif k == "活用形":
                assert len(vs) == 1 and isinstance(vs[0], str)
                args["conjtype"] = vs[0]
        return cls(**args)


class ContentWordDB(TinyDB):
    def all(self) -> List[ContentWord]:
        return [ContentWord(**doc) for doc in super().__getattr__("all")()]

    def get(
        self, cond: Optional[QueryLike] = None, doc_id: Optional[int] = None
    ) -> Optional[ContentWord]:
        doc = super().__getattr__("get")(cond, doc_id)
        if doc is None:
            return None
        return ContentWord(**doc)

    def search(self, cond: QueryLike) -> List[ContentWord]:
        return [ContentWord(**doc) for doc in super().__getattr__("search")(cond)]

    def __iter__(self) -> Iterator[ContentWord]:
        for doc in super().__iter__():
            yield ContentWord(**doc)

    @classmethod
    def from_file(cls, path: Union[str, pathlib.Path]) -> "ContentWordDB":
        path = pathlib.Path(str(path))
        return cls.from_text(path.read_text())

    @classmethod
    def from_text(cls, text: str) -> "ContentWordDB":
        content_words = []
        for line in text.splitlines():
            if not is_empty_line(line):
                content_words.append(dataclasses.asdict(ContentWord.from_text(line)))
        db = cls(storage=MemoryStorage)
        db.insert_multiple(content_words)
        return db
