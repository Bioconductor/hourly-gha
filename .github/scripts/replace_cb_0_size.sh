#!/bin/sh
FPATH=$(echo "$1" | awk '{print $2}')
SIZE=$(echo "$1" | awk '{print $1}')
if [ "$SIZE" = "0" ]; then
  NEWSIZE=$(rclone ls "$2/$FPATH" | awk '{print $1}')
  sed -i "s#$1#$NEWSIZE $FPATH#g" "$3"
fi