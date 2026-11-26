#!/usr/bin/env python3
"""What the Elevator Would Say -- one-line entry.

Prints a single line (<=120 characters) in the elevator's own voice:
the funniest thing a lift would say if it could talk. The ding and the
floor call set the scene, then the lift breaks the awkward silence
every rider knows, with a punchline only a lift could deliver.
Deterministic: no input, no randomness, no network, no files.
"""

LINE = "Ding! Floor 12. We ride in silence every day. Say hi, I'm literally holding you up."


def main() -> None:
    assert len(LINE) <= 120, "line exceeds 120 characters: %d" % len(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
