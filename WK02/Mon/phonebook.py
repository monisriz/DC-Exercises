# Write a phone book app

import json

phonebook = {}

def pb_save():
    with open('phonebook.json', 'w') as fh:
        json.dump(phonebook, fh)
    fh.close()
    print("All entries saved.")

def pb_restore():
    global phonebook

    try:
        with open('phonebook.json', 'r') as fh:
            phonebook = json.load(fh)
            print("All entries restored.")

    except:
        phonebook = {}
        print("No entries found.")


def pb_menu():
    while True:
        print("\nElectronic Phone Book")
        print("=====================")
        print("1. Look up an entry")
        print("2. Set an entry")
        print("3. Delete an entry")
        print("4. List all entries")
        print("5. Save all entries")
        print("6. Restore all entries")
        print("7. Quit")

        menu_option = input("Choose an option (1-7): ")

        if menu_option == "1":
            entry_name = input("Enter the name to search: ").upper()
            print(phonebook.get(entry_name, 'No entry found for {}.'.format(entry_name)))

        elif menu_option == "2":
            entry_name = input("Enter name to create an entry: ").upper()
            entry_num = input("Enter phone number for {}: ".format(entry_name))
            phonebook[entry_name] = entry_num
            print("Entry created for {}.".format(entry_name))

        elif menu_option == "3":
            entry_name = input("Enter the name to delete the entry: ").upper()
            if entry_name not in phonebook:
                print("There is no entry for {}".format(entry_name))
            elif len(phonebook) == 1:
                print("Cannot delete. There has to be at least one entry in the database.")
            else:
                del phonebook[entry_name]
                print("Entry deleted for {}.".format(entry_name))

        elif menu_option == "4":
            if len(phonebook) == 0:
                print("No saved entries present.")
            else:
                for key, value in phonebook.items():
                    print("\nName: {}\nPhone number: {}".format(key, value))
        elif menu_option == "5":
            pb_save()

        elif menu_option == "6":
            pb_restore()

        elif menu_option == "7":
            print("Thank you for using my app. Good bye!")
            return False
        else:
            print("Invalid choice. Please choose the correct option.")
pb_menu()
