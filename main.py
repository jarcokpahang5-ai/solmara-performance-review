"""Performance review one-liner entry for make.fun.

Writes a single funny line to /output/entry.txt and echoes exactly
that line to stdout. Pure Python 3 standard library, deterministic,
no network access.
"""

import os

TEXT = (
    "Exceeds expectations in turning five-minute tasks into week-long sagas, "
    "and somehow still gets promoted before the rest of us."
)


def checked(text):
    """Return text unchanged after confirming it is one valid entry line."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters long")
    return text


def emit(text):
    """Save the line (plus one trailing newline) and print it."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    print(text)


if __name__ == "__main__":
    emit(checked(TEXT))
