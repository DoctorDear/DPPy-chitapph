#!/usr/bin/env python3

import re
import sys

if len(sys.argv) == 3:

    keyword = sys.argv[1]
    txt = sys.argv[2]

    searched = re.findall(keyword, txt)
    # if len(searched) < 0:
    #     print(len(searched))
    # else:
    #     print("none")
    if not searched:
        print("none")
    else:
        print(searched)
        print(len(searched))
else:
    print("none")