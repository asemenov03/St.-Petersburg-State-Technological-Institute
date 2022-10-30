import time
import random
import math

def o_3n():
    start_time = time.perf_counter()
    a = []
    for i in range(3):
        for j in range(10):
            a.append(random.randint(-1000, 1000))
    print("--- %s seconds ---" % (time.perf_counter() - start_time))

def nlogn(n,x):
    # Создание упорядоченного массива и вывод наличия в нём числа x
    start_time = time.perf_counter()
    a = []
    for i in range(n):
        a.append(i)

    left=0
    right=0
    step=0
    while step<= math.log2(n):
        median = (left+right)//2
        if a[median]==x:
            return True
        if a[median]>x:
            right=median
        if a[median]<x:
            left = median
        step+=1
    print("--- %s seconds ---" % (time.perf_counter() - start_time))

def nfact(n):
    # Вычисление факториала самым медленным способом
    start_time = time.perf_counter()
    count =1
    c=0
    gc=1
    while gc<=n:
        c=count
        for i in range(gc-1):
            for j in range(c):
                count+=1
        gc+=1
    print("--- %s seconds ---" % (time.perf_counter() - start_time))

def o_n3():
    start_time = time.perf_counter()
    a = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                a.append(random.randint(-1000, 1000))
    print("--- %s seconds ---" % (time.perf_counter() - start_time))

def o_3logn(n,x):
    start_time = time.perf_counter()
    a = []
    for i in range(n):
        a.append(i)

    left = 0
    right = 0
    step = 0
    while step <= math.log2(n):
        median = (left + right) // 2
        if a[median] == x:
            return True
        if a[median] > x:
            right = median
        if a[median] < x:
            left = median
        step += 1

    left = 0
    right = 0
    step = 0
    while step <= math.log2(n):
        median = (left + right) // 2
        if a[median] == x:
            return True
        if a[median] > x:
            right = median
        if a[median] < x:
            left = median
        step += 1
    print("--- %s seconds ---" % (time.perf_counter() - start_time))

o_3n()
nlogn(10,5)
nfact(6)
o_n3()
o_3logn(34,22)
