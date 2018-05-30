#!/bin/bash

/bin/modprobe msr
wrmsr -a 0x1a2 0x3000000 # which sets the offset to 3 C, so the new trip point is 97 C