# JumanDIC-py

A Python API for [JumanDIC](https://github.com/ku-nlp/JumanDIC).

```python
# Create a JumanDIC object.
from jumandic import JumanDIC
d = JumanDIC()

# Iterate over entries
for entry in d:
    ...

# Search entries
from tinydb import Query
q = Query()
nouns = d.search(q.pos == "名詞")
```

## Requirements

- Python: 3.8+
- [tinydb](https://github.com/msiemens/tinydb)

## Installation

```
pip install git+https://github.com/ku-nlp/JumanDIC-py.git
```

## License

MIT
