# JumanDIC-py

A Python API for [JumanDIC](https://github.com/ku-nlp/JumanDIC).

```python
import jumandic

# Create a JumanDIC instance.
d = jumandic.JumanDIC()

# Iterate over the entries in the dictionary.
for entry in d:
    print(entry.surf)  # Surface form(s).
    print(entry.reading)  # Reading.
    print(entry.pos)  # Part of speech.
    print(entry.subpos)  # Part of speech (subtype).
    print(entry.conjtype)  # Conjugation type.
    print(entry.semantics)  # Semantics.
    break

# Search for nouns.
from tinydb import Query

q = Query()
nouns = d.search(q.pos == "名詞")
```
