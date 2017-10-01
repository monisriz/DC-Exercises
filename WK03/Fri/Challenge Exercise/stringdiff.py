# Find the single different character between two strings
#
# Assume two strings str1, str2, where str2 contains the same set of characters
# in str1 with one additional character. Find the signal different character
# between the two strings.

def stringdiff(str1, str2):
    list1=[]
    list2=[]

    for aChar in str1:
        list1.append(aChar)
    for aChar in str2:
        list2.append(aChar)
    set1=set(list1)
    set2=set(list2)
    if set1 == set2:
        print("No different characters")
    else:
        if len(set2) > len(set1):
            print(sorted(set2 - set1))
        else:
            print(sorted(set1 - set2))

stringdiff('abcd', 'abcde')
