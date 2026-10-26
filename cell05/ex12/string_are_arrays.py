#!/usr/bin/env python3

import sys

# txt = (sys.argv[1]).count("z")
# print(txt)

# if len(sys.argv) == 2:
#     txt = ("z" * sys.argv[1].count("z"))
#     if txt:
#         print(txt)
#     else:
#         print("none")
# else:
#     print("none")

if len(sys.argv) == 2:
    txt = ""
    for char in sys.argv[1]:
        if char == "z":
            txt += "z"
    if txt:
        print(txt)
    else:
        print("none")
else:
    print("none")