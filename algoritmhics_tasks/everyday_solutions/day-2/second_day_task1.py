with open('data.txt') as file:
    data = file.read()

data_arr = data.split('\n')

new_arr = [list(map(int, num_list.split())) for num_list in data_arr]

total = 0
# Checking for the all arrays in data
for arr in new_arr:
    # Set temporary variables for checking list type and safety.
    # Index will use for to compare first and second elements of array.
    safety = ""
    list_type = ""
    index = 0
    # If first element of our list greater than second one. The list type will be increase, vise versa
    if arr[index] > arr[index + 1]:
        list_type = "Decrease"
    if arr[index] < arr[index + 1]:
        list_type = "Increase"

    if list_type == 'Increase':
        for idx in range(len(arr)):
            # We should check the idx (index) here if it's not starter one (if you don't make this, code will check
            # before the 0th index.
            if idx != 0:
                # In increasing list the difference between 2 elements have to be greater and not equal 0, also...
                # less equal (<=) than 3
                if 0 < arr[idx] - arr[idx - 1] <= 3:
                    safety = "safe"
                else:
                    safety = "unsafe"
                    break

    if list_type == "Decrease":
        for idx in range(len(arr)):
            # We should check the idx (index) here if it's not starter one (if you don't make this, code will check
            # before the 0th index.
            if idx != 0:
                # In decreasing list the difference between 2 elements have to be less and not equal 0, also...
                # great equal (>=) than 3
                if 0 > arr[idx] - arr[idx - 1] >= -3:
                    safety = "safe"
                else:
                    safety = "unsafe"
                    break

    if safety == "safe":
        total += 1

print(total)
