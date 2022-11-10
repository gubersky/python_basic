first_list = [1, 2, 5, 7, 9, 99, 7, 200, 39, 2]
second_list = [5, 42, 29, 345, 50, 33, 7, 2, 201, 9, 2, 132, 45, 23, 934]
count = 0
for i in first_list:
    for k in second_list:
        if i == k:
            count += 1
            second_list.remove(i)

print("|" + "-" * 24 + "|")
print(f"|The number of matches: {count}|")
print("|" + "-" * 24 + "|")