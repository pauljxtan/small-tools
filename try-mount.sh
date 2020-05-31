#######################################
# Mounts a labelled partition if it is
# connected and not already mounted.
#
# Args:
#     The partition label
#     The mount path (if not given,
#         checks /etc/fstab)
#######################################
function try-mount {
    local LABEL=$1
    local MOUNT_PATH=$2

    if [ -b /dev/disk/by-label/$LABEL ]
    then
        echo "$LABEL is connected"
        if [ $(grep -c $LABEL /proc/mounts) -eq 1 ]
        then
            echo "$LABEL is already mounted"
        else
            echo "Mounting $LABEL at $MOUNT_PATH..."
            sudo mount -L $LABEL $MOUNT_PATH
        fi
    else
        echo "$LABEL is not connected"
    fi
}
