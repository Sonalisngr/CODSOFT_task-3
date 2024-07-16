import pickle

class Contact:
    def __init__(self, name, phone, email, address):
        """
        Initialize a new contact with name, phone, email, and address.
        """
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        """
        Return a string representation of the contact.
        """
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self, filename='contacts.pkl'):
        """
        Initialize the contact book. Load existing contacts from a file.
        """
        self.filename = filename
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
        """
        Load contacts from a file using pickle. Return an empty list if the file does not exist.
        """
        try:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []
    
    def save_contacts(self):
        """
        Save contacts to a file using pickle.
        """
        with open(self.filename, 'wb') as file:
            pickle.dump(self.contacts, file)
    
    def add_contact(self, name, phone, email, address):
        """
        Add a new contact to the contact book and save the updated list.
        """
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        self.save_contacts()
    
    def view_contacts(self):
        """
        Print all contacts in the contact book.
        """
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)
    
    def search_contacts(self, search_term):
        """
        Search for contacts by name or phone number and print the results.
        """
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not results:
            print("No contacts found.")
        else:
            for contact in results:
                print(contact)
    
    def update_contact(self, search_term, name=None, phone=None, email=None, address=None):
        """
        Update the details of a contact found by name or phone number.
        """
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                if name:
                    contact.name = name
                if phone:
                    contact.phone = phone
                if email:
                    contact.email = email
                if address:
                    contact.address = address
                self.save_contacts()
                print("Contact updated.")
                return
        print("Contact not found.")
    
    def delete_contact(self, search_term):
        """
        Delete a contact found by name or phone number.
        """
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact deleted.")
                return
        print("Contact not found.")

def main():
    """
    Main function to run the contact book application.
    """

    contact_book = ContactBook()
    
    while True:
        # Print the menu
        print("\n\n################## Contact Book Menu ##################:")
        print("\n\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        
        # Get the user's choice
        choice = input("\n\n\t\t\t\t\t\tEnter your choice: ")
        
        if choice == '1':
            # Add a new contact
            name = input("\nEnter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            # View all contacts
            contact_book.view_contacts()
        elif choice == '3':
            # Search for a contact
            search_term = input("\nEnter name or phone to search: ")
            contact_book.search_contacts(search_term)
        elif choice == '4':
            # Update a contact
            search_term = input("\nEnter name or phone to search for updating: ")
            print("Leave blank if you don't want to update a field.")
            name = input("\nEnter new name (leave blank to skip): ")
            phone = input("Enter new phone (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            address = input("Enter new address (leave blank to skip): ")
            contact_book.update_contact(search_term, name or None, phone or None, email or None, address or None)
        elif choice == '5':
            # Delete a contact
            search_term = input("\nEnter name or phone to delete: ")
            contact_book.delete_contact(search_term)
        elif choice == '6':
            # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()