"""The 3 AM Excuse: writes the entry text to /output/entry.txt.

Why this line: true to the prompt, the wallet itself speaks — a concrete
reason (its secure element only signs for owners who can type their PIN
without squinting) and the punch lands at the end (the owner just typed
the PIN with their nose). One breath, wallet voice, 3 AM doing real work.

The entry text is fixed: a single line, no trailing newline, exactly
132 characters. Validation lives in validate_entry() so main() stays
short and only handles writing the file.
"""

import os

# The entry itself: one line, the wallet refuses with a reason and a punch.
ENTRY = 'At 3 AM my secure element only signs for owners who can type their PIN without squinting, and you just entered yours with your nose.'

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate_entry(text):
    """Check the entry is a single non-empty line within the length gate."""
    assert text and not text.isspace(), "entry must not be empty"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert MIN_CHARS <= len(text) <= MAX_CHARS, "entry must be 1-200 chars"
    return text


def main():
    # Guard: never submit a blank entry to the sealed gate.
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
