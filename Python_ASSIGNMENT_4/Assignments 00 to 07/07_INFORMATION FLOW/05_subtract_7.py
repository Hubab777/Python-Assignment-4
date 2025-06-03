def subtract_seven(num):
    return num - 7

def main():
    number = int(input("Enter a number: "))
    result = subtract_seven(number)
    print("Result after subtracting 7:", result)

# This line calls main() when the script is run
if __name__ == '__main__':
    main()
