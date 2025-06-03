import random

PROMPT = "What do you want? "
JOKE_1 = """Here is a joke for you!
Panaversity GPT - Sophia is heading out to the grocery store.
A programmer tells her: get a liter of milk, and if they have eggs, get 12.
Sophia returns with 13 liters of milk.
The programmer asks why and Sophia replies: 'because they had eggs'"""

JOKE_2 = """Here's another joke!
Why do Python programmers wear glasses?
Because they can't C!"""

SORRY = "Sorry I only tell jokes"

def main():
    user_input = input(PROMPT)

    if user_input.lower() == "joke":  # accepts "joke" or "Joke" (case-insensitive)
        print(random.choice([JOKE_1, JOKE_2]))  # randomly choose a joke
    else:
        print(SORRY)

if __name__ == '__main__':
    main()
