# Contact manager application
def display_menu():
    print("\nWelcome to Contact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    if any(contact[0] == name for contact in contacts):
        print("Contact with this name already exists!")
    else:
        contacts.append((name, phone, email))
        print("Contact added successfully!")
    
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\nList of Contacts:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact[0]} - {contact[1]} - {contact[2]}")
    
def search_contact(contacts):
    name = input("Enter name to search: ")
    for contact in contacts:
        if contact[0] == name:
            print(f"Contact Found: {contact[0]} - {contact[1]} - {contact[2]}")
            return
    print("Contact not found!")
    
def update_contact(contacts):
    name = input("Enter name to update: ")
    for i, contact in enumerate(contacts):
        if contact[0] == name:
            new_phone = input("Enter new phone number: ")
            contacts[i] = (contact[0], new_phone, contact[2])
            print("Contact updated successfully!")
            return
    print("Contact not found!")
    
def delete_contact(contacts):
    name = input("Enter name to delete: ")
    for i, contact in enumerate(contacts):
        if contact[0] == name:
            contacts.pop(i)
            print("Contact deleted successfully!")
            return
    print("Contact not found!")
    
def main():
    contacts = []
    print("Welcome! Contact Manager Application")
    while True:
        display_menu()
        choice = input("Enter your choice: ")    
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
            
if __name__ == "__main__":
    main()
