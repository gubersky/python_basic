first_class = input("Input the number of students in first class")
second_class = input("Input the number of students in second class")
third_class = input("Input the number of students in third class")

count_desks = int(first_class) + int(second_class) + int(third_class)
count_remainder = count_desks % 2
result = (count_desks + count_remainder) // 2

print("You need to buy:", result, "desks")
