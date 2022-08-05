# JumanDIC-py

A Python API for JumanDIC.

```python
import jumandic

# Create a JumanDIC instance.
d = jumandic.JumanDIC()

# Iterate over the entries in the dictionary.
for content_word in d.dic.ContentW:
    print(content_word.surf)       # Surface form(s).
    print(content_word.reading)    # Reading.
    print(content_word.pos)        # Part of speech.
    print(content_word.subpos)     # Part of speech (subtype).
    print(content_word.conjtype)   # Conjugation type.
    print(content_word.semantics)  # Semantics.
    break

# Search for nouns.
from tinydb import Query
q = Query()
nouns = d.dic.ContentW.search(q.pos == "名詞")

# Search for words with the surface form "あく".
akus = d.dic.ContentW.search(q.surf.any(["あく"]))

# Search for nouns with the surface form "あく".
aku_nouns = d.dic.ContentW.search((q.surf.any(["あく"])) & (q.pos == "名詞"))
```
