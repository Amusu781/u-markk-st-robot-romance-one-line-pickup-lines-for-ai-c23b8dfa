"""Robot Romance: One-Line Pickup Lines for AI.

Writes a single pickup line, aimed at an AI, to /output/entry.txt
(no trailing newline). The output directory can be overridden with the
OUTPUT_DIR environment variable; it is created if missing and never deleted.
"""

import os

LINE = "Are you an embedding? Because you're closest to me in every dimension."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_NAME = "entry.txt"


def write_line(path: str, text: str) -> None:
    """Overwrite only the file at path with text, encoded as UTF-8."""
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    assert "\n" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    write_line(os.path.join(OUTPUT_DIR, OUTPUT_NAME), LINE)


if __name__ == "__main__":
    main()
