from dataclasses import dataclass
from pathlib import Path
from typing import Any, List, Optional, Union


@dataclass()
class Entry:
    """Entry class."""

    surf: List[str]  #: Surface form.
    reading: str  #: Reading.
    pos: str  #: Part of speech.
    subpos: str = "*"  #: Part of speech (subtype).
    conjtype: str = "*"  #: Conjugation type.
    semantics: str = "*"  #: Semantics.
    location: str = "*"  #: Location.

    def __str__(self) -> str:
        """Convert to the string."""
        return self.to_sexp()

    @classmethod
    def from_sexp(cls, sexp: Any, path: Optional[Union[str, Path]] = None) -> "Entry":
        """Create an entry from an S-expression.

        Args:
            sexp: S-expression.
            path: Path to the file.
        """
        if sexp[0] == "連語":
            raise NotImplementedError("'連語' is not supported.")
        args = {}
        pos, sexp = sexp
        args["pos"] = pos
        if isinstance(sexp[0], str):
            subpos, sexp = sexp
        else:
            subpos = "*"
        args["subpos"] = subpos
        for k, *vs in sexp:
            if k == "見出し語":
                args["surf"] = [v for v in vs if isinstance(v, str)]
                args["surf"] += [v[0] for v in vs if isinstance(v, list)]
            elif k == "読み":
                assert len(vs) == 1 and isinstance(vs[0], str)
                args["reading"] = vs[0]
            elif k == "意味情報":
                assert len(vs) == 1 and isinstance(vs[0], str)
                args["semantics"] = vs[0].strip('"')
            elif k == "活用型":
                assert len(vs) == 1 and isinstance(vs[0], str)
                args["conjtype"] = vs[0]
        if path:
            args["location"] = str(path)
        return cls(**args)

    def to_sexp(self) -> str:
        """Convert to the S-expression."""
        rv = "(" + self.pos + " ("
        if self.subpos != "*":
            rv += self.subpos + " ("
        rv += "(読み " + self.reading + ")"
        rv += "(見出し語 " + " ".join(self.surf) + ")"
        if self.conjtype != "*":
            rv += "(活用型 " + self.conjtype + ")"
        if self.semantics != "*":
            rv += "(意味情報 " + f'"{self.semantics}"' + ")"
        if self.subpos != "*":
            rv += ")"
        rv += "))"
        return rv
