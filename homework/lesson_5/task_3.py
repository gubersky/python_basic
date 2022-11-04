value = input("Input number from 3 to 9: ")

numbers = "123456789"

if value.isdigit():
    number = int(value)
    if 3 <= number <= 9:
        for i in range(0, number):
            print(numbers[0:i] + numbers[i::-1])
    else:
        print("Wrong data! Please input number from 3 to 9")
else:
    print("Wrong data! Please input number")


