#!/usr/bin/env python3

import sys

def shrink(text):
    return(text[0:8])

def enlarge(text):
    while len(text) < 8:
        text += "Z"
    return(text)

shrink("physical")
enlarge("test")

if len(sys.argv) > 1:
    for word in sys.argv[1:]:
        if len(word) > 8:
            print(shrink(word))
        elif len(word) < 8:
            print(enlarge(word))
        else:
            print(word)
else:
    print("none")
