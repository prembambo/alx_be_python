<<<<<<< HEAD
# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # Return current date for use in other functions

def calculate_future_date(current_date):
    """
    Calculates and displays the future date after adding user-specified days.
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days_to_add)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    # Step 1: Display current date and time
    now = display_current_datetime()

    # Step 2: Calculate future date
    calculate_future_date(now)
=======
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer number.")
        return
    
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
>>>>>>> 51fd4f43afa216daa1ea0c26568cb6c06a7cbfc6
