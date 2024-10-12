import random
import json


# --- User Login/Registration functions ---
def display_menu():
    print("\nWat wil je doen?:")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    found = False
    for user in users:
        if user["Username"] == username and user["Password"] == password:
            found = True
            print(f"Welcome back, {username}!")
            mainMenu(users)  # Go to the main menu after successful login
            break
    if not found:
        print("No user found with these credentials.")

def register_login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user_creds = {"Username": username, "Password": password}

    for user in users:
        if user["Username"] == username:
            print("This username is already taken.")
            return

    users.append(user_creds)
    print(f"User {username} registered successfully!")

def save_registration(users, filename="UserLogins.txt"):
    with open(filename, "w") as file:
        json.dump(users, file, indent=4)
    print("User credentials saved.")

def load_logins(filename="UserLogins.txt"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No users found. Starting with an empty list.")
        return []
    except json.JSONDecodeError:
        print("Error reading user data.")
        return []

# --- Main program flow ---
def main():
    users = load_logins()  # Load existing users from the file
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            login(users)
        elif choice == "2":
            register_login(users)
            save_registration(users)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

# --- Game and Application Menu ---
def choiceMenu():
    print("\nNanoXL")
    print("1. Play Number Guess")
    print("2. Open Diary")
    print("3. Play Rock, paper, scissors")
    print("4. Log out")

def mainMenu(users):
    while True:
        choiceMenu()
        choice = input("Choose an option: ")
        if choice == "1":
            numberGuess()
        elif choice == "2":
            diary()
        elif choice == "3":
            rockPaperScissors()
        elif choice == "4":
            print("Logging out...")
            break  # Return to the login menu

# --- Number Guess Game ---
def numberGuess():
    playing = True
    computer_guess = random.randrange(1, 100)

    while playing:
        try:
            guess_count = 0
            user_guess = 0
            while user_guess != computer_guess:
                user_guess = int(input("What is your guess?: "))
                if user_guess < computer_guess:
                    print("You need to guess higher")
                    guess_count += 1
                elif user_guess > computer_guess:
                    print("You need to guess lower")
                    guess_count += 1
                else:
                    playing = False
        except ValueError:
            print("This is not a valid number. Please try again.")
    print("Well done!")
    print(f"You did it in {guess_count + 1} guesses!")

# --- Diary Application ---
def diary():
    def displayMenu():
        print("\nPersonal Diary Application")
        print("1. Add a new diary entry")
        print("2. Display all diary entries")
        print("3. Search for entries by keyword")
        print("4. Delete an entry by number")
        print("5. Exit")

    def add_entry(entries, filename="diary_entries.txt"):
        date = input("Enter Date of Entry (DD-MM-YYYY): ")
        content = input("Enter your diary entry: ")
        entry = {"date": date, "content": content}
        entries.append(entry)
        print("Diary entry added.")
        save_entry(entries, filename)

    def view_entries(entries):
        if not entries:
            print("No diary entries found.")
        else:
            for i, entry in enumerate(entries, start=1):
                print(f"\nEntry {i}")
                print(f"Date: {entry['date']}")
                print(f"Content: {entry['content']}")

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

    def save_entry(entries, filename="diary_entries.txt"):
        with open(filename, "w") as file:
            json.dump(entries, file, indent=4)
        print("Diary entry saved.")

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

    entries = load_entries()  # Load diary entries
    while True:
        displayMenu()
        choice = input("Choose an option: ")
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
            break

# --- Rock Paper Scissors Game ---
def rockPaperScissors():
    playing = True
    options = ["rock", "paper", "scissors"]

    while playing:
        computer_choice = random.choice(options)
        player_choice = input("rock, paper or scissors?: ")

        if computer_choice == player_choice:
            print("It's a tie!")
        elif (computer_choice == "rock" and player_choice == "scissors") or \
             (computer_choice == "scissors" and player_choice == "paper") or \
             (computer_choice == "paper" and player_choice == "rock"):
            print("You lose!")
        else:
            print("You win!")

        again = input("Thanks for playing! Want to play again? y/n: ")
        if again.lower() != "y":
            playing = False

# --- Start the program ---
if __name__ == "__main__":
    main()  # Start the login menu
