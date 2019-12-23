#!/bin/sh

# Make a git commit with the current timestamp (useful for automation)

git commit -m "$(date +%Y-%m-%d\ %H:%M:%S)"
