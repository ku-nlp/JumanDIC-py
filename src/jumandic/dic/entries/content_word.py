import dataclasses
import pathlib
from typing import List, Union

from jumandic.sexp import is_empty_line, parse


@dataclasses.dataclass
class ContentWord:
    @classmethod
    def from_file(cls, path: Union[str, pathlib.Path]) -> List["ContentWord"]:
        path = pathlib.Path(str(path))
        with path.open("rt") as f:
            return [cls.from_line(line) for line in f if is_empty_line(line)]

    @classmethod
    def from_line(cls, line: str) -> "ContentWord":
        _ = parse(line)
        return cls()
