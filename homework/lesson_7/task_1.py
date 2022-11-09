new_list = []
for i in range(10, 250):
    new_list.append(i)
    if i % 20 == 0:
        new_list.remove(i)

print(new_list)
