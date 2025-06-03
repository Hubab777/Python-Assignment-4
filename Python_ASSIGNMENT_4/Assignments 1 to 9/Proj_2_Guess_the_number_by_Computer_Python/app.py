import random

def play_game():
    print("\n ✨Welcome to the Number Guessing Game.✨ \n")
    print("\n 💻 Computer Will Guess the Number. \n")

    low = 1
    high = 15
    tries = 0  # To count the number of attempts the computer makes
    max_tries = 3  # Maximum attempts for the computer to guess

    print("🤔 Think of a number between 1 and 15, and 💻 will try to guess it!")
    
    while tries < max_tries:
        tries += 1
        guess = random.randint(low, high)
        print(f"🤖 Try {tries}: Is your number {guess}?")

        feedback = input(" 👉 Enter 'h' to indicate the guess is too high, 'l' to indicate the guess is too low, or 'c' to indicate I guessed correctly: ").lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"🎉 🎉🎉🎉🎉 Yay! 💻 guessed {guess} correctly in {tries} tries. 🎉 🎉🎉🎉🎉")
            break
        else:
            print("⚠️ Invalid input. Please enter only 'h', 'l', or 'c'. 🚫")
        
        # If the computer exceeds 3 tries and hasn't guessed correctly, ask the user for their number
        if tries == max_tries:
            print("😅 Oops! I couldn't guess your number in 3 tries.")
            user_number = int(input("Please tell me your number: "))
            print(f"Okay! Your number is {user_number}. Thanks for playing!")
            break

def main():
    while True:
        play_game()
        play_again = input("🎮 Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("👋 Thanks for playing! See you next time. ✨")
            break

if __name__ == "__main__":
    main()


