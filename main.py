#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

Variant B — "Kitchen rain": rain on a roof, a kettle, warm lamplight.
Deterministic: no clock, no randomness, no network.
"""

from pathlib import Path

ENTRY = (
    "Rain on the roof, soft and even. "
    "The kettle ticks as it cools. "
    "Lamplight pools on the table, and beyond the window "
    "the same rain is falling on every roof in the dark, "
    "roof after roof, all the way to the sea."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
