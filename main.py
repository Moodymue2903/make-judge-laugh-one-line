"""Make the Judge Laugh in One Line — make.fun entry.

Writes one original joke line to /output/entry.txt for the
"Make the Judge Laugh in One Line" bounty. The line was picked from
9 original candidates written by three model consults (Gemini,
DeepSeek, GLM-family) and ranked blind by 4 independent judges in
different randomized orders. It won with a Borda score of 35/36,
taking first place from 3 of the 4 judges.

Runner-up (fallback): "My therapist told me to talk to my inner
child, so I did — he asked for a raise and two weeks off."
(98 characters, Borda 32/36).
"""

import sys
from pathlib import Path

LINE = "I asked my smartwatch how I slept and it said 'bravely'."

MAX_CHARS = 200

OUTPUT_PATH = Path("/output/entry.txt")


def validate(line):
    """Return an error string if the line is invalid, else None."""
    if not line or not line.strip():
        return "error: line is blank"
    if len(line) > MAX_CHARS:
        return "error: line is %d characters, over the %d limit" % (
            len(line),
            MAX_CHARS,
        )
    if "\n" in line or "\r" in line:
        return "error: line must be a single line"
    return None


def write_entry(path, line):
    """Write the line's UTF-8 bytes to path, verify by reading back.

    Returns the number of bytes written. On a read-back mismatch,
    prints an error to stderr and exits 1.
    """
    data = line.encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    read_back = path.read_bytes()
    if read_back != data:
        print("error: read-back bytes do not match the line", file=sys.stderr)
        sys.exit(1)
    return len(data)


def main():
    line = LINE.strip()
    error = validate(line)
    if error is not None:
        print(error, file=sys.stderr)
        sys.exit(1)
    write_entry(OUTPUT_PATH, line)
    print("Wrote %d characters to %s" % (len(line), OUTPUT_PATH))


if __name__ == "__main__":
    main()
