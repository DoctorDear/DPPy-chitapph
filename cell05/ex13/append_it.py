#!/usr/bin/env python3

import re
import sys

# if len(sys.argv) > 1:
#     for word in sys.argv[1:]:
#         if word.endswith("ism"): #endswith is string method
#             continue
#         print(word + "ism")
# else:
#     print("none")

if len(sys.argv) > 1:
    for word in sys.argv[1:]:
        if re.search(r"ism\Z", word): #regex end of string anchor
            continue
        print(word + "ism")
else:
    print("none")