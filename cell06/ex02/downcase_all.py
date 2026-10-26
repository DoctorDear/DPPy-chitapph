#!/usr/bin/env python3

import sys


def downcase_it(word):
    return word.lower()

if len(sys.argv) > 1:
    for word in sys.argv[1:]:
        print(downcase_it(word))
else:
    print("none") 


