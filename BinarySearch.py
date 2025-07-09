found_flag = False
def binary_search(numbers, key_value, found_flag = False):
    start_index = 0
    end_index = len(numbers) - 1

    while start_index <= end_index:
        mid = (start_index + end_index) //2

        mid_val = numbers[mid]

        if mid_val == key_value:
           found_flag = True
           return mid

        elif key_value > mid_val:
             start_index = mid_val + 1

        elif key_value < mid_val:
             end_index = mid_val - 1

    return -1



if __name__ == '__main__':
    key_value = 88
    numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]

    index = binary_search(numbers = numbers, key_value= key_value)

    if found_flag == True:
        print(f"Element {key_value} found at pos:{index}")

