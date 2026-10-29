#!/usr/bin/env python3

import sys

# if len(sys.argv) > 2:
#     sys.argv.reverse()
#     for argv in sys.argv[:-1]:
#         print(argv)
# else:
#     print("none")

# slicing method
# sys.argv[start:stop:step]
# if len(sys.argv) > 2:
#     for argv in sys.argv[:0:-1]:
#         print(argv)
# else:
#     print("none")


# reversed method
if len(sys.argv) > 2:
    for argv in reversed(sys.argv[1:]):
        print(argv)
else:
    print("none")