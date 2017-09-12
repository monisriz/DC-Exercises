# Python Exercises

# #1 Hello, you!
username = input("What is your name? ")
print("Hello, {}!".format(username))


# #2 HELLO, YOU!
uppername = input("WHAT IS YOUR NAME? ")
uppername = uppername.upper()
print("HELLO, {}!".format(uppername))
print("Your name has {} letters in it.".format(len(uppername)))


# #3 Madlib
print("Please fill in the blanks below:")
print("--(your name)-- lives in --(your city)--")
yourname = input("What's your name? ")
yourcity = input("What city do you live in? ")
print(("{} lives in {}.").format(yourname, yourcity))


# #4 Day of the week
day = int(input("Day 0-6)?"))

if day == 0:
    print("Sunday")
elif day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
else:
    print("Please enter a valid number between 0 and 6!")


# #5 Work or Sleep In?
workorsleep = int(input("Day 0-6)?"))

if workorsleep == 0 or workorsleep == 6:
    print("Sleep in")
elif workorsleep > 0 and workorsleep < 6:
    print("Go to work")
else:
    print("Please enter a valid number between 0 and 6!")


# #6 Celsius to Fahrenheit
tempcel = int(input("Please enter the temperature in Celsius: "))
tempfah = tempcel * 1.8 + 32
print("Temperature in Fahrenheit:\n", tempfah, "F")


# #7 Tip Calculator
billamt = float(input("Total bill amount: $"))
svclevel = input("Level of service (Good, Fair or Bad): ").upper()
goodtip = float(0.20 * billamt)
fairtip = float(0.15 * billamt)
badtip = float(0.10 * billamt)
totgood = float(billamt + goodtip)
totfair = float(billamt + fairtip)
totbad = float(billamt + badtip)

if svclevel == "GOOD":
    print("Tip: $", "{:.2f}".format(goodtip))
    print("Total: $", "{:.2f}".format(totgood))
elif svclevel == "FAIR":
    print("Tip: $ ", "{:.2f}".format(fairtip))
    print("Total: $", "{:.2f}".format(totfair))
elif svclevel == "BAD":
    print("Tip: $", "{:.2f}".format(badtip))
    print("Total: $", "{:.2f}".format(totbad))
else:
    print("Please choose from Good, Fair or Bad for the level of service!")


# #8 Tip Calculator 2
billamt = float(input("Total bill amount: $"))
svclevel = input("Level of service (Good, Fair or Bad): ").upper()
goodtip = float(0.20 * billamt)
fairtip = float(0.15 * billamt)
badtip = float(0.10 * billamt)
totgood = float(billamt + goodtip)
totfair = float(billamt + fairtip)
totbad = float(billamt + badtip)
splitin = int(input("How many people to split the bill: "))

if svclevel == "GOOD":
    print("Tip: $", "{:.2f}".format(goodtip))
    print("Total: $", "{:.2f}".format(totgood))
    print("Amount per person: $", "{:.2f}".format(totgood/splitin))
elif svclevel == "FAIR":
    print("Tip: $ ", "{:.2f}".format(fairtip))
    print("Total: $", "{:.2f}".format(totfair))
    print("Amount per person: $", "{:.2f}".format(totfair/splitin))
elif svclevel == "BAD":
    print("Tip: $", "{:.2f}".format(badtip))
    print("Total: $", "{:.2f}".format(totbad))
    print("Amount per person: $", "{:.2f}".format(totbad/splitin))
else:
    print("Please choose from Good, Fair or Bad for the level of service!")


# #9 1 to 10
i = 1
while i < 11:
    print(i)
    i += 1

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
        print("Enter yes or no.")
