# Word summary

import string

count = {}
def word_histogram():
    para = input("Enter a sentence: ").lower()
    para_split = para.split()
    for aword in para_split:
        filtered_word = ""
        for achar in aword:
            if achar in string.ascii_lowercase:
                filtered_word += achar

        if filtered_word in count:
            count[filtered_word] = count[filtered_word] + 1
        else:
            count[filtered_word] = 1
    print(count)

word_histogram()
