#!/usr/bin/env python3
"""Validate a generated e-commerce asset folder without changing files."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Task folder containing 主图/ and/or 详情页/")
    parser.add_argument("--width", type=int, default=1086)
    parser.add_argument("--height", type=int, default=1448)
    parser.add_argument("--expected", type=int, default=None, help="Optional expected PNG count")
    args = parser.parse_args()

    try:
        from PIL import Image
    except ImportError as exc:
        raise SystemExit("Pillow is required: python3 -m pip install pillow") from exc

    files = sorted(args.root.rglob("*.png"))
    wrong = []
    for path in files:
        try:
            with Image.open(path) as image:
                if image.size != (args.width, args.height):
                    wrong.append(f"{path}: {image.size[0]}x{image.size[1]}")
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
