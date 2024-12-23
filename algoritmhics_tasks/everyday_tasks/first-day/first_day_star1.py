with open('data.txt') as file:
    data = file.read()

arr = data.split()

left_array = [int(arr[i]) for i in range(len(arr)) if i % 2 == 0]
right_array = [int(arr[i]) for i in range(len(arr)) if i % 2 == 1]

left_array.sort()
right_array.sort()

total = 0
for left, right in zip(left_array, right_array):
    total += abs(left - right)

print(total)
