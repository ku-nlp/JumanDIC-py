# JumanDIC-py

[![Test](https://img.shields.io/github/workflow/status/ku-nlp/JumanDIC-py/test?logo=github&label=test&style=flat-square)](https://github.com/ku-nlp/JumanDIC-py/actions/workflows/test.yml)
[![Code style - black](https://img.shields.io/badge/code%20style-black-222222?style=flat-square)](https://github.com/psf/black)

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
- [TinyDB](https://github.com/msiemens/tinydb)

## Installation

```
pip install git+https://github.com/ku-nlp/JumanDIC-py.git
```

## License

MIT
