#!/bin/sh

tar -cf skel.tar.gz skel/

makepkg -s --sign

rm -r skel.tar.gz
rm -r pkg/ src/ 
