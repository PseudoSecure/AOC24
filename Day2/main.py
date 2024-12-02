

array1 = []

count = 0


def is_sorted_and_valid_diff(arr):
    if all(arr[i] < arr[i + 1] and 1 <= abs(arr[i + 1] - arr[i]) <= 3 for i in range(len(arr) - 1)):
        return True
    if all(arr[i] > arr[i + 1] and 1 <= abs(arr[i] - arr[i + 1]) <= 3 for i in range(len(arr) - 1)):
        return True
    return False

def can_remove_one_to_make_valid(arr):
    for i in range(len(arr)):
        new_arr = arr[:i] + arr[i + 1:]
        if is_sorted_and_valid_diff(new_arr):
            return True
    return False


with open('input.txt', 'r') as file:
    for line in file:
        elements = line.strip().split(' ')
        int_array = [int(x) for x in elements]
        if is_sorted_and_valid_diff(int_array):
            count += 1
        elif can_remove_one_to_make_valid(int_array):
            count +=1

print(count)



