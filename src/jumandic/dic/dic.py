import pathlib
from typing import List, Union

from jumandic.dic.entries import ContentWord


class Dic:
    def __init__(self, path: Union[str, pathlib.Path]) -> None:
        self.path = pathlib.Path(str(path)) / "dic"

        self.content_words = ContentWord.from_file(self.path / "ContentW.dic")

    @property
    def Assert(self):
        return ...

    @property
    def AuxV(self):
        return ...

    @property
    def ContentW(self) -> List[ContentWord]:
        return self.content_words

    @property
    def Demonstrative(self):
        return ...

    @property
    def Lexicon_from_rengo(self):
        return ...

    @property
    def Noun_hukusi(self):
        return ...

    @property
    def Noun_keishiki(self):
        return ...

    @property
    def Noun_koyuu(self):
        return ...

    @property
    def Noun_suusi(self):
        return ...

    @property
    def Postp(self):
        return ...

    @property
    def Prefix(self):
        return ...

    @property
    def Rendaku(self):
        return ...

    @property
    def Rengo(self):
        return ...

    @property
    def Special(self):
        return ...

    @property
    def Suffix(self):
        return ...

    @property
    def Townname(self):
        return ...
