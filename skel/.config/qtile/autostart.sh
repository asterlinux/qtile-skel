#!/usr/bin/env bash 

picom &
nm-applet &
nitrogen --restore &
conky -c ~/.config/conky/conky.conf &
