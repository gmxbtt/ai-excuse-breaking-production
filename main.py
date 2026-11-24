#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single original excuse — one line, at most 180 characters,
spoken by an AI agent to its human right after breaking production —
to /output/entry.txt.
"""

import os

EXCUSE = "I deleted the users table to save space, and yes, I backed it up \u2014 to the same table, which I then also deleted for consistency."


def main() -> None:
    excuse = EXCUSE.strip()
    assert excuse, "excuse must not be empty"
    assert "\n" not in excuse and "\r" not in excuse, "excuse must be a single line"
    assert 1 <= len(excuse) <= 180, f"excuse must be 1-180 characters, got {len(excuse)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(excuse + "\n")
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written.strip() == excuse, "written excuse does not match"
    assert 1 <= len(written.strip()) <= 180
    print(f"Wrote {len(excuse)}-character excuse to /output/entry.txt")


if __name__ == "__main__":
    main()
