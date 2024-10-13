import json


def display_menu():
    print("\n--Personal Diary--")
    print("1. Add a new diary entry")
    print("2. Display all diary entries")
    print("3. Search for entries by keyword")
    print("4. Delete an entry by number")
    print("5. Exit")
#This is the menu that the user sees

def add_entry(entries, filename="diary_entries.txt"):
    date = input("Enter Date of Entry (DD-MM-YYYY): ")
    content = input("Enter your diary entry: ")
    entry = {"date": date, "content": content}
    entries.append(entry)
    print("Diary entry added.")
    save_entry(entries, filename)
#This part of the script makes the user be able to add an entry to the diary with the date, content and saves it to the list

def view_entries(entries):
    if not entries:
        print("No diary entries found.")
    else:
        for i, entry in enumerate(entries, start=1):
            print(f"\nEntry {i}")
            print(f"Date: {entry['date']}")
            print(f"Content: {entry['content']}")
#This part of the script makes it able for the user to view entries and read the contents of the entry

def search_entries(entries):
    keyword = input("Enter keyword to search: ")
    found = False
    for i, entry in enumerate(entries, start=1):
        if keyword.lower() in entry["content"].lower():
            print(f"Entry {i}")
            print(f"Date: {entry['date']}")
            print(f"Content: {entry['content']}")
            found = True
    if not found:
        print("No diary entries found with that keyword.")
#This part of the script makes it possible for the user to search in their entries by typing in keywords

def delete_entry(entries, filename="diary_entries.txt"):
    view_entries(entries)
    try:
        entry_number = int(input("Enter entry number to delete: "))
        if 1 <= entry_number <= len(entries):
            removed_entry = entries.pop(entry_number - 1)
            print(f"Entry from {removed_entry['date']} deleted.")
            save_entry(entries, filename)
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Please enter a valid entry number.")
#This part of the script makes it possible for the user to delete entries in the diary

def save_entry(entries, filename="diary_entries.txt"):
    with open(filename, "w") as file:
        json.dump(entries, file, indent=4)
    print("Diary entry saved.")
#This script saves the changes made by the user (Deleted or added entries

def load_entries(filename="diary_entries.txt"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No diary entries found.")
        return []
    except json.JSONDecodeError:
        print("Error reading diary entries")
        return []
#This script runs on start of the program and loads all the entries for the user

def diary_main():
    entries = load_entries() #Make an empty list to add entries
    while True:
        display_menu()
        choice = input("\nChoose an option: ")
        if choice == "1":
            add_entry(entries)
        elif choice == "2":
            view_entries(entries)
        elif choice == "3":
            search_entries(entries)
        elif choice == "4":
            delete_entry(entries)
        elif choice == "5":
            save_entry(entries)
            print("Goodbye!")
            break #Exit the loop
        else:
            print("Invalid choice. Please choose again.")
#This is the main menu and correspondents with the input of the user

if __name__ == "__main__":
    diary_main()