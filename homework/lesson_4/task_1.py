input_number = input("Input number: ")

same_num = 0
count = 0

for i in input_number:
    count += 1
    for k in input_number:
        if k == i:
            same_num += 1

if same_num != count:
    print("Yes")
else:
    print("No")
