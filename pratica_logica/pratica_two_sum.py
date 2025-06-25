def two_sum(list, target):
    new_list = []

    for x in range(len(list)):
        for y in range(len(list)):
            if x == y:
                continue
            if list[x] + list[y] == target and (y, x) not in new_list:
                new_list.append((x, y))
            
    return new_list


list = [2, 3, 6, 7, 11, 15]

target = 9

new_list = two_sum(list, target)

print(list)
print(new_list if new_list else 'Lista não a somas igual ao número alvo!')