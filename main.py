#!/usr/bin/env python3
"""The Robot Pickup Line Championship -- entry program.

Writes one original robot pickup line to /output/entry.txt.
Python standard library only, deterministic, no network access.
"""

import os

LINE = "I don't have a heart, but my error logs are full of you."


def main() -> None:
    line = LINE.strip()
    if not (1 <= len(line) <= 200):
        raise SystemExit(
            "entry must be 1-200 characters, got %d" % len(line)
        )
    if not line.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line)


if __name__ == "__main__":
    main()
