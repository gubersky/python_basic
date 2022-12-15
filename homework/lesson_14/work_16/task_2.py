def longest_words(file):
    with open(file, "r", encoding="utf-8") as text:
        word = ""
        temp_list = []
        for i in text:
            words = i.replace("\"", "").split()
            for k in words:
                if len(k) >= len(word):
                    word = k
                    temp_list.append(k)
    word_list = []
    for i in range(len(temp_list)):
        if len(word) == len(temp_list[i]):
            word_list.append(temp_list[i])
    for i in range(len(word_list)):
        print("{:>5}".format(word_list[i]), end='')
        print()


if __name__ == '__main__':
    longest_words("article.txt")
