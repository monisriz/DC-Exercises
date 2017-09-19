# Bonus challenge - Print top 3 values of the letter count

import string
count = {}

def letter_histogram():
    word = input("Enter a word: ").lower()
    for achar in word:
        if achar in string.ascii_lowercase:
            count_letter = count.get(achar, 0)
            count[achar] = count_letter + 1
    # print(count)
    count_list = list(count.items())
    print(count_list)
    sorted_list = sorted(count_list, key=lambda lettercount:lettercount[1], reverse=True)
    print(sorted_list)
    topthree = sorted_list[0:3]
    print("The most used letters are: {}, {} and {}.".format(topthree[0][0], topthree[1][0], topthree[2][0]))

letter_histogram()
