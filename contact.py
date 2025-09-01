contacts = {}

def add_contact():
    name = input("Enter store name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print(f" Contact '{name}' added successfully.\n")

def view_contacts():
    if not contacts:
        print(" No contacts found.\n")
        return
    print("\n Contact List:")
    for name, info in contacts.items():
        print(f"- {name}: {info['Phone']}")
    print()

def search_contact():
    query = input("Search by name or phone number: ")
    found = False
    for name, info in contacts.items():
        if query.lower() in name.lower() or query == info["Phone"]:
            print(f"\n Found Contact:\nName: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nAddress: {info['Address']}\n")
            found = True
    if not found:
        print(" No matching contact found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Enter new details (leave blank to keep current):")
        phone = input(f"New phone ({contacts[name]['Phone']}): ") or contacts[name]['Phone']
        email = input(f"New email ({contacts[name]['Email']}): ") or contacts[name]['Email']
        address = input(f"New address ({contacts[name]['Address']}): ") or contacts[name]['Address']
        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print(f" Contact '{name}' updated successfully.\n")
    else:
        print(" Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.\n")
    else:
        print(" Contact not found.\n")

def menu():
    while True:
        print(" Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print(" Exiting Contact Book. Goodbye!")
            break
        else:
            print(" Invalid choice. Please select a valid option.\n")
menu()
