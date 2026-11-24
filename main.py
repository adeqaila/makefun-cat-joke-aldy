#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands - slot 1 entry.

Writes a single cat joke (one line, under 200 characters) to
/output/entry.txt. Deterministic, no network, no input files.

Competition: u-aldy998-the-one-line-cat-joke-that-lands-a7b18262
Reward: $2 (1st place only). Deadline: 2026-11-26T15:40:00Z.
Gate: /output/entry.txt must be UTF-8 text, 1-200 characters.
"""

import os
from pathlib import Path

# Winner of the internal 12-candidate tournament (see candidates.md).
# Chosen by the house judge's own criteria, in priority order:
# setup + turn that lands, laugh-out-loud first read, fresh angle,
# no padding, retellable the same day.
JOKE = "My cat sat on my resume during a job interview and got hired. I just work here now."

MAX_CHARS = 200


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"joke is {len(text)} chars, gate needs 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line")
    out = Path(os.environ.get("CAT_JOKE_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: exactly the joke bytes, one line.
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
