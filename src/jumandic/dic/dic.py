import pathlib
from typing import Union

from jumandic.dic.entries import ContentWordDB


class Dic:
    def __init__(self, path: Union[str, pathlib.Path]) -> None:
        self.path = pathlib.Path(str(path)) / "dic"
        self.content_words = ContentWordDB.from_file(self.path / "ContentW.dic")

    @property
    def Assert(self):
        raise NotImplementedError

    @property
    def AuxV(self):
        raise NotImplementedError

    @property
    def ContentW(self) -> ContentWordDB:
        return self.content_words

    @property
    def Demonstrative(self):
        raise NotImplementedError

    @property
    def Lexicon_from_rengo(self):
        raise NotImplementedError

    @property
    def Noun_hukusi(self):
        raise NotImplementedError

    @property
    def Noun_keishiki(self):
        raise NotImplementedError

    @property
    def Noun_koyuu(self):
        raise NotImplementedError

    @property
    def Noun_suusi(self):
        raise NotImplementedError

    @property
    def Postp(self):
        return ...

    @property
    def Prefix(self):
        raise NotImplementedError

    @property
    def Rendaku(self):
        raise NotImplementedError

    @property
    def Rengo(self):
        raise NotImplementedError

    @property
    def Special(self):
        raise NotImplementedError

    @property
    def Suffix(self):
        raise NotImplementedError

    @property
    def Townname(self):
        raise NotImplementedError
