#!/usr/bin/env python3

# Errors on absolute imports in any .py files found in the input paths

import re
import sys
from pathlib import Path


def check_for_absolute_imports(library_name: str, *dirs):
    """
    Ensures no absolute imports of the library (e.g. 'import mylib' or 'from mylib import ...')
    appear outside test files.
    """
    # only matches "from/import <library_name>", while "from/import <library-name>-other" is allowed
    abs_import_pattern = re.compile(rf"^\s*(?:from|import)\s+{re.escape(library_name)}(?=\.|\s|$)")

    errors = []
    for dir in dirs:
        dir_path = Path(dir)
        for py_file in dir_path.rglob("*.py"):
            with py_file.open() as f:
                dir_rel_path = py_file.absolute().relative_to(Path.cwd())
                for lineno, line in enumerate(f, 1):
                    if not abs_import_pattern.search(line):
                        continue
                    errors.append(f"{dir_rel_path}:{lineno}: {line.strip()}")

    if errors:
        print(f"❌ Absolute imports of {library_name} found outside tests:")
        print("\n".join(errors))
        sys.exit(1)
    else:
        print("✅ No forbidden absolute imports found.")
        sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python check_imports.py <library_name> <dirpath1> [<dirpath2>] ...")
        sys.exit(1)

    check_for_absolute_imports(sys.argv[1], *sys.argv[2:])
