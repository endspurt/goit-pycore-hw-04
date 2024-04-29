def parse_input(user_input):
    """Parse the user input into a command and its arguments."""
    parts = user_input.split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def add_contact(args, contacts):
    """Add a new contact to the dictionary."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """Change an existing contact in the dictionary."""
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    """Show the phone number of a given contact."""
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."

def show_all(contacts):
    """Show all saved contacts."""
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts stored."

def main():
    """Main function to run the command loop."""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2:
            print(add_contact(args, contacts))
        elif command == "change" and len(args) == 2:
            print(change_contact(args, contacts))
        elif command == "phone" and len(args) == 1:
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
