def write_example():
    print("\n1️⃣  Writing to a File")
    file = open("example.txt", "w")
    file.write("Hello! This is the first line.\n")
    file.write("Python makes file handling easy.\n")
    file.close()
    print("\nData written successfully.")

def read_example():
    print("\n2️⃣  Reading from a File")
    try:
          file = open("example.txt", "r")
          content = file.read()
          print("\nFile content: \n " , content)
          file.close()
    except FileNotFoundError:
         print("\nFile not Found!")


def append_example():
    print("\n3️⃣  Appending to a File")
    file = open("example.txt", "a")
    file.write("This is added using append.\n")
    file.close()
    print("\nNew data appended successfully.") 

def with_example():
    print("\n4️⃣  Using 'with' Statement")
    with open("example.txt", "r") as file:
        content = file.read()
        print("\nContent using 'with':\n", content)
     

def read_line_by_line():
     
    print("\n5️⃣  Reading Line by Line")
    with open("example.txt", "r") as file:
        for line in file:
            print("\nLine:" ,line.strip())
     
def write_list_example():
    
    print("\n6️⃣  Writing a List of Lines")
    lines = ["First Line\n" ,"Second Line\n", "Third Line\n"]
    with open("example.txt", "w") as file:
        file.writelines(lines)
    print("\nList of lines written to file.")

def file_error_handling():
    print("\n7️⃣  Handling File Not Found Error")
    try:
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("\nError: The file dose not exist")


if __name__ == "__main__":
    
    print("\n===== File Handling Menu =====")
    print("1. Write to a file")
    print("2. Read from a file")
    print("3. Append to a file")
    print("4. Use 'with' to read")
    print("5. Read line by line")
    print("6. Write list of lines")
    print("7. Handle file error")
    print("0. Exit")

    choice = input("Enter your choice (0-7): ")

    if choice == "1":
        write_example()
    elif choice == "2":
        read_example()
    elif choice == "3":
        append_example()
    elif choice == "4":
        with_example()
    elif choice == "5":
        read_line_by_line()
    elif choice == "6":
        write_list_example()
    elif choice == "7":
        file_error_handling()
    elif choice == "0":
        print("\nExiting program. Goodbye!")
        
    else:
        print("\nInvalid choice! Please enter a number from 0 to 7.")
