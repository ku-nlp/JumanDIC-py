from dataclasses import dataclass
from typing import Any, List


@dataclass()
class Entry:
    """Entry class."""

    surf: List[str]  #: Surface form.
    reading: str  #: Reading.
    pos: str = "*"  #: Part of speech.
    subpos: str = "*"  #: Part of speech (subtype).
    conjtype: str = "*"  #: Conjugation type.
    semantics: str = ""  #: Semantics.

    @classmethod
    def from_sexp(cls, obj: Any) -> "Entry":
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
            elif k == "活用型":
                assert len(vs) == 1 and isinstance(vs[0], str)
                args["conjtype"] = vs[0]
        return cls(**args)
