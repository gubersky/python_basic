count_value = 0
count_iteration = 0
even_number = 0
odd_number = 0
max_number = 0
min_number = 0

while True:
    value = int(input("Input value: "))
    count_value += value
    if value == 0:
        break
    count_iteration += 1
    if min_number == 0:
        min_number = value
    if value > max_number:
        max_number = value
    if value < min_number != 0 and value != 0:
        min_number = value
    if value % 2 == 0:
        even_number += 1
    else:
        odd_number += 1

arithmetic_mean = count_value / count_iteration

print("The sum of numbers:", count_value)
print("Arithmetic average of all numbers:", arithmetic_mean)
print("Max number is:", max_number)
print("Min number is:", min_number)
print("Number of even:", even_number)
print("Number of odd:", odd_number)
