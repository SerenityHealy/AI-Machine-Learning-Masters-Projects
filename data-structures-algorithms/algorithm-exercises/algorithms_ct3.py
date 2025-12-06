import time
import random
import statistics
from faker import Faker

fake = Faker()

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j]['Patient ID'] > arr[j + 1]['Patient ID']:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i]['Patient ID'] < right_half[j]['Patient ID']:
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
    return arr

def generate_patient_records(n):
    return [{'Patient ID': random.randint(100000, 999999), 'Name': fake.name(),
             'Condition': random.choice(['Diabetes', 'Hypertension', 'Asthma', 'Cardiac Disease', 'Healthy'])} for _ in
            range(n)]

data_sizes = [100, 500, 1000, 5000]
num_trials = 5

results = {}

for size in data_sizes:
    bubble_times = []
    merge_times = []

    for _ in range(num_trials):
        patient_records = generate_patient_records(size)

        bubble_records = patient_records.copy()
        bubble_start = time.time()
        bubble_sort(bubble_records)
        bubble_end = time.time()
        bubble_times.append(bubble_end - bubble_start)

        merge_records = patient_records.copy()
        merge_start = time.time()
        merge_sort(merge_records)
        merge_end = time.time()
        merge_times.append(merge_end - merge_start)

    results[size] = {
        "Bubble Sort Avg Time": statistics.mean(bubble_times),
        "Merge Sort Avg Time": statistics.mean(merge_times)
    }

print("Execution Time Comparison:")
for size, times in results.items():
    print(f"Dataset Size: {size}")
    print(f"  Bubble Sort Avg Time: {times['Bubble Sort Avg Time']:.6f} seconds")
    print(f"  Merge Sort Avg Time: {times['Merge Sort Avg Time']:.6f} seconds")
    print()
