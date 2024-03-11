def add_contact(contacts):
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contacts[name] = number
    print("Contact added successfully!")

def view_contacts(contacts):
    print("Contacts:")
    for name, number in contacts.items():
        print(f"{name}: {number}")

def main():
    contacts = {}
    while True:
        print("\nChoose an option:")
        print("1. Add a contact")
        print("2. View contacts")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
