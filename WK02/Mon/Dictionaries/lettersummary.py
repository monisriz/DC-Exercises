# Letter summary

import string
count = {}

def letter_histogram():
    word = input("Enter a word: ").lower()
    for achar in word:
        if achar in string.ascii_lowercase:
            count_letter = count.get(achar, 0)
            count[achar] = count_letter + 1
    print(count)

letter_histogram()
