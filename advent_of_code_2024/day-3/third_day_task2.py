import re as r

with open("data.txt") as file:
    data = file.read()

storage = []
total_value = 0
do = True
for index in range(len(data)):
    new_seq = data[index: index + 12]
    if "do()" in new_seq:
        do = True
    if "don't()" in new_seq:
        do = False
    if do:
        if r.search("^mul[(].*[)]", new_seq):
            seq = r.search("^mul[(]([0-9]+,[0-9]+)[)]", new_seq)
            # print(f"{new_seq}: {seq}") for checking
            new_str = ""
            if seq is not None:
                for i in seq.group():
                    if i != ')':
                        new_str += i
                    else:
                        new_str += ')'
                        break
            # You should check this block inside the condition, if you don't none value sequences will give index error
            # because new_str will be empty
                numbers = r.findall("[0-9]+,[0-9]+", new_str)
                numbers_array = numbers[0].split(',')
                total_value += (int(numbers_array[0]) * int(numbers_array[1]))
print(total_value)
