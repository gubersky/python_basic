value = input("Enter more than 2 words: ").strip()

text = value.split(" ")
text.sort()
count = 0

if value.count(" ") >= 2:
    for i in range(text.count("")):
        text.remove("")
else:
    print("Wrong data! Please enter more than 2 words")

for i in range(len(text)):
    count += 1
    print(f"{i} {text[i]}")

print("Number of words:", count)
