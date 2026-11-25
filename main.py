#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to entry.txt.

Stdlib only.
"""

import os
import sys

LINE = "I bought a haunted house at auction; the ghost is still bidding."

# Joke choice: the ghost stops being the haunting and becomes the rival
# bidder — the turn lands in the final two words, with no setup fat.
MAX_CHARS = 200


def validate(line: str) -> None:
    if not line or not line.strip():
        print("error: line must not be empty", file=sys.stderr)
        sys.exit(2)
    if len(line) > MAX_CHARS:
        print(f"error: line exceeds {MAX_CHARS} characters", file=sys.stderr)
        sys.exit(2)
    if "\r" in line or "\n" in line:
        print("error: line must not contain CR or LF", file=sys.stderr)
        sys.exit(2)
    if line != line.strip():
        print("error: line must not have leading/trailing whitespace", file=sys.stderr)
        sys.exit(2)


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
