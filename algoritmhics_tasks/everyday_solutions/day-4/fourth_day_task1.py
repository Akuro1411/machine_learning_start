import time
start_time = time.time()
with open("data.txt") as file:
    data = file.read()
arr = data.split('\n')
# print(arr)

def check_front_back(number, idx):
    xmas = ""
    if number < 0:
        for shift in range(number, 0):
            # This block shifts the letters to the left and find xmas word at the left of the letter
            if index + shift < len(data):
                # print(data[index + shift])
                xmas += data[idx + shift]
        if xmas == "XMAS":
            return 1
        return 0
    for shift in range(number):
        # This block shifts the letters to the right and find xmas word at the right of the letter
        if index + shift < len(data):
            # print(data[index + shift])
            xmas += data[idx + shift]
    if xmas == "XMAS":
        return 1
    return 0


def all_degree_checking(idx=0, x_axis=0, y_axis=0):
    matrix = data.split('\n')
    length_row = len(matrix[0])
    # We define the row and column of letter in string with this logic.
    position_of_letter_row = idx // length_row
    position_of_letter_column = idx - (position_of_letter_row * length_row)

    xmas = ""
    for i in range(4):
        # This block checks for the row on matrix and column in the row for not exceeding the length of them.
        if len(matrix) > position_of_letter_row + y_axis * i >= 0:
            if 0 <= position_of_letter_column + x_axis * i < length_row:
                xmas += matrix[position_of_letter_row + y_axis * i][position_of_letter_column + x_axis * i]
    if xmas == "XMAS":
        # print("XMAS found at this index: {} x: {} and y: {}".format(idx, x_axis, y_axis))
        return 1
    return 0


total_xmas = 0
for index in range(len(data)):
    # total_xmas += check_front_back(4, index) + check_front_back(-4, index)
    total_xmas += all_degree_checking(idx=index, x_axis=1, y_axis=0)
    total_xmas += all_degree_checking(idx=index, x_axis=-1, y_axis=0)
    total_xmas += all_degree_checking(idx=index, x_axis=1, y_axis=1)
    total_xmas += all_degree_checking(idx=index, x_axis=-1, y_axis=-1)
    total_xmas += all_degree_checking(idx=index, x_axis=1, y_axis=-1)
    total_xmas += all_degree_checking(idx=index, x_axis=-1, y_axis=1)
    total_xmas += all_degree_checking(idx=index, x_axis=0, y_axis=1)
    total_xmas += all_degree_checking(idx=index, x_axis=0, y_axis=-1)

print(total_xmas)

end_time = time.time()
differ = end_time - start_time
print("Total execution time: {}".format(differ))
