def main():
    """
    This program prompts the user to enter a temperature in Fahrenheit,
    converts it to Celsius using the formula:
        Celsius = (Fahrenheit - 32) * 5.0 / 9.0
    and then prints the result.
    """
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print("Temperature: " + str(fahrenheit) + "°F = " + str(celsius) + "°C")

if __name__ == '__main__':
    main()
