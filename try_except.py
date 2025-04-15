# exception_handler.py

# Basic try-except

def basic_example():
    print("\n\tBasic try-except\n")
    print("Definition: 'try-except' is used to catch and handle errors that occur during code execution.")
    try:
        num = int(input("\nEnter a number: "))
        print(f"\nYou Entered: {num}")
    except ValueError:
        print("\nInvalid input! Please enter a valid number.")


# try-except-else


def else_example():
    print("\n\ttry-except-else\n")
    print("Definition: 'else' runs if no exception is raised in the try block.")
    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("\nDivision by zero!")
    else:
        print(f"\nDivision successful, result is {result}")


# try-except-finally

def finally_example():
    print("\n\ttry-except-finally\n")
    print("Definition: 'finally' block always runs, no matter if an exception occurs or not.")
    try:
        file = open("sample.txt", "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("\nFile not found.")
    finally:
        print("\nExecution completed. Closing resources if open.")



    # Catching specific exceptions
def specific_exception():
    print("\n\tCatching specific exceptions\n")
    print("Definition: Catch specific exception types (like IndexError) to handle different errors precisely.")
    try:
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError:
        print("\nIndex out of range!")



    # Handling multiple exceptions
def multiple_exceptions():
    print("\n\tHandling multiple exceptions\n")
    print("Definition: Use multiple except blocks to handle different types of errors separately.")
    try:
        a = int(input("\nEnter number: "))
        b = int(input("\nEnter divisor: "))
        result = a / b
    except ValueError:
        print("\nInvalid input! Enter numbers only.")
    except ZeroDivisionError:
        print("\nCannot divide by zero.")
    else:
        print(f"\nResult is {result}")


# Using raise for custom error


def raise_example():
    print("\n\tUsing raise for custom error\n")
    print("Definition: 'raise' allows you to trigger exceptions manually.")
    age = int(input("\nEnter your age: "))
    if age < 0:
        raise ValueError("\nAge cannot be negative!")
    print(f"\nYour age is {age}")


# Custom Exception Class


class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

def custom_exception_class():
    print("\n\tCustom Exception Class\n")
    print("Definition: Create your own error types using classes derived from 'Exception'.")
    try:
        user_input = int(input("\nEnter a number above 10: "))
        if user_input <= 10:
            raise CustomError("\nNumber must be greater than 10!")
        print("\nValid number entered.")
    except CustomError as ce:
        print(f"Custom Error: {ce}")


# Run the examples
if __name__ == "__main__":
    
    print("\nChoose an example to run:")
    print("1. Basic try-except")
    print("2. try-except-else")
    print("3. try-except-finally")
    print("4. Catching specific exceptions")
    print("5. Handling multiple exceptions")
    print("6. Using raise for custom error")
    print("7. Custom Exception Class")
    print("0. Exit")

    choice = input("\nEnter your choice (0-7): ")

    if choice == "1":
        basic_example()
    elif choice == "2":
        else_example()
    elif choice == "3":
        finally_example()
    elif choice == "4":
        specific_exception()
    elif choice == "5":
        multiple_exceptions()
    elif choice == "6":
        raise_example()
    elif choice == "7":
        custom_exception_class()
    elif choice == "0":
        print("\nExiting program. Goodbye!")
       
    else:
        print("\nInvalid choice, please select a valid option.")
