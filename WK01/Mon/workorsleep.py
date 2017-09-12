# #5 Work or Sleep In?
workorsleep = int(input("Day 0-6)?"))

if workorsleep == 0 or workorsleep == 6:
    print("Sleep in")
elif workorsleep > 0 and workorsleep < 6:
    print("Go to work")
else:
    print("Please enter a valid number between 0 and 6!")
