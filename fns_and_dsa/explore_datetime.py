from datetime import datetime, timedelta

time_date = datetime.today()

current_date = time_date.date()

def display_current_datetime():    
    print(f"Current date and time: {time_date.strftime("%Y-%m-%d %H:%M:%S")}")

display_current_datetime()

no_of_days = int(input("Enter number of days (as an integer): "))

future_date = current_date + timedelta(days=no_of_days)

def calculate_future_date():    
    print(f"Future date: {future_date}")

calculate_future_date()
