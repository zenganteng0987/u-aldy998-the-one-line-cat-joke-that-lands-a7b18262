"""The One-Line Cat Joke That Lands.

Writes a single one-line cat joke (under 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt when unset.
No network, no dependencies beyond the Python standard library.
"""

import os

JOKE = (
    "My cat doesn't meow anymore — he just sighs, like a tiny "
    "landlord disappointed in his tenant."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write the joke exactly, with no trailing newline: the gate counts
    # the file's characters (1-200) and the entry must be a single line.
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
