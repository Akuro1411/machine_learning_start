with open("data.txt") as file:
    puzzle = file.read()
puzzle_matrix = puzzle.split('\n')


def find_position(matrix):
    for row_index, row in enumerate(matrix):
        if "^" in row:
            return [row_index, row.index("^")]


start, position = find_position(puzzle_matrix), find_position(puzzle_matrix)
total = 0
total_barriers = 0
inside = True
visited_position = []


def set_barrier(obj,  ref):
    row, column = obj[0], obj[1]
    obj_row, obj_column = start[0], start[1]
    # if we write it as new_matrix = puzzle_matrix both of them will point same array, and it won't create own local arr
    # In python everything is object, due to this if we want to create new local arr, we should write it as below.
    new_matrix = puzzle_matrix.copy()
    new_row = "".join(list(map(lambda x: x.replace("^", "."), new_matrix[obj_row])))
    new_matrix[obj_row] = new_row
    new_obj_row = list(new_matrix[row])
    new_obj_row[column] = "^"
    new_matrix[row] = "".join(new_obj_row)

    if ref == "" or ref == "up":
        if row > 0:
            row -= 1
    elif ref == "right":
        if column < len(new_matrix[row]) - 1:
            column += 1
    elif ref == "left":
        if column > 0:
            column -= 1
    elif ref == "down":
        if row < len(new_matrix) - 1:
            row += 1

    new_row = ""
    for i in range(len(new_matrix[row])):
        if i == column:
            new_row += "#"
            continue
        new_row += new_matrix[row][i]
    new_matrix[row] = new_row
    return new_matrix


def check_for_loop(start_pos, matrix, refer):
    global total_barriers
    position = start_pos
    positions = []
    while inside:
        if position not in positions:
            positions.append(position)
        elif position == start_pos and (position in positions):
            return 1
        if refer == "" or refer == "up":
            t = up(matrix, position, refer)
            print(t)
            refer, position = t[0], t[1]
        elif refer == "down":
            t = down(matrix, position, refer)
            refer, position = t[0], t[1]
        elif refer == "right":
            t = right(matrix, position, refer)
            refer, position = t[0], t[1]
        elif refer == "left":
            t = left(matrix, position, refer)
            refer, position = t[0], t[1]
        print(positions)


def up(roadmap, guard, ref):
    global total, inside, total_barriers
    for row in range(guard[0], -1, -1):
        if [row, guard[1]] not in visited_position:
            visited_position.append([row, guard[1]])
            total += 1
        if row == 0:
            inside = False

        elif roadmap[row - 1][guard[1]] == "#":
            position[0] = row
            ref = "right"
            return ref, position
        obj_pos = [row, guard[1]]
        new = set_barrier(obj_pos, ref)
        total_barriers += check_for_loop(obj_pos, new, ref)


def right(roadmap, guard, ref):
    global total, inside, total_barriers
    for column in range(guard[1], len(puzzle_matrix[0])):
        if [guard[0], column] not in visited_position:
            visited_position.append([guard[0], column])
            total += 1
        if column == len(puzzle_matrix[0]) - 1:
            inside = False

        elif roadmap[guard[0]][column + 1] == "#":
            position[1] = column
            ref = "down"
            return ref, position
        obj_pos = [guard[0], column]
        new = set_barrier(obj_pos, ref)
        total_barriers += check_for_loop(obj_pos, new, ref)


def down(roadmap, guard, ref):
    global total, inside, total_barriers
    for row in range(guard[0], len(roadmap)):
        if [row, guard[1]] not in visited_position:
            visited_position.append([row, guard[1]])
            total += 1

        if row == len(roadmap) - 1:
            inside = False

        elif roadmap[row + 1][guard[1]] == "#":
            position[0] = row
            ref = "left"
            return ref, position
        obj_pos = [row, guard[1]]
        new = set_barrier(obj_pos, ref)
        total_barriers += check_for_loop(obj_pos, new, ref)


def left(roadmap, guard, ref):
    global total, inside, total_barriers
    for column in range(guard[1], -1, -1):
        if [guard[0], column] not in visited_position:
            visited_position.append([guard[0], column])
            total += 1

        if column == 0:
            inside = False

        elif roadmap[guard[0]][column - 1] == "#":
            position[1] = column
            ref = "up"
            return ref, position
        obj_pos = [guard[0], column]
        new = set_barrier(obj_pos, ref)
        total_barriers += check_for_loop(obj_pos, new, ref)


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
print(total_barriers)

# Look below link about why l don't use global keyword for modifying position array,
# But l used it when l assign total inside function.
# https://python-forum.io/thread-41434.html#:~:text=If%20you%20pass%20an%20integer,variable%20in%20the%20global%20scope.

