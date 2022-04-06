name = (input("Please Enter Your Name: ")).upper()


def word_count(n):
    word = {}
    for i in range(len(n)):
        word[n[i]] = n.count(n[i])
    return word


print(f"\nWord Count of Your Name: \n{word_count(name)}")
