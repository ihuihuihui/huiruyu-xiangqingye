#!/usr/bin/env python3
"""Validate PNG dimensions in a generated e-commerce asset folder.

Only Python's standard library is used so the skill can run after a plain clone.
"""

from __future__ import annotations

import argparse
import struct
from pathlib import Path


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def read_png_size(path: Path) -> tuple[int, int]:
    """Read width and height from a PNG IHDR without third-party packages."""
    with path.open("rb") as stream:
        header = stream.read(24)
    if len(header) < 24 or header[:8] != PNG_SIGNATURE or header[12:16] != b"IHDR":
        raise ValueError("not a valid PNG with an IHDR header")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Task folder containing 主图/ and/or 详情页/")
    parser.add_argument("--width", type=int, default=1086)
    parser.add_argument("--height", type=int, default=1448)
    parser.add_argument("--expected", type=int, default=None, help="Optional expected PNG count")
    args = parser.parse_args()

    files = sorted(args.root.rglob("*.png"))
    wrong = []
    for path in files:
        try:
            width, height = read_png_size(path)
            if (width, height) != (args.width, args.height):
                wrong.append(f"{path}: {width}x{height}")
        except Exception as exc:  # pragma: no cover - diagnostic path
            wrong.append(f"{path}: unreadable ({exc})")

    print(f"PNG_COUNT={len(files)}")
    print(f"EXPECTED_SIZE={args.width}x{args.height}")
    print(f"WRONG_DIMENSIONS={len(wrong)}")
    for item in wrong:
        print(item)

    if args.expected is not None and len(files) != args.expected:
        return 1
    return int(bool(wrong))


if __name__ == "__main__":
    raise SystemExit(main())
