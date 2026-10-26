#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    prompt = input("What was the parameter? ")
    if prompt == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")    