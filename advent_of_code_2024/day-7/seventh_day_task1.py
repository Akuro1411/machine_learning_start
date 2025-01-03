with open("data.txt") as file:
    data = file.read().splitlines()


def combination_create(length):
    # Function creates the binary representation of operations: 1 represents * and 0 represents +
    combinations = []
    for i in range(2 ** length):
        combinations.append(bin(i)[2:].zfill(length))
    return combinations


def calculate_result(operations, arr):
    total = arr[0]
    for index, operation in enumerate(operations):
        if operation == "1":
            total *= arr[index + 1]
        if operation == "0":
            total += arr[index + 1]
    return total


total_answer = 0
for row in data:
    equation = row.split(":")
    numbers = list(map(int, equation[1].split(" ")[1:]))
    possible_combinations = combination_create(len(numbers) - 1)
    for combination in possible_combinations:
        if calculate_result(combination, numbers) == int(equation[0]):
            total_answer += int(equation[0])
            break


print(total_answer)

# With converting indexes to binary...
# l can find all the combinations filling their binary representations with zeros at beginning.
# [1, 2, 3, 4] 4 numbers have 3 spaces between them which is possible to set operations.
# 0 000 +++
# 01 001 ++*
# 10 010 +*+
# 11 011 +**
# 100 100 *++
# 101 101 *+*
# 110 110 **+
# 111 111 ***

