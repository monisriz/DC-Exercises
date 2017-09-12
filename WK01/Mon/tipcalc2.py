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
