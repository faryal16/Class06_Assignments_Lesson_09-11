import math
import datetime
import calendar

def math_operations():
    print("\n1️⃣  Math Module Examples")
    number = float(input("\nEnter a number: "))

    print(f"\nSquare Root of {number} = {math.sqrt(number)}")
    print(f"\nCeiling of {number} = {math.ceil(number)}")
    print(f"\nFloor of {number} = {math.floor(number)}")
    print(f"\nPower of {number} = {math.pow(number, 2)}")
    print(f"\nSine of {number} = {math.sin(number)}")
    print(f"\nPi content = {math.pi}")


def datetime_operations():
    print("\n2️⃣  Datetime Module Examples")

    now = datetime.datetime.now()
    print(f"\nCurrent Date & Time: {now}")

    today = datetime.date.today()
    print(f"\nToday's Date: {today}")

    custom_date = datetime.date(2025,4,15)
    print(f"\nCustom's Date: {custom_date}")

    future_date = datetime.timedelta(days=7) + today
    print(f"\nDate after 7 days: {future_date}")

    formatted = now.strftime("%d-%m-%Y %H:%M:%S")
    print(f"\nFormatted Date & Time: {formatted}")



def calendar_operations():
    print("\n3️⃣  Calendar Module Examples")

    year = int(input("\nEnter Year: "))
    month = int(input("\nEnter month (1-12): "))

    print("\nMonth Calender:\n")
    print(calendar.month(year , month))

    print("\nFull Year Calendar:\n")
    print(calendar.calendar(year))

    if calendar.isleap(year):
        print(f"\n{year} is a leap year! ✅")
    else:
        print(f"{year} is not a leap year ❌")



if __name__ == "__main__":
   
    print("\n===== Math, Datetime, Calendar Menu =====")
    print("1. Math Module Operations")
    print("2. Datetime Module Operations")
    print("3. Calendar Module Operations")
    print("0. Exit")

    choice = input("Enter your choice (0-3): ")

    if choice == "1":
        math_operations()
    elif choice == "2":
        datetime_operations()
    elif choice == "3":
        calendar_operations()
    elif choice == "0":
        print("Exiting program. Goodbye!")
        
    else:
        print("Invalid choice! Please select a valid option.")
