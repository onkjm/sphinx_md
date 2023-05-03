# sphinx_md
sample of document site created with .md and recursive search

## prerequisite

- sphinx
- myst-parser

## Usage

- create sphinx project by `sphinx-quickstart` command.
- edit `conf.py` to import `utils.py` and execute `create_index_rst()` at the beginning of `conf.py`

```
import os
import sys
sys.path += [os.getcwd()]

import utils
utils.create_index_rst()
```

- add `extensions = ['myst_parser']` (necessary for dealing with `.md` files)

- put `utils.py` in source dir.
- create documents and execute `make build`. `create_index_rst()` will recursively search the source dirs and generate `.rst` files.

In this sample, the documents under `topic1` and `topic2` are recursivey searched and the following files are generated.
- index.rst
- topic1.rst
- topic1-3.rst
- topoc2.rst

Users just add directories and `.md` files and hit `make html`, then, the new directories and files are took in account automatically.

## note
The template of each `.rst` is embedded in `utils.py` as code, so that you have to edit `utils.py` when you want to change the template.

There should be better way to do this... (or the ideal way may be already delivered in somewhere...)
