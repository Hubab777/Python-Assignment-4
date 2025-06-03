import random

def play_game():
    print("\n ✨ Welcome to the Number Guessing Game.✨ \n")
    print("\n 💻 Computer Will Think of the Number, and 👨 You Will Guess It! \n")

    # Computer selects a random number between 1 and 15
    computer_number = random.randint(1, 15)
    tries = 0  # To count the number of attempts the user makes
    max_tries = 3  # Maximum attempts for the user to guess

    print("🤔 The computer has selected a number between 1 and 15. Now, you try to guess it!\n")
    
    while tries < max_tries:
        tries += 1
        user_guess = int(input(f"🧐 Try {tries}: What is your guess? Enter a number between 1 and 15: \n"))
        
        if user_guess < computer_number:
            print("🔻 Your guess is too low. Try again!")
        elif user_guess > computer_number:
            print("🔺 Your guess is too high. Try again!")
        elif user_guess == computer_number:
            print(f"🎉 🎉🎉 Congratulations! You guessed the number {computer_number} correctly in {tries} tries. 🎉 🎉🎉")
            break
        else:
            print("⚠️ Invalid input. Please enter a valid number between 1 and 15. 🚫")

        # If the user exceeds 3 tries and hasn't guessed correctly, reveal the number
        if tries == max_tries:
            print(f"\n😅 Oops! You couldn't guess the number in {max_tries} tries.\n")
            print(f"The correct number was {computer_number}. Thanks for playing! 👏\n")

def main():
    while True:
        play_game()
        play_again = input("🎮 Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("👋 Thanks for playing! See you next time. ✨")
            break

if __name__ == "__main__":
    main()
