def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        print(f"The price of {fruit_name} is ${price} each.")  # Showing price before asking
        amount_bought = int(input(f"How many {fruit_name}s do you want to buy?: "))
        total_cost += price * amount_bought

    print("\nYour total is $" + str(total_cost))


if __name__ == '__main__':
    main()
