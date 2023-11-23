def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.2808

def feet_to_meters(feet):
    return feet / 3.2808

def kilograms_to_pounds(kilograms):
    return kilograms * 2.204

def pounds_to_kilograms(pounds):
    return pounds / 2.204

def display_menu():
    print("\n=== Unit Converter Menu ===")
    print("1. Temperature Converter")
    print("2. Length Converter")
    print("3. Weight Converter")
    print("Q. Quit")

def temperature_converter():
    print("\n=== Temperature Converter ===")
    print("Options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter option number (or 'q' to go back): ").lower()

    if choice == 'q':
        return None, None

    value = get_float_input("Enter the temperature value: ")

    if choice == '1':
        return celsius_to_fahrenheit, value, 'Celsius', 'Fahrenheit'
    elif choice == '2':
        return fahrenheit_to_celsius, value, 'Fahrenheit', 'Celsius'
    else:
        print("Invalid option. Please enter a valid option number.")
        return None, None

def length_converter():
    print("\n=== Length Converter ===")
    print("Options:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")

    choice = input("Enter option number (or 'q' to go back): ").lower()

    if choice == 'q':
        return None, None

    value = get_float_input("Enter the length value: ")

    if choice == '1':
        return meters_to_feet, value, 'Meters', 'Feet'
    elif choice == '2':
        return feet_to_meters, value, 'Feet', 'Meters'
    else:
        print("Invalid option. Please enter a valid option number.")
        return None, None

def weight_converter():
    print("\n=== Weight Converter ===")
    print("Options:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")

    choice = input("Enter option number (or 'q' to go back): ").lower()

    if choice == 'q':
        return None, None

    value = get_float_input("Enter the weight value: ")

    if choice == '1':
        return kilograms_to_pounds, value, 'Kilograms', 'Pounds'
    elif choice == '2':
        return pounds_to_kilograms, value, 'Pounds', 'Kilograms'
    else:
        print("Invalid option. Please enter a valid option number.")
        return None, None

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").lower()

        if choice == 'q':
            break
        elif choice == '1':
            conversion_function, value, source_unit, target_unit = temperature_converter()
        elif choice == '2':
            conversion_function, value, source_unit, target_unit = length_converter()
        elif choice == '3':
            conversion_function, value, source_unit, target_unit = weight_converter()
        else:
            print("Invalid option. Please enter a valid option number.")
            continue

        if conversion_function is not None:
            result = conversion_function(value)
            print(f"{value} {source_unit} is equal to {result:.2f} {target_unit}.")

if __name__ == "__main__":
    main()
