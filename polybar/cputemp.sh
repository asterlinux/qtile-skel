#!/bin/sh

sensors | grep -A 0 'Core 0:' | cut -c16-17
