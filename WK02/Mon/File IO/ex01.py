# Exercise 1

filename = input("Enter the file name: ")
fh = open(filename, 'r')
contents = fh.read()
fh.close()
print(contents)
