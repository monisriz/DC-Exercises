# Exercise 1

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict)
# 1
print("Print Elizabeth's number:")
print(phonebook_dict['Elizabeth'])
print("\n")
# 2
print("Add Kareem's number:")
phonebook_dict['Kareem'] = '938-489-1234'
print(phonebook_dict['Kareem'])
print(phonebook_dict)
print("\n")
# 3
print("Delete Alice's phone entry:")
del phonebook_dict['Alice']
print(phonebook_dict)
print("\n")
# 4
print("Change Bob's number:")
phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict)
print("\n")
#5
print("Print all entries:")
for i in phonebook_dict.items():
    print(i)
