with open("data.txt") as file:
    puzzle = file.read()
puzzle_matrix = puzzle.split('\n')


def find_position(matrix):
    for row_index, row in enumerate(matrix):
        if "^" in row:
            return [row_index, row.index("^")]


position = find_position(puzzle_matrix)
total = 0
inside = True
visited_position = []


def up(roadmap, guard, ref):
    global total, inside
    for row in range(guard[0], -1, -1):
        if [row, guard[1]] not in visited_position:
            visited_position.append([row, guard[1]])
            total += 1
        if row == 0:
            inside = False

        elif roadmap[row - 1][guard[1]] == "#":
            position[0] = row
            ref = "right"
            return ref


def right(roadmap, guard, ref):
    global total, inside
    for column in range(guard[1], len(puzzle_matrix[0])):
        if [guard[0], column] not in visited_position:
            visited_position.append([guard[0], column])
            total += 1
        if column == len(puzzle_matrix[0]) - 1:
            inside = False

        elif roadmap[guard[0]][column + 1] == "#":
            position[1] = column
            ref = "down"
            return ref


def down(roadmap, guard, ref):
    global total, inside
    for row in range(guard[0], len(roadmap)):
        if [row, guard[1]] not in visited_position:
            visited_position.append([row, guard[1]])
            total += 1

        if row == len(roadmap) - 1:
            inside = False

        elif roadmap[row + 1][guard[1]] == "#":
            position[0] = row
            ref = "left"
            return ref


def left(roadmap, guard, ref):
    global total, inside
    for column in range(guard[1], -1, -1):
        if [guard[0], column] not in visited_position:
            visited_position.append([guard[0], column])
            total += 1

        if column == 0:
            inside = False

        elif roadmap[guard[0]][column - 1] == "#":
            position[1] = column
            ref = "up"
            return ref


reference = ""
while inside:
    if reference == "" or reference == "up":
        reference = up(puzzle_matrix, position, reference)
    elif reference == "down":
        reference = down(puzzle_matrix, position, reference)
    elif reference == "right":
        reference = right(puzzle_matrix, position, reference)
    elif reference == "left":
        reference = left(puzzle_matrix, position, reference)

print(total)
# Look below link about why l don't use global keyword for modifying position array,
# But l used it when l assign total inside function.
# https://python-forum.io/thread-41434.html#:~:text=If%20you%20pass%20an%20integer,variable%20in%20the%20global%20scope.
