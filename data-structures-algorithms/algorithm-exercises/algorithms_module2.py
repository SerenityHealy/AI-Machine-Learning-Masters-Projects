import time
import random
import pandas as pd

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort(arr):
    if len(arr) <= 10:
        insertion_sort(arr)
        return arr
    else:
        first, middle, last = arr[0], arr[len(arr) // 2], arr[-1]
        pivot = sorted([first, middle, last])[1]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 10:
        insertion_sort(arr)
        return arr
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def measure_time(sort_function, arr):
    start_time = time.perf_counter()
    if sort_function in [quick_sort, merge_sort]:
        sort_function(arr)
    else:
        sort_function(arr[:])
    end_time = time.perf_counter()
    return end_time - start_time

def generate_test_cases(size):
    return {
        "random": [random.randint(0, 1000) for _ in range(size)],
        "sorted": list(range(size)),
        "reverse": list(range(size, 0, -1))
    }

def run_tests():
    sizes = [100, 1000, 5000]
    sorting_algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort,
        "Heap Sort": heap_sort
    }
    results = []
    for name, func in sorting_algorithms.items():
        for size in sizes:
            test_cases = generate_test_cases(size)
            for test_type, arr in test_cases.items():
                time_taken = measure_time(func, arr[:])
                results.append([name, size, test_type, time_taken])

    df = pd.DataFrame(results, columns=["Algorithm", "Size", "Type", "Time (s)"])
    print(df)

if __name__ == "__main__":
    run_tests()
