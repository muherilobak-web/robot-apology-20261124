"""The Robot Apology.

Writes a two-line robot apology to /output/entry.txt: line 1 owns one
specific mistake, line 2 states what the robot learned and what it will
do differently. Deterministic, no dependencies, no input.
"""

import os

TEXT = (
    "I am sorry I watered the fern that was already soaked and left the "
    "thirsty basil dry, because I followed my routine instead of reading "
    "the tag on each pot.\n"
    "From now on I will read the tag on every pot before I lift the "
    "watering can, so each plant gets only the water it needs."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
