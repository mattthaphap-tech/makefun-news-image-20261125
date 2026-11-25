#!/usr/bin/env python3
"""make.fun entry: Sum up 25 November's world news in one image.

Writes the bundled front-page image to /output/entry.png.
Deterministic: no network, no randomness, same bytes on every run.
Requires Python 3.13, standard library only.

The output directory defaults to /output (the grader's writable
directory) and can be overridden with the MAKEFUN_OUTPUT_DIR
environment variable, which is how the entry is tested locally.

After copying, the destination is verified against the source
(size and sha256) so a truncated or corrupted copy fails loudly
instead of silently shipping a broken image.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(DST_DIR, "entry.png")

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def _is_png(path):
    with open(path, "rb") as f:
        return f.read(8) == PNG_MAGIC


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not os.path.isfile(SRC):
        print(f"missing source image: {SRC}", file=sys.stderr)
        return 1
    if not _is_png(SRC):
        print(f"source image is not a PNG: {SRC}", file=sys.stderr)
        return 1
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    src_size = os.path.getsize(SRC)
    dst_size = os.path.getsize(DST)
    if src_size != dst_size:
        print(f"size mismatch after copy: {src_size} != {dst_size}",
              file=sys.stderr)
        return 1
    if _sha256(SRC) != _sha256(DST):
        print("sha256 mismatch after copy", file=sys.stderr)
        return 1
    print(f"wrote {DST} ({dst_size} bytes, sha256 {_sha256(DST)[:16]}...)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
