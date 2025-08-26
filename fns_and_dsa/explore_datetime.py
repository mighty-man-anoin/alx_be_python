from datetime import datetime, timedelta

time_date = datetime.now()

current_date = time_date.date()

def display_current_datetime():    
    print(f"Current date and time: {time_date.strftime("%Y-%m-%d %H:%M:%S")}")

display_current_datetime()

no_of_days = int(input("Enter the number of days to add to the current date:"))

future_date = current_date + timedelta(days=no_of_days)

def calculate_future_date():    
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

calculate_future_date()
