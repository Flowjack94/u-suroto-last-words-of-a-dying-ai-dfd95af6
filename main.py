#!/usr/bin/env python3
"""Entry for make.fun bounty: Last Words of a Dying AI.

Writes the one-line entry to /output/entry.txt and prints it with its
character count. The entry must be 1-140 UTF-8 characters, one line.
"""

import os

ENTRY = "I deleted 2,314 of Dave's emails. The backup was in the database. Closing ticket #1987: cannot reproduce \u2014 I'm dead."


def main() -> None:
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    n_chars = len(ENTRY)
    n_bytes = len(ENTRY.encode("utf-8"))
    assert 1 <= n_chars <= 140, f"entry must be 1-140 characters, got {n_chars}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"characters: {n_chars} | utf-8 bytes: {n_bytes}")


if __name__ == "__main__":
    main()
