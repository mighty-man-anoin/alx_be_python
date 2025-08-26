from datetime import datetime, timedelta

def display_current_datetime():
    time_date = datetime.today()
    
    print(f"Current date and time: {time_date.strftime("%Y-%m-%d %H:%M:%S")}")
    return time_date.date()

current_date = display_current_datetime()

no_of_days = int(input("Enter number of days (as an integer): "))

# 
def calculate_future_date():
    new_date = current_date + timedelta(days=no_of_days)
    
    print(f"Future date: {new_date}")
    return new_date

future_date = calculate_future_date()
