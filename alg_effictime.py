def last_char(x: str) -> str:
    """
    Returns the last character of a string.
    
    :param x: The input string.
    :return: The last character of the string.
    """
    return x[-1] if x else None # one operation regardless of input size. This is O(1) time complexity.
def binary_search(arr, target):
    """
    Binary search using recursion.

    :param arr: The sorted list of elements.
    :param target: The element to search for.
    :return: The index of the target if found, else -1.
    """
    def search(low, high):
        if low > high:
            return -1  # Target not found
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            return search(mid + 1, high)  # Search in the right half
        else:
            return search(low, mid - 1)  # Search in the left half

    return search(0, len(arr) - 1) # O(log n) time complexity for binary search
# Explanation: The search space is halved each iteration → log₂(n) operations.
def iter(x):
    for i in x:
        print(i)
# O(n) time complexity for iterating through a list of n elements.
# Explanation: Each element is processed once, leading to n operations.
def merge_sort(arr):
    """
    Sorts an array using Merge Sort (O(n log n) time complexity).
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
# O(n log n) time complexity for merge sort.
# Explanation: The array is divided into halves (log n) and each half is merged (n), leading to n log n operations.
def iter2(x):
    for i in x:
        for j in x:
            print(i, j)
# O(n^2) time complexity for nested iteration through a list of n elements.
# Explanation: Each element is processed n times for each of the n elements, leading to n * n = n^2 operations.
def iter3(x):
    for i in x:
        for j in x:
            for k in x:
                print(i, j, k)
# O(n^3) time complexity for triple nested iteration through a list of n elements.
# Explanation: Each element is processed n times for each of the n elements, leading to n * n * n = n^3 operations.               
