import time
start_time = time.time()
with open("data.txt") as file:
    data = file.read()
arr = data.split('\n')


def all_degree_checking(row, column):
    # I used the row and column method instead of finding the index in the data,
    # because there is an empty string at the end of each row.
    # This empty string shifts all indexes by +1, causing the code to behave incorrectly.
    if arr[row][column] == 'A':
        matrix = data.split('\n')
        length_row = len(matrix[0])

        main_d = ""
        second_d = ""
        mas_set = set("MAS")
        if 0 <= row + 1 < len(matrix) and 0 <= row - 1 < len(matrix):
            if 0 <= column + 1 < length_row and 0 <= column - 1 < length_row:
                main_d += matrix[row - 1][column - 1] + matrix[row][column] + matrix[row + 1][column + 1]
                second_d += matrix[row + 1][column - 1] + matrix[row][column] + matrix[row - 1][column + 1]
        if set(main_d) == set(second_d) == mas_set:
            # print(f"{main_d} - {second_d} found at row: {row} column: {column}")
            return 1
    return 0
total_xmas = 0
for arr_row in range(len(arr)):
    for arr_column in range(len(arr[arr_row])):
        total_xmas += all_degree_checking(row=arr_row, column=arr_column)


print(total_xmas)
end_time = time.time()
print(end_time - start_time)
