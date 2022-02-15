import json 


with open("phonebook.json", "r") as file_handle:
    phonebook = json.load(file_handle)
selection = 0

def get_selection_from_user():
    try:
        selection = int(input("""
Electronic Phone Book 
=====================
1. Look up an entry
2. Set an entry 
3. Delete an entry
4. List all entries 
5. Quit

What do you want to do (1-5): """))
    except ValueError:
        # set dummy value to skip to else statement
        selection = 0 
    return selection

def get_name_from_user():
    return input("\nEnter name: ")

def look_up_entry(name):
    entry = phonebook.get(name)
    if entry:
        print(f"\nFound entry for {name}: {entry}")
    else:
        print(f"\nDid not find an entry for {name}")

def set_entry(name):
    entry_value = input("Enter phone number: ")
    phonebook[name] = entry_value 
    print(f"\nEntry stored for {name}.")

def delete_entry(name):
    entry = phonebook.get(name)
    if entry:
        del phonebook[name]
        print(f"\nDeleted entry for {name}.")
    else:
        print("\nThat name does not exist.")

def list_entries():
    if phonebook:
        for name, number in phonebook.items():
            print(f"\nFound entry for {name}: {number}")
    else:
        print("\nPhone Book is currently empty.")


while selection != 5:
    selection = get_selection_from_user()
    if selection == 1: 
        entry_name = get_name_from_user()
        look_up_entry(entry_name)
    elif selection == 2:
        entry_name = get_name_from_user()
        set_entry(entry_name)
    elif selection == 3:
        entry_name = get_name_from_user()
        delete_entry(entry_name)
    elif selection == 4: 
        list_entries()
    elif selection == 5:
        with open("phonebook.json", "w") as file_handle:
            json.dump(phonebook, file_handle)
        print("\nBye!")
    else:
        print("\nPlease enter a number between 1 and 5")