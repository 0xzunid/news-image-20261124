"""24 November 2026 news-image entry.

Places the bundled front page (``entry.png``) in the output directory
(``$MAKEFUN_OUTPUT_DIR``, default ``/output``) and proves the placed copy
is a byte-exact duplicate: matching SHA-256 and a 1024x1024 PNG header.

Standard library only. No network, no arguments, deterministic.
"""

import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

BUNDLED = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
WANT_DIMS = (1024, 1024)
# SHA-256 of the bundled front page, taken when the image was drawn:
# catches a damaged or swapped bundled file, not just a copy slip.
WANT_SHA256 = "f41552452cea0afaf7da913a8eca2565224f8eaec0ceb44a2a451280a6fbb4ec"


def sha256_of(path):
    """Hex SHA-256 of a file, streamed in 64 KiB blocks."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(1 << 16)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def check_dimensions(path):
    """(width, height) read from the PNG IHDR chunk, or None if invalid."""
    with open(path, "rb") as handle:
        head = handle.read(33)
    if len(head) < 33:
        return None
    if head[:8] != b"\x89PNG\r\n\x1a\n" or head[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", head[16:24])


def check_digest(path, want):
    """True when the file at path hashes to the expected SHA-256."""
    return sha256_of(path) == want


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(BUNDLED, target)

    dims = check_dimensions(target)
    if dims != WANT_DIMS:
        print(f"bad dimensions {dims}, expected {WANT_DIMS}", file=sys.stderr)
        return 1

    if not check_digest(target, WANT_SHA256) or not check_digest(BUNDLED, WANT_SHA256):
        print("placed copy digest does not match bundled image", file=sys.stderr)
        return 1

    print(f"wrote {target} ({target.stat().st_size} bytes, {dims[0]}x{dims[1]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
