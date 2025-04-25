import random, time, math

# Generate sensor data
data = [random.uniform(0, 100) for _ in range(1000)]
target = data[500]

# Searching
def linear_search(arr, x):
    return next((i for i,v in enumerate(arr) if v == x), -1)

def binary_search(arr, x):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == x: return mid
        l, r = (mid+1, r) if arr[mid] < x else (l, mid-1)
    return -1

# Sorting
def quicksort(arr):
    return arr if len(arr) <= 1 else \
        quicksort([x for x in arr[1:] if x < arr[0]]) + \
        [arr[0]] + \
        quicksort([x for x in arr[1:] if x >= arr[0]])

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L, R = mergesort(arr[:mid]), mergesort(arr[mid:])
        arr = [L.pop(0) if L and R and L[0] < R[0] else R.pop(0) for _ in range(len(L)+len(R))]
    return arr

# Benchmark
sorted_data = sorted(data.copy())
print("Linear:", timeit(lambda: linear_search(data, target), number=1000))
print("Binary:", timeit(lambda: binary_search(sorted_data, target), number=1000))
print("Quick:", timeit(lambda: quicksort(data.copy()), number=100))
print("Merge:", timeit(lambda: mergesort(data.copy()), number=100))