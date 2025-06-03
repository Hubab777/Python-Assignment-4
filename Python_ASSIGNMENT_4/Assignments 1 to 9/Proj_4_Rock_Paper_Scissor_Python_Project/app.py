import random 

print("🎉 Welcome to Rock, Paper & Scissor Game! 🤖 vs 🧑")

user_score = 0
comp_score = 0
ties = 0

name = input("👤 Enter Your Name Here: ")
print("""\n📜 Winning Rules: 
        📝 1. Paper 📄 beats Rock 🪨
        📝 2. Rock 🪨 beats Scissor ✂️
        📝 3. Scissor ✂️ beats Paper 📄
        """)
print()

while True:
    print("""🤔 Make Your Choice: 
        1️⃣ Rock 🪨
        2️⃣ Paper 📄
        3️⃣ Scissor ✂️
        """)
    choice = int(input("🔢 Enter your choice (1-3): "))
    print()
    
    while choice > 3 or choice < 1:
        choice = int(input("🚫 Invalid input. Please enter 1, 2 or 3: "))
        
    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissor"
        
    print(f"🧑 {name}'s choice: {user_choice}")
    print("🤖 Computer is making its move...")

    computer = random.randint(1,3)
    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissor"
        
    print(f"🤖 Computer's choice: {comp_choice}")

    # Determine winner
    if ((user_choice == "Paper" and comp_choice == 'Rock') or 
        (user_choice == "Rock" and comp_choice == "Paper")):
        print("📄 Paper Wins!")
        result = "Paper"
        
    elif ((user_choice == "Scissor" and comp_choice == 'Rock') or 
          (user_choice == "Rock" and comp_choice == "Scissor")):
        print("🪨 Rock Wins!")
        result = "Rock"
        
    elif user_choice == comp_choice:
        print("🤝 It's a Tie!")
        result = "Draw"
    else:
        print("✂️ Scissor Wins!")
        result = "Scissor"

    # Update scores
    if result == "Draw":
        ties += 1
    elif result == user_choice:
        print("🎉 You Win This Round!")
        user_score += 1
    else:
        print("💻 Computer Wins This Round!")
        comp_score += 1
        
    # Scoreboard
    print("\n📊 Current Scores:")
    print(f"🧑 {name}'s Score: {user_score}")
    print(f"🤖 Computer's Score: {comp_score}")
    print(f"🤝 Total Ties: {ties}")
    
    # Ask to play again
    
    repeat = input("\n🔁 Do you want to play again? (Yes/No): ").lower()
    if repeat in ["no", "not", "n"]:
        break
    elif repeat in ["yes", "y"]:
        print("🔄 Starting a new round...\n")
    else:
        print("🤔 Invalid input. Assuming you want to continue...")


print("\n🏁 Game Over!")
print("🙏 Thanks for playing!! See you next time 👋")
