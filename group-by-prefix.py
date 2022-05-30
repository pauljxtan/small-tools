#!/usr/bin/env python3
"""Group files into sub-directories according to filename prefixes.

Example:
    $ ls
    a.jpg  ab.jpg  abc.jpg  abcd.jpg
    $ group-by-prefix.py --prefix-length 3 .
    ...
    $ tree
    .
    ├── a
    │   ├── a.jpg
    │   └── b
    │       ├── ab.jpg
    │       └── c
    │           ├── abcd.jpg
    │           └── abc.jpg
"""

# TODO add a test
# TODO may want to handle filename/dirname conflicts

import argparse
import os
import shutil
import sys


def main():
    args = parse_args()

    for filename in sorted(
        f
        for f in os.listdir(args.path)
        if os.path.isfile(f) and f != os.path.basename(sys.argv[0])
    ):
        name = os.path.splitext(filename)[0]
        dest_path = "."

        for i in range(args.prefix_length):
            if i >= len(name):
                break
            dest_path = os.path.join(dest_path, name[i])

        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        print(f"{filename} -> {dest_path}")
        if not args.dry_run:
            shutil.move(filename, dest_path)


def parse_args():
    parser = argparse.ArgumentParser(
        description="group files by filename prefix",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--prefix-length", default=1, type=int, help="length of prefix to use"
    )
    parser.add_argument("--path", default=".", help="path at which to process files")
    parser.add_argument(
        "--dry-run",
        default=False,
        action="store_true",
        help="do a dry run without moving files",
    )

    return parser.parse_args()


if __name__ == "__main__":
    main()
