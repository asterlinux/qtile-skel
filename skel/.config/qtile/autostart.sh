#!/usr/bin/env bash 

picom &
nm-applet &
nitrogen --restore &
conky -c ~/.config/conky/conky.conf &
/usr/lib/xfce-polkit/xfce-polkit &
