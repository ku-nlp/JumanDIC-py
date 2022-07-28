import pathlib
from typing import Optional, Union

from jumandic.dic import Dic
from jumandic.grammar import Grammar


class JumanDIC:
    def __init__(self, path: Optional[Union[str, pathlib.Path]] = None) -> None:
        if path is None:
            path = str(pathlib.Path(__file__).parent / "data" / "JumanDIC")
        self.path = pathlib.Path(path)
        self.dic = Dic(self.path)
        self.grammar = Grammar(self.path)
