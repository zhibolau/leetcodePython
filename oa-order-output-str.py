
## Happy path
configuration = "0002f7c22e7904|000176a3a4d214|000305d29f4a4b"

# Based on the `order` value, the expected output of this configuration string is:

## Output
[
"76a3a4d214", # 0001
"f7c22e7904", # 0002
"05d29f4a4b"  # 0003
]

## Invalid configuration
configuration = "0002f7c22e7904|000176a3a4d214|000205d29f4a4b"

# Configuration string contains two indices for "0002"

## Output
["Invalid configuration"]


#!/bin/python3

import math
import os
import random
import re
import sys



def ordered_configuration(configuration):
    print(configuration)
    # Write your code here
    if not configuration or "|" not in configuration:
        return ["Invalid configuration"]
    configs = configuration.split("|")
    d = {}
    print(configs)
    for i in configs:
        if i[:4] not in d.keys():
            d[i[:4]] = i[4:]
        else:
            return ["Invalid configuration"]
    result = []
    last = sorted(d.keys())[-1]
    if int(last) != len(d.keys()):
        print(last)
        return ["Invalid configuration"]
        
    for i in sorted(d.keys()):
        result.append(d[i])
    print(result)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    configuration = input()

    result = ordered_configuration(configuration)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
