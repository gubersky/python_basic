first_class = input("Input the number of students in first class")
second_class = input("Input the number of students in second class")
third_class = input("Input the number of students in third class")

count_first = int(first_class) % 2
result_first = (int(first_class) + int(count_first)) // 2

count_second = int(second_class) % 2
result_second = (int(second_class) + int(count_second)) // 2

count_third = int(third_class) % 2
result_third = (int(third_class) + int(count_third)) // 2

overall = result_first + result_second + result_third

print("You need to buy:", overall, "desks")
