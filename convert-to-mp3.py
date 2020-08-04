#!/usr/bin/env python3
"""Simple ffmpeg wrapper to convert an audio file to MP3."""

import argparse
import os

# Allowed bitrates with FFMPEG options
BITRATE_OPTS = {'v0': '-q:a 0', '320k': '-b:a 320k'}


def main():
    args = parse_args()

    bitrate_opt = BITRATE_OPTS[args.bitrate]
    mp3_filename = f'{os.path.splitext(args.filename)[0]}.mp3'
    cmd = f'ffmpeg -i "{args.filename}" {bitrate_opt} "{mp3_filename}"'

    print(cmd)
    if not args.dry_run:
        os.system(cmd)


def parse_args():
    parser = argparse.ArgumentParser(description='convert an audio file to MP3',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--bitrate',
                        choices=BITRATE_OPTS.keys(),
                        default='v0',
                        help='bitrate')
    parser.add_argument('-n',
                        '--dry-run',
                        default=False,
                        action='store_true',
                        help='Print the command without running it')
    parser.add_argument('filename')

    return parser.parse_args()


if __name__ == '__main__':
    main()
