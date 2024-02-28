import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Generate test data
random.seed(42)
data_sizes = [1000, 5000, 10000]  # Adjust as needed
datasets = {}
for size in data_sizes:
    dataset = random.sample(range(size * 3), size)
    datasets[size] = {
        'random': dataset,
        'sorted': sorted(dataset),
        'reversed': sorted(dataset, reverse=True)
    }

# Benchmark sorting algorithms
algorithms = {
    'Merge Sort': merge_sort,
    'Insertion Sort': insertion_sort,
    'Timsort': sorted
}

for algo_name, algo_func in algorithms.items():
    print(f"\nBenchmarking {algo_name}:")
    for size, datasets_dict in datasets.items():
        print(f"\nDataset size: {size}")
        for data_type, data in datasets_dict.items():
            time_taken = timeit.timeit(lambda: algo_func(data.copy()), number=10)
            print(f"{data_type.capitalize()}: {time_taken:.6f} seconds")
