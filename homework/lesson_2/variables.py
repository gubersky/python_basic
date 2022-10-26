first_var = 7
second_var = 3

temp_var = first_var
first_var = second_var
second_var = temp_var

print(first_var, second_var)

first_num = 5
second_num = 10

first_num, second_num = second_num, first_num

print(first_num, second_num)

one_num = 6
two_num = 8

one_num = one_num + two_num
two_num = one_num - two_num
one_num = one_num - two_num

print(one_num, two_num)
