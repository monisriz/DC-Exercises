# Exercise 3

import string

filename = input("Enter the file name: ")
fh = open(filename, 'r')
contents = fh.read()

count_l = {}
count_w = {}
def letter_histogram(word):
    for achar in word:
        if achar in string.ascii_lowercase:
            count_letter = count_l.get(achar, 0)
            count_l[achar] = count_letter + 1
    print(sorted(count_l.items()))

def word_histogram(para):
    para_split = para.split()
    for aword in para_split:
        filtered_word = ""
        for achar in aword:
            if achar in string.ascii_lowercase:
                filtered_word += achar

        if filtered_word in count_w:
            count_w[filtered_word] = count_w[filtered_word] + 1
        else:
            count_w[filtered_word] = 1
    print(count_w)


letter_histogram(contents)
word_histogram(contents)
