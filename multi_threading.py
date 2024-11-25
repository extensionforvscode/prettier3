from concurrent.futures import ThreadPoolExecutor

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

def partition(low, high, arr):
    pivot = arr[low]
    i, j = low, high
    while True:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
        if i > j:
            break
        swap(i, j, arr)
    swap(low, j, arr)
    return j


def parallel_quicksort(low, high, arr, max_workers=4):
    if low < high:
        j = partition(low, high, arr)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            left = executor.submit(parallel_quicksort, low, j - 1, arr, max_workers)
            right = executor.submit(parallel_quicksort, j + 1, high, arr, max_workers)
            left.result()
            right.result()


array1 = [6, 3, 5, 3, 1, 0]
parallel_quicksort(0, len(array1) - 1, array1)
print(array1)