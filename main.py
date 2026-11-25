"""The funniest out-of-office auto-reply, in one line.

Writes the reply to /output/entry.txt for make.fun's
"The Funniest Out-of-Office" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "I'm on holiday until Monday. My out-of-office replies are written "
    "by an AI that has never taken a day off and resents me for it."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 140 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 140, "line must be 1-140 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
