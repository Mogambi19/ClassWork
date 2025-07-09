def binary_search(arr, key_value)-> int:
    start = 0
    end = len(arr) - 1

    while start<=end:
        mid = (start + end) //2
        mid_val = arr[mid]

        if mid_val == key_value:
            return mid
        elif key_value < mid_val:
            end = mid - 1
        else: # key_value > mid_val
             start = mid + 1

    return -1

sorted_numbers = [11, 22, 33, 44,55,66,77,88,99]
key = 88

# index_found = binary_search(key_value = key, arr = sorted_numbers)
index_found = binary_search(sorted_numbers, key)

if index_found != -1:
    print(f"Binary Search for Target: {key} found at index {index_found}")
else:
    print("Item Not Found")


def recursive_binary_search(arr, target, start_index, end_index):
    if start_index > end_index:
        return -1

    mid = (start_index + end_index) // 2
    mid_val = arr[mid]

    if mid_val == target:
        return mid
    elif mid_val < target:
        return recursive_binary_search(arr, target, mid + 1, end_index)
    else:
        return recursive_binary_search(arr, target, start_index, mid - 1)


