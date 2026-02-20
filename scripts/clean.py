#!/usr/bin/env -S uv run --active --script --quiet
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "from-root>=1.3.0",
# ]
# ///

from shutil import rmtree
from from_root import from_root

file = from_root("main.spec")
file.unlink(missing_ok=True)

for name in ("dist", "build"):
    directory = from_root(name)
    rmtree(directory, ignore_errors=True)