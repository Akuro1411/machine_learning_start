import time


with open("data.txt") as file:
    data = file.read().splitlines()


def combination_create(length):
    # Function creates the binary representation of operations: 1 represents * and 0 represents +
    combinations = []
    for i in range(3 ** length):
        combinations.append(ternary(i).zfill(length))
    return combinations


def ternary(number):
    str_number = ""
    while number > 0:
        remain = number % 3
        str_number = str(remain) + str_number
        number = number // 3
    return str_number


def calculate_result(operations, arr):
    total = arr[0]
    for index, operation in enumerate(operations):
        if operation == "1":
            total *= arr[index + 1]
        if operation == "0":
            total += arr[index + 1]
        if operation == "2":
            # Here l changed the value of total, due to l don't need adding concatenated number to total. l need just...
            # concatenate them. 192: 17 8 14 -> If l add: 17 += int(str(17) + str(8)), but correct way is ...
            # 17 = int(str(17) + str(8)) in programming it will replace the value of 17 with concatenated number 178...
            # will not add them.
            total = int(str(total) + str(arr[index + 1]))
    return total


start_time = time.time()
total_answer = 0
for row in data:
    equation = row.split(":")
    numbers = list(map(int, equation[1].split(" ")[1:]))
    answer = int(equation[0])
    possible_combinations = combination_create(len(numbers) - 1)
    for combination in possible_combinations:
        if calculate_result(combination, numbers) == answer:
            total_answer += int(equation[0])
            # If there are 2 possible way, the code will evaluate it 2 time but l need only 1
            break


print(total_answer)
end_time = time.time()
print(end_time - start_time)
# In this code l converted all combinations to ternary numbers and using them for operations
# [1, 2, 3, 4] - in this case there 3^(n-1) combinations with "+ * |" operators.
# 7290: 6 8 6 15 - only one combination makes it true, 6 * 8 | 6 * 15
# It will evaluate like that: 6 * 8 = 48, 48 | 6 = 486, 486 * 15 = 7290
