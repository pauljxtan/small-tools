#!/bin/sh

# Copies the content of a file onto the system clipboard

xclip -sel cli < "$1"
