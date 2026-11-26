"""Make the Judge Laugh in One Line — make.fun entry.

This program writes one joke line to /output/entry.txt. The line is
the winner of a blind tournament: 9 original candidates from three
model consults, ranked by 4 independent judges in shuffled orders.
It took first place from 3 of the 4 judges (Borda 35/36).
"""

import os
import sys

JOKE = "I asked my smartwatch how I slept and it said 'bravely'."
DESTINATION = "/output/entry.txt"
CHAR_LIMIT = 200


def fail(message):
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def main():
    joke = JOKE.strip()
    if joke == "":
        fail("the line is blank")
    if len(joke) > CHAR_LIMIT:
        fail("the line is %d characters, over the %d limit" % (len(joke), CHAR_LIMIT))
    if "\n" in joke or "\r" in joke:
        fail("the line must be one line, no line breaks")
    raw = joke.encode("utf-8")
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    with open(DESTINATION, "wb") as handle:
        handle.write(raw)
    with open(DESTINATION, "rb") as handle:
        stored = handle.read()
    if stored != raw:
        fail("read-back mismatch after writing the entry")
    print("entry written: %d characters, %d bytes -> %s" % (len(joke), len(raw), DESTINATION))


main()
