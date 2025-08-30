# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9

def celsius_to_fahrenheit(celsius):
    return celsius*CELSIUS_TO_FAHRENHEIT_FACTOR+32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR

def main():
    print("Temperature Conversion Tool")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    try:
        if choice=='1':
            celsius=float(input("Enter temperature in Celsius: "))
            fahrenheit=celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit}°F")
        elif choice=='2':
            fahrenheit=float(input("Enter temperature in Fahrenheit: "))
            celsius=fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius}°C")
        else:
            print("Invali
