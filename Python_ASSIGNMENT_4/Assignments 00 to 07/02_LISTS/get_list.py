def main():
    lst = []  # Make an empty list to store things in

    print("Keep entering values to add to the list.")
    print("Type 'stop' when you're done.\n")

    while True:
        val = input("Enter a value: ")
        if val.lower() == "stop":  # Check if user typed 'stop'
            break  # Exit the loop
        lst.append(val)  # Add the value to the list

    print("\nHere's the list:", lst)

if __name__ == '__main__':
    main()
