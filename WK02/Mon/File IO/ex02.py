# Exercise 2

filename = input("Enter the file name: ")
usertext = input("Enter the contents of the file: ")

fh = open(filename, 'w')
fh.write(usertext)
fh.close()
