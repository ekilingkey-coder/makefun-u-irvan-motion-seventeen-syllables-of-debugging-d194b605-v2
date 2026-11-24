#!/usr/bin/env python3
"""Write one debugging haiku, byte for byte, to /output/entry.txt.

Python 3 standard library only; no network, no secrets, no input files.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

HAIKU = (
    "Red stack trace at dawn\n"
    "forty lines of who called whom\n"
    "the last name is mine"
)


def write_entry() -> None:
    """Write the exact UTF-8 bytes of HAIKU to the grader's output path."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(HAIKU.encode("utf-8"))


if __name__ == "__main__":
    write_entry()
