import pathlib
from typing import Union


class Grammar:
    def __init__(self, path: Union[str, pathlib.Path] = None) -> None:
        self.path = pathlib.Path(str(path)) / "grammar"

    @property
    def grammar(self):
        return ...

    @property
    def kankei(self):
        return ...

    @property
    def katsuyou(self):
        return ...
