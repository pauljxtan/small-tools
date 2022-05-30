#!/usr/bin/env python3
"""Renames an image file with its MD5 hash."""

import hashlib
import os
import re
import sys

IMG_EXTS = (
    ".gif",
    ".jpeg",
    ".jpg",
    ".png",
)


def main():
    # TODO use argparse?
    filepaths = sys.argv[1:]

    for filepath in filepaths:
        dirname, filename = os.path.split(filepath)
        filename_no_ext, ext = os.path.splitext(filename)

        if ext.lower() not in IMG_EXTS:
            print(
                f"Unsupported extension {ext} in {filename}; expected one of {IMG_EXTS}"
            )
            sys.exit()

        if looks_like_md5(filename_no_ext):
            print(f"{filename} already looks like md5; doing nothing")
            sys.exit()

        new_filename = get_md5_hash(filepath) + ext
        new_filepath = os.path.join(dirname, new_filename)

        confirm = input(f"Rename {filepath} -> {new_filepath}? [y/N] ")
        if confirm != "y":
            print("Aborting")
            sys.exit()

        os.system(f"mv -v {filepath} {new_filepath}")


def looks_like_md5(string):
    regex = re.compile("^[0-9a-f]{32}$")
    return re.match(regex, string) is not None


def get_md5_hash(filepath):
    with open(filepath, "rb") as img_file:
        return hashlib.md5(img_file.read()).hexdigest()


if __name__ == "__main__":
    main()
