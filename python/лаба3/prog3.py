import time
import random
import math


def o_1(n=1):
    start_time = time.perf_counter()
    print("--- %s seconds ---" % (time.perf_counter() - start_time))
    return 1

def logn(n):
    start_time = time.perf_counter()
    count=0
    for i in range(round(math.log2(n))):
        count+=1
    print("--- %s seconds ---" % (time.perf_counter() - start_time))
    return  count

def n2(n):
    start_time = time.perf_counter()
    count =0
    for i in range(n):
        for j in range(n):
            count+=1
    print("--- %s seconds ---" % (time.perf_counter() - start_time))
    return count

def o_2n(n):
    start_time = time.perf_counter()
    count=0
    for i in range(2**n):
        count+=1
    print("--- %s seconds ---" % (time.perf_counter() - start_time))
    return  count

o_1()
logn(6)
n2(6)
o_2n(6)
