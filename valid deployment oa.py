#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'evaluate_deployments' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY deployments as parameter.
#
import json

def valid_json(i):
    return i["deployment_id"] and i["deployment_id"][2:].isalnum() and len(i["deployment_id"][2:]) ==10 and i["deployment_id"][0] =='d' and i["deployment_id"].islower() and isinstance(i["status"],str)

def evaluate_deployments(deployments):
    # Write your code here
    sum_s = 0
    sum_f = 0
    sum_e = 0
    res = []
    d = []
    print(deployments)

    for i in deployments:
        #print(type(item["status"]))
        try:
            item = json.loads(i)
            d.append(item)
        except:
            sum_e += 1
        
    for i in d:
        if len(i.keys()) != 2:
            sum_e += 1
        elif valid_json(i) and i["status"] == "Success":
            sum_s += 1
        elif  valid_json(i) and i["status"] == "Fail":
            sum_f += 1
        else:
            sum_e += 1
    res = [sum_s, sum_f, sum_e]
    return res
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    deployments_count = int(input().strip())

    deployments = []

    for _ in range(deployments_count):
        deployments_item = input()
        deployments.append(deployments_item)

    result = evaluate_deployments(deployments)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
