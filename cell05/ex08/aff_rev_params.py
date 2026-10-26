#!/usr/bin/env python3

import sys

# if len(sys.argv) > 2:
#     sys.argv.reverse()
#     for argvs in sys.argv[:-1]:
#         print(argvs)
# else:
#     print("none")

# slicing method
# sys.argv[start:stop:step]
# if len(sys.argv) > 2:
#     for argvs in sys.argv[:0:-1]:
#         print(argvs)
# else:
#     print("none")


# reversed method
if len(sys.argv) > 2:
    for argvs in reversed(sys.argv[1:]):
        print(argvs)
else:
    print("none")