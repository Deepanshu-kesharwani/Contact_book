import re

def is_valid_email(email):
    # Regular expression for validating an Email
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    # Using fullmatch to check the pattern
    if re.fullmatch(pattern, email):
        return True
    else:
        return False

contacts = {}


def is_valid_mobile(mobile):
    # Check if the mobile number is exactly 10 digits long
    return len(mobile) == 10 and mobile.isdigit()


while True:
    print("\nContact book ")
    print("1: Create Contact ")
    print("2: Update Contact ")
    print("3: View Contact ")
    print("4: Search Contact ")
    print("5: Delete Contact ")
    print("6: Count Contact ")
    print("7: Exit ")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter the name: ")
        if name in contacts:
            print(f'Contact name {name} already exists')
        else:
            age = input("Enter the age: ")
            email = input("Enter the email: ")
            while not is_valid_email(email):
                print("Invalid email id ")
                email = input("Enter the email: ")
            mobile = input("Enter the mobile number: ")

            # Validate the mobile number
            while not is_valid_mobile(mobile):
                print("Invalid mobile number! It should be exactly 10 digits.")
                mobile = input("Enter a valid 10-digit mobile number: ")

            contacts[name] = {'Age': int(age), 'Email': email, 'Mobile_Number': mobile}
            print(f'Contact name {name} created successfully')

    elif choice == 2:
        name = input("Enter the contact name you want to update: ")
        if name in contacts:
            age = input("Enter the age: ")
            email = input("Enter the email: ")
            while not is_valid_email(email):
                print("Invalid email id ")
                email = input("Enter the email: ")
            mobile = input("Enter the mobile number: ")

            # Validate the mobile number
            while not is_valid_mobile(mobile):
                print("Invalid mobile number! It should be exactly 10 digits.")
                mobile = input("Enter a valid 10-digit mobile number: ")

            contacts[name] = {'Age': int(age), 'Email': email, 'Mobile_Number': mobile}
            print(f'Contact name {name} updated successfully')
        else:
            print("Contact not found")

    elif choice == 3:
        name = input("Enter the contact name you want to view: ")
        if name in contacts:
            contact = contacts[name]
            print(
                f'Name: {name}, Age: {contact["Age"]}, Email: {contact["Email"]}, Mobile Number: {contact["Mobile_Number"]}')
        else:
            print("Contact not found")

    elif choice == 4:
        search_name = input("Enter the contact to search: ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(
                    f'Found-- Name: {name}, Age: {contact["Age"]}, Email: {contact["Email"]}, Mobile Number: {contact["Mobile_Number"]}')
                found = True
        if not found:
            print("Contact not found!!!")

    elif choice == 5:
        name = input("Enter the name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} deleted successfully!!')
        else:
            print("Contact not found")

    elif choice == 6:
        print(f'Total contacts in the book: {len(contacts)}')

    elif choice == 7:
        print("Closing the app!!!")
        break
    else:
        print("Invalid choice")
