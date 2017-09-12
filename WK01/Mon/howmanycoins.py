#10 How many coins?

count = 0
print("You currently have {} coins.".format(count))
while True:
    wantone = input("Do you want another coin? (yes or no) ").lower()
    if wantone == "yes":
        count += 1
        print("You now have have {} coins.".format(count))
    elif wantone == "no":
        print("Your final count is {} coins.".format(count))
        break
    else:
        print("Please enter yes or no.")
