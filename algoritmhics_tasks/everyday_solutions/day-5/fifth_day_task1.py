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

total = 0
for num_arr in numbers_order:
    true_order = ""
    for index in range(len(num_arr)):
        if index + 1 < len(num_arr):
            temp_arr = []
            temp_arr.append(num_arr[index])
            temp_arr.append(num_arr[index + 1])
            if temp_arr in rules_order:
                true_order = "True"
            else:
                true_order = "False"
                break
    if true_order == "True":
        middle_index = len(num_arr) // 2
        total += int(num_arr[middle_index])

print(total)
