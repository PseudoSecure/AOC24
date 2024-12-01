array1 = []
array2 = []
map2 = {}
i = 0

with open('input_part2.txt', 'r') as file:
    for line in file:
        elements = line.strip().split('   ')
        array1.append(int(elements[0]))
        array2.append(int(elements[1]))


for number in array2:
    if number not in map2:
        map2[number] = 1
    else:
        map2[number] = map2[number] + 1


for number in array1:
    try:
        if map2[number]:
            i = i + map2[number] * number
    except KeyError:
        continue


print(i)
