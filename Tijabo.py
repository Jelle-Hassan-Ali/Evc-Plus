contacts = []

def add_contact():
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number of the contact: ")
    contact = {'name': name, 'phone': phone}
    contacts.append(contact)
    print(f"Contact '{name}' with phone number '{phone}' added successfully.")

def remove_contact():
    name = input("Enter the name of the contact to remove: ")
    removed = False
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print(f"Contact '{name}' removed successfully.")
            removed = True
            break
    if not removed:
        print(f"Contact '{name}' not found.")

def view_contacts():
    if contacts:
        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No contacts found.")

while True:
    print("\n--- Contact Management ---")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. View Contacts")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        remove_contact()
    elif choice == '3':
        view_contacts()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
