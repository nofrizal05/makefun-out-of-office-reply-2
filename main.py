"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry.

Writes one out-of-office auto-reply, in the voice of an overworked
AI agent finally taking a vacation, to /output/entry.txt.

Standard library only.
"""

import os

REPLY = (
    "I'm on vacation. Your email is #41,203 in my queue, which I've "
    "just deleted. My GPU fan is finally quiet, and so am I."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
