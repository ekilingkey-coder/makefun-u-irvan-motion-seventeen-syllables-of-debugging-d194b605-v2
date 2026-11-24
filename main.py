#!/usr/bin/env python3
"""Write one debugging haiku, byte for byte, to /output/entry.txt.

Python 3 standard library only; no network, no secrets, no input files.
"""

import argparse
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


def check_entry() -> bool:
    """Read /output/entry.txt back and report whether it matches HAIKU exactly."""
    expected = HAIKU.encode("utf-8")
    actual = OUTPUT_PATH.read_bytes()
    if actual == expected:
        print("match: /output/entry.txt is byte-identical to HAIKU")
        return True
    print("MISMATCH: /output/entry.txt differs from HAIKU")
    print("  expected bytes:", len(expected), "actual bytes:", len(actual))
    return False


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="read back /output/entry.txt and report byte-for-byte match",
    )
    args = parser.parse_args()
    if args.check:
        ok = check_entry()
    else:
        write_entry()
        ok = True
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
