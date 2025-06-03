import random

NUM_ROUNDS = 5

def main():
    print("🎮 Welcome to the High-Low Game!")
    print('--------------------------------')
    print(f"You will play {NUM_ROUNDS} rounds. Try to guess if your number is higher or lower than the computer's!")
    print()

    your_score = 0
    computer_score = 0  # To help declare a winner later

    for i in range(NUM_ROUNDS):
        print(f"🔁 Round {i + 1} of {NUM_ROUNDS}")
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print("👉 Your number is:", your_num)

        choice = input("Do you think your number is higher or lower than the computer's?: ").lower()

        while choice != "higher" and choice != "lower":
            choice = input("❗ Please enter either 'higher' or 'lower': ").lower()

        higher_and_correct = choice == "higher" and your_num > computer_num
        lower_and_correct = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print(f"✅ Correct! The computer's number was {computer_num}.")
            your_score += 1
        else:
            print(f"❌ Incorrect. The computer's number was {computer_num}.")
            computer_score += 1

        print(f"📊 Current Score — You: {your_score} | Computer: {computer_score}")
        print("-" * 40)

    print("\n🏁 Game Over!")
    print(f"Your final score is: {your_score}/{NUM_ROUNDS}")
    print(f"Computer's score: {computer_score}/{NUM_ROUNDS}")

    # Ending messages based on score
    if your_score == NUM_ROUNDS:
        print("🎉 Wow! You played perfectly!")
    elif your_score > NUM_ROUNDS // 2:
        print("👏 Good job, you played really well!")
    else:
        print("🙁 Better luck next time!")

    # Declare the winner
    print()
    if your_score > computer_score:
        print("🏆 You win the game! Congrats!")
    elif your_score < computer_score:
        print("🤖 The computer wins this time!")
    else:
        print("🤝 It's a tie!")

if __name__ == "__main__":
    main()
