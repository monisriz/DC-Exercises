# Letter summary - print a count of each letter in the string

import string

count = {}
def letter_histogram():
    word = input("Enter a word: ").lower()
    for achar in word:
        if achar in string.ascii_lowercase:
            if achar not in count:
                count[achar] = 1
            else:
                count[achar] += 1
    print(count)

letter_histogram()
