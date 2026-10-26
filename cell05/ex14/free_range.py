#!/usr/bin/env python3

import sys

# if len(sys.argv) == 3:
#     freeRange = []
#     firstArr = int(sys.argv[1])
#     lastArr = int(sys.argv[2]) + 1
#     for i in range(firstArr, lastArr):
#         freeRange.append(i)
#     print(freeRange)
# else:
#     print("none")



if len(sys.argv) == 3:
    firstArr = int(sys.argv[1])
    lastArr = int(sys.argv[2]) + 1
    print(range(firstArr, lastArr))
    freeRange = list(range(firstArr, lastArr))
    print(freeRange)
else:
    print("none")