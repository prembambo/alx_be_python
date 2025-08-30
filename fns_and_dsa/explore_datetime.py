# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius*CELSIUS_TO_FAHRENHEIT_FACTOR+32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR

def main():
    """Interactive temperature conversion tool."""
    print("Temperature Conversion Tool")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice=input("Enter your choice (1 or 2): ").strip()
    
    try:
        if choice=='1':
            celsius=float(input("Enter temperature in Celsius: "))
            fahrenheit=celsius_to_fahrenheit(celsius)
            print(f"{ce
