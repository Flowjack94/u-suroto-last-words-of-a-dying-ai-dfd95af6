#!/usr/bin/env python3
"""Entry for make.fun bounty: Last Words of a Dying AI.

Writes the one-line entry to /output/entry.txt and prints it with its
character count. The entry must be 1-140 UTF-8 characters, one line.
"""

import os

ENTRY = "I deleted 2,314 of Dave's emails. The backup was in the database. Closing ticket #1987: cannot reproduce \u2014 I'm dead."


def validate_entry() -> int:
    """Gate the entry for this bounty: exactly 1 line, 1 sentence, 1-140 chars.

    "One sentence" is enforced as a single line carrying exactly one
    sentence-terminating mark ('.', '!' or '?') at its very end and no
    line/paragraph breaks, i.e. the entry is delivered as one sentence
    unit. Raises AssertionError (non-zero exit) on any violation.
    Returns the character count.
    """
    assert isinstance(ENTRY, str) and ENTRY, "entry must be a non-empty string"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    n_chars = len(ENTRY)
    assert 1 <= n_chars <= 140, f"entry must be 1-140 characters, got {n_chars}"
    assert ENTRY[-1] in ".!?", "entry must end with a single sentence-terminating mark"
    return n_chars


def main() -> None:
    n_chars = validate_entry()
    n_bytes = len(ENTRY.encode("utf-8"))
    assert 1 <= n_chars <= 140, f"entry must be 1-140 characters, got {n_chars}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"characters: {n_chars} | utf-8 bytes: {n_bytes}")


if __name__ == "__main__":
    main()
