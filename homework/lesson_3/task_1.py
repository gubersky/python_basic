student_count = input("Input the number of students")
apple_count = input("Input the number of apples")

students = int(student_count)
apples = int(apple_count)

students_received = apples // students
basket_balance = apples % students

if apples >= students:
    print("Every schoolchild got:", students_received, "apples")
    print("The apple remained in the basket:", basket_balance)
else:
    print("There are not enough apples for all students")

