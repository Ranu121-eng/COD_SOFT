<<<<<<< HEAD
# Contact Book Task
print("Welcome to the Contact Book!")

# Creating an empty dictionary to store contacts
my_contacts = {}

# Menu options
while True:
    print("Please choose an option:")
    print("1. Add a contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Update contact")
    print("6. Exit")

    # Getting user input for option choice
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        my_contacts[name] = phone
        print(f"Contact {name} added successfully!")
    # print(my_contacts)
    elif choice == '2':
        print("All contacts:")
        for name, phone in my_contacts.items():
            print(f"{name}: {phone}")
    elif choice == '3':
        name = input("Enter contact name to search: ")
        if name in my_contacts:
            print(f"{name}: {my_contacts[name]}")
        else:
            print(f"Contact {name} not found.")
    elif choice == '4':   
        name = input("Enter contact name to delete: ")
        if name in my_contacts:
            del my_contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact {name} not found.")
    elif choice == '5':
        name = input("Enter contact name to update: ")
        if name in my_contacts:
            phone = input("Enter new phone number: ")
            my_contacts[name] = phone
            print(f"Contact {name} updated successfully!")
        else:
            print(f"Contact {name} not found.")
    elif choice == '6':
        print("Exiting the Contact Book. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
=======
# Creating a mini calculator that can perform basic arithmetic operations (addition, subtraction, multiplication, division) on two numbers. The calculator should take user input for the two numbers and the desired operation, and then output the result.
# 3 steps to implement the calculator functionality
#    1. Functions for operations
#    2. User input
#    3. Print result

# Function to perform the desired operation
def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operation == 'average':
        return (num1 + num2) / 2
    else:
        return "Error: Invalid operation."
# User input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the desired operation: ")

# Print result
print("Result:", calculate(num1, num2, operation))
>>>>>>> 6e38181f9fd9362fc12d247637003302bcac6c1e
