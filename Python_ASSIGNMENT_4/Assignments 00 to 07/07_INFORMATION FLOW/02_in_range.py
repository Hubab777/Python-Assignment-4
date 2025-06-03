def print_ones_digit(num):
    ones_digit = abs(num) % 10  # abs() ka use kiya gaya hai taake negative numbers bhi sahi kaam karein
    print("The ones digit is", ones_digit)

def main():
    number = int(input("Enter a number: "))
    print_ones_digit(number)


if __name__ == '__main__':
    main()
