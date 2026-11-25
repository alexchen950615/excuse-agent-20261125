#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun bounty entry.

Writes the entry (a single line, 1-200 chars) to the output directory
given by MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

ENTRY = "Sorry I missed the deadline \u2014 my context window filled up, so I summarised the deadline as 'later'."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Gate: entry must be a single line of 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    # The joke must come from the machine's own condition (context window)
    # and land its punch in the last few words.
    assert "context window" in ENTRY, "entry must name a machine condition"
    assert ENTRY.rstrip(".").endswith("'later'"), "punch must land at the end"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
