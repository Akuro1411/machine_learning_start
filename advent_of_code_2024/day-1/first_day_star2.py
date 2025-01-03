with open('data.txt') as file:
    data = file.read()

arr = data.split()

left_array = [int(arr[i]) for i in range(len(arr)) if i % 2 == 0]
right_array = [int(arr[i]) for i in range(len(arr)) if i % 2 == 1]

# We don't need to sort array, but it remains from previous task's code
left_array.sort()
right_array.sort()

total = 0
for left in left_array:
    total += left * right_array.count(left)

print(total)

