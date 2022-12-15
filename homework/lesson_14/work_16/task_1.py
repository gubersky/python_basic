with open("task.txt", "w") as file:
    while True:
        text = input("Write some string: ")
        file.write(text + "\n")
        if not text.isalnum():
            break
