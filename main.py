"""Write a one-line joke about working beside AI coding agents.

The program is deterministic: it always writes the same bytes to
/output/entry.txt, with no network access and no input beyond the
joke text below.
"""

from __future__ import annotations

import os
import sys

JOKE = (
    "My coding agent fixed the bug, apologised for the fix, "
    "then fixed the apology \u2014 now the demo is just it "
    "saying sorry in a loop."
)

MAX_CHARS = 280
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Check the joke fits the competition gate before writing it."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"joke must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if any(ord(char) < 0x20 for char in text):
        raise ValueError("joke must not contain control characters")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> int:
    validate(JOKE)
    output_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(output_dir, exist_ok=True)
    # Write to a temporary file first, then move it into place, so a
    # failed run never leaves a half-written entry behind.
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    os.replace(tmp_path, OUTPUT_PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
