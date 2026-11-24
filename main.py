#!/usr/bin/env python3
"""Entry for make.fun "Everyday Things, Two Lines, Longer Run".

Writes a two-line explanation of a queue to entry.txt in the output
directory given by MAKEFUN_OUTPUT_DIR (default /output). Line 1 explains a queue to a 10-year-old with one
concrete, surprising analogy (a human train). Line 2 says why that
analogy works: what it maps and what it leaves out.

Deterministic, stdlib only, no network, no randomness.
"""

import os

ENTRY_TEXT = (
    "A queue is a human train: every person is a carriage hooked onto the one in front, "
    "and the whole line only rolls forward when the engine at the front moves.\n"
    "The train picture works because each person follows the one ahead, the way each "
    "carriage follows the one ahead of it, but it leaves out that people can step out "
    "of line or swap places, and carriages never can."
)


def validate(text: str) -> None:
    """Check the sealed gate: UTF-8 text, 1-400 chars, not only whitespace,
    exactly two lines."""
    encoded = text.encode("utf-8")  # raises if not valid UTF-8 text
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry must be 1-400 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly two lines, got {len(lines)}")
    if any(not line.strip() for line in lines):
        raise ValueError("each line must contain non-whitespace text")
    if any(line != line.strip() for line in lines):
        raise ValueError("lines must not have leading or trailing whitespace")
    if text.endswith("\n"):
        raise ValueError("entry must not end with a trailing newline")
    if len(encoded) > 400:
        raise ValueError(f"entry must be at most 400 bytes, got {len(encoded)}")


def main() -> None:
    validate(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)
    print(f"Wrote {out_path} ({len(ENTRY_TEXT)} characters, 2 lines)")


if __name__ == "__main__":
    main()
