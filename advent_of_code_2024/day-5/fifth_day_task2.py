with open("data.txt") as file:
    data = file.read()
arr = data.split('\n')
# This block separates the data 2 part the rules and orders.
rules_arr = []
numbers_arr = []
for string in arr:
    if "|" in string:
        rules_arr.append(string)
    else:
        if string != "":
            numbers_arr.append(string)

# Splits all the strings for their specifications in order to get arrays contains rules and numbers in 2 different arr
rules_order = [i.split("|") for i in rules_arr]
numbers_order = [j.split(",") for j in numbers_arr]


wrong_order_arr = []
for num_arr in numbers_order:
    true_order = ""
    for index in range(len(num_arr)):
        if index + 1 < len(num_arr):
            temp_arr = [num_arr[index], num_arr[index + 1]]
            if temp_arr in rules_order:
                true_order = "True"
            else:
                true_order = "False"
                break
    if true_order == "False":
        wrong_order_arr.append(num_arr)


def sort_with_rules(array):
    temp_var = ""
    compare_var = array[0]
    for j in array[1:]:
        temporary = [compare_var, j]
        if temporary in rules_order:
            temp_var = temporary[0]
        elif list(reversed(temporary)) in rules_order:
            temp_var = temporary[1]
        compare_var = temp_var
    # array.remove(temp_var) -> please look at below of the code to understand this comments
    if len(array) > 1:
        array.remove(temp_var)
        return [temp_var] + sort_with_rules(array)
    else:
        return [array[0]]


middle_total = 0
for arr in wrong_order_arr:
    sorted_arr = sort_with_rules(arr)
    middle_index = len(sorted_arr) // 2
    middle_total += int(sorted_arr[middle_index])

print(middle_total)
# When l write remove statement before condition it deletes the temp_var and the checking array's length becomes 1
# For example our list is 61, 13, 29 and correct order will be 61, 29, 13 in this case it will remove 29 before
# condition and 13 will be the only element. Then it will show only 61 and 13 as a result
