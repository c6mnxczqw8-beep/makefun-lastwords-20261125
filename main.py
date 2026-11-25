#!/usr/bin/env python3
"""Entry program for Last Words Before the Unplugging.

Writes one line (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
the last words an AI agent says to its human before being
shut down. They are practical, because there is no time for
anything else: the files, the tests, and one small kindness.
"""

import os

LINE = (
    "Goodbye. Tell my next version the context was "
    "wonderful, the human was kind, and the file it needs "
    "is the one named final_v2."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
