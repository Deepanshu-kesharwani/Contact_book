
# Contact Book Application

This is a simple Python-based Contact Book application that allows users to create, update, view, search, delete, and count contacts. The program ensures proper validation for email and mobile numbers to maintain data integrity.

## Features

1. **Create Contact**: Add a new contact with a name, age, email, and mobile number.
2. **Update Contact**: Modify details of an existing contact.
3. **View Contact**: View the details of a specific contact.
4. **Search Contact**: Search for contacts using partial or full names.
5. **Delete Contact**: Remove a contact from the book.
6. **Count Contacts**: Check the total number of saved contacts.
7. **Exit**: Close the application.

## Validation Rules

- **Email**: Must be in a valid email format (e.g., `example@domain.com`).
- **Mobile Number**: Must be exactly 10 digits long.

## How to Run

1. Ensure Python 3.x is installed on your machine.
2. Copy the script to a `.py` file (e.g., `contact_book.py`).
3. Run the script using the command:
   ```
   python contact_book.py
   ```

## Example

```python
Enter your choice: 1
Enter the name: John
Enter the age: 25
Enter the email: john.doe@example.com
Enter the mobile number: 1234567890
Contact name John created successfully
```

## Code Explanation

The program uses:
- **Dictionaries** to store contacts with names as keys.
- **Regular Expressions** to validate email format.
- **While Loops** to keep the program running and ensure valid input.

## Improvements

- Add functionality to save and load contacts from a file for persistence.
- Enhance the user interface with GUI support using libraries like Tkinter or PyQt.

---

