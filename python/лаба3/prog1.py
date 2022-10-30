import time
import random
arrs = [random.randint(-1000, 1000) for i in range(100000)]
arr = arrs

def bubbleSort(arr):
    global count
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return arr

print('-----Метод sort()-----')
start_time = time.perf_counter()
arrs.sort()
#print(f"Отсортированный список: {arrs}")
print("--- %s seconds ---" % (time.perf_counter() - start_time))

print('-----Пузырьковая сортировка-----')
start_time = time.perf_counter()
bubbleSort(arr)
#print(f"Отсортированный список: {arr}")
print("--- %s seconds ---" % (time.perf_counter() - start_time))
