# #10 Print a banner

bannertext = input("Enter the string for the banner:\n")

textlength = len(bannertext)
bannerW = textlength + 4

print("*" * bannerW)
print("* "+bannertext+" *")
print("*" * bannerW)
