#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply.

Writes a single one-line out-of-office auto-reply to entry.txt in the
output directory named by MAKEFUN_OUTPUT_DIR (default /output).

The joke: instead of the usual "limited access to email" line, the sender
hands the inbox to "Future Me" -- a very confident intern who, it turns
out, has no password. It reads like a real away message, lands on the
first read, and turns on the usual away-message trope rather than
repeating the beach / inbox / limited-email lines.
"""

import os

# The entry: one line, plain UTF-8, well inside the 1-160 character gate.
ENTRY = (
    "I'm out of office; my inbox is now in the care of Future Me, "
    "a very confident intern with no password and no plan."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
