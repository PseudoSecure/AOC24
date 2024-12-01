array1 = []
array2 = []
i = 0

with open('input_part1.txt', 'r') as file:
    for line in file:
        elements = line.strip().split('   ')
        array1.append(int(elements[0]))
        array2.append(int(elements[1]))


sorted_array_1 = sorted(array1)
sorted_array_2  =sorted(array2)

for index, ele in enumerate(sorted_array_1):
    i = i + abs(sorted_array_1[index] - sorted_array_2[index])
print(i)