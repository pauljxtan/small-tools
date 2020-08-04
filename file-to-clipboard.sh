#!/bin/sh

# Copies the content of a file onto the system clipboard

if [ "$XDG_SESSION_TYPE" = "x11" ]
then
    xclip -sel cli < "$1"
elif [ "$XDG_SESSION_TYPE" = "wayland" ]
then
    wl-copy < "$1"
else
    echo "Unrecognized XDG_SESSION_TYPE: $XDG_SESSION_TYPE"
    echo "Expected x11 or wayland"
fi
