def access_element(lst, index):
    try:
        return f"Element at index {index}: {lst[index]}"
    except IndexError:
        return "❌ Index out of range."


def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return f"✅ List updated: {lst}"
    except IndexError:
        return "❌ Index out of range."


def slice_list(lst, start, end):
    try:
        return f"Sliced list [{start}:{end}]: {lst[start:end]}"
    except IndexError:
        return "❌ Invalid indices."


def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("🎮 Welcome to the Index Game!")
    print("📋 Current list:", lst)
    print("🔁 You can: access, modify, slice, or exit")

    while True:
        operation = input("\n👉 Enter operation (access / modify / slice / exit): ").strip().lower()

        if operation == "exit":
            print("👋 Exiting the game. Goodbye!")
            break
        elif operation == "access":
            try:
                index = int(input("🔢 Enter index to access: "))
                print(access_element(lst, index))
            except ValueError:
                print("❌ Please enter a valid integer.")
        elif operation == "modify":
            try:
                index = int(input("🔢 Enter index to modify: "))
                new_value = int(input("✍️ Enter new integer value: "))
                print(modify_element(lst, index, new_value))
            except ValueError:
                print("❌ Invalid input. Please enter integers only.")
        elif operation == "slice":
            try:
                start = int(input("🔢 Enter start index: "))
                end = int(input("🔢 Enter end index: "))
                print(slice_list(lst, start, end))
            except ValueError:
                print("❌ Please enter valid integers.")
        else:
            print("❌ Invalid operation. Try again.")

# Run the game
index_game()
