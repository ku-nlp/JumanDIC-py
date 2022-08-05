import dataclasses
import pathlib
from collections import UserList
from typing import List, Union

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


class ContentWordList(UserList[ContentWord]):
    @classmethod
    def from_file(cls, path: Union[str, pathlib.Path]) -> "ContentWordList":
        path = pathlib.Path(str(path))
        return cls.from_text(path.read_text())

    @classmethod
    def from_text(cls, text: str) -> "ContentWordList":
        content_word_list = []
        for line in text.splitlines():
            if not is_empty_line(line):
                content_word_list.append(ContentWord.from_text(line))
        return cls(content_word_list)
