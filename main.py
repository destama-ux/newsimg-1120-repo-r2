#!/usr/bin/env python3
"""Validate the v2 news-image artwork and copy it to the output directory.

Reads artwork.jpg from this script's own directory, checks that it is a
real JPEG of exactly 1024x1024 pixels and at most 1 MiB, then copies it
byte-for-byte to entry.png inside $MAKEFUN_OUTPUT_DIR (created if needed;
a local "output" directory is used when the variable is unset).
"""

import os
import shutil
import sys

MAX_BYTES = 1 * 1024 * 1024
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def fail(message):
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def jpeg_dimensions(data):
    """Return (width, height) parsed from a JPEG start-of-frame segment."""
    if len(data) < 4 or data[0] != 0xFF or data[1] != 0xD8:
        return None
    pos = 2
    while pos + 9 <= len(data):
        if data[pos] != 0xFF:
            return None
        marker = data[pos + 1]
        if marker == 0xD8 or marker == 0x01 or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        if pos + 4 > len(data):
            return None
        length = (data[pos + 2] << 8) | data[pos + 3]
        if length < 2 or pos + 2 + length > len(data):
            return None
        # SOF0-SOF3, SOF5-SOF7, SOF9-SOF11, SOF13-SOF15 carry dimensions;
        # SOF4, SOF8 and SOF12 are not start-of-frame markers, so skip them.
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                      0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            height = (data[pos + 5] << 8) | data[pos + 6]
            width = (data[pos + 7] << 8) | data[pos + 8]
            return (width, height)
        pos += 2 + length
    return None


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "artwork.jpg")
    if not os.path.isfile(source):
        fail("artwork.jpg not found in " + here)
    with open(source, "rb") as handle:
        data = handle.read()
    if len(data) > MAX_BYTES:
        fail("artwork.jpg is %d bytes, over the 1 MiB limit" % len(data))
    if len(data) < 2 or data[0] != 0xFF or data[1] != 0xD8:
        fail("artwork.jpg is not a JPEG (missing SOI marker FF D8)")
    dims = jpeg_dimensions(data)
    if dims is None:
        fail("could not parse JPEG dimensions from artwork.jpg")
    if dims != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        fail("artwork.jpg is %dx%d, expected 1024x1024" % dims)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(here, "output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)
    print("wrote %s (%dx%d, %d bytes)" % (dest, dims[0], dims[1], len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
