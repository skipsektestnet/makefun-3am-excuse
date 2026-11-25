"""The 3 AM Excuse: writes the entry text to /output/entry.txt.

Why this line: true to the prompt, the wallet itself speaks — a concrete
reason (its secure element only signs for owners who can type their PIN
without squinting) and the punch lands at the end (the owner just typed
the PIN with their nose). One breath, wallet voice, 3 AM doing real work.
"""

import os

# The entry itself: one line, the wallet refuses with a reason and a punch.
ENTRY = 'At 3 AM my secure element only signs for owners who can type their PIN without squinting, and you just entered yours with your nose.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
