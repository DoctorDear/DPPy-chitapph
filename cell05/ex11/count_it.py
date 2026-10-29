#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print(f"parameters: {len(sys.argv[1:])}")
    for word in sys.argv[1:]:
        count = 0
        for char in word:
            count += 1
        print(f"{word}: {count}")
else:
    print("none")