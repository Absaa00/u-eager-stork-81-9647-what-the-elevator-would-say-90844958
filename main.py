#!/usr/bin/env python3
"""What the Elevator Would Say -- one-line entry.

Writes a single line (<=120 characters) in the elevator's own voice to
/output/entry.txt -- the funniest thing a lift would say if it could talk.
The ding and the floor call set the scene, then the lift breaks the
awkward silence every rider knows, with a punchline only a lift could
deliver. Also prints the line to stdout for local runs.
Deterministic: no input, no randomness, no network.
"""

import os

LINE = "Ding! Floor 12. We ride in silence every day. Say hi, I'm literally holding you up."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 120, "line must be 1-120 characters: %d" % len(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
