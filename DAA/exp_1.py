import time
import random
import sys

def interpolation_search(arr, target):
    '''
    Interpolation Search Algorithm
    Time Complexity: O(log log n) average, O(n) worst case
    Space Complexity: O(1)
    '''
    low, high = 0, len(arr)-1
    comparison = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparison += 1
        if low == high:
            if arr[low] == target:
                return low, comparison
            return -1, comparison
        #formula
        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))
        if arr[pos] == target:
            return pos, comparison
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos -1
    return -1, comparison

def binary_search(arr, target):
    '''
    Binary Search Algorithm
    Time Complexity: O(log n)
    Space Complexity: O(1)
    '''
    low, high = 0, len(arr) -1
    comparison = 0

    while low <= high:
        comparison += 1
        mid = (high + low)//2
        if target == arr[mid]:
            return mid, comparison
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1, comparison


def performance_analysis():
    sizes = [1000, 5000, 10000, 50000, 100000]
    print(f"{'Size':>10} {'IS Time(ms)':>14} {'BS Tme(ms)':>14}"
          f"{'IS Comparisons':>16} {'BS Comparisons':>16} ")
    print('-' * 75)

    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        target = arr[random.randint(0, size - 1)]

        #Interpolation Search Timings
        start = time.perf_counter()
        for _ in range(100):
            idx_is, comp_is = interpolation_search(arr, target)
        is_time = (time.perf_counter() - start) / 100 * 1000

        #Binary Search Timings
        start = time.perf_counter()
        for _ in range(100):
            idx_bs, comp_bs = binary_search(arr, target)
        bs_time = (time.perf_counter() - start) / 100 * 1000

        print(f"{size:>10} {is_time:>14.4f} {bs_time:>14.4f} "
            f"{comp_is:>16} {comp_bs:>16}")

# --- Main ---
arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
target = 35
idx, comp = interpolation_search(arr, target)
print(f"Array: {arr}")
print(f"Searching for: {target}")
print(f"Found at index: {idx}, Comparisons: {comp}")
print()
performance_analysis()