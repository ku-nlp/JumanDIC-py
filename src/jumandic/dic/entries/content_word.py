import dataclasses
import pathlib
from typing import List, Union

from jumandic.utils import is_valid_line


@dataclasses.dataclass
class ContentWord:
    @classmethod
    def from_file(cls, path: Union[str, pathlib.Path]) -> List["ContentWord"]:
        path = pathlib.Path(str(path))
        with path.open("rt") as f:
            return [cls.from_line(line) for line in f if is_valid_line(line)]

    @classmethod
    def from_line(cls, line: str) -> "ContentWord":
        return cls()
