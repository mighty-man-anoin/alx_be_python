FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return result

def convert_to_fahrenheit(celsius):
    result = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return result

valid_user_entry = False

while not valid_user_entry:
    try:
        temperature = float(input("Enter the temperature to convert: "))
        valid_user_entry = True
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
    
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == 'C':
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
elif unit == 'F':
    print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
