
import random

words = ["BRAINSTORM", "FRIENDSHIP", "EUCALYPTUS", "PSYCHOLOGY", "PLAYGROUND"]

word = random.choice(words)

total_chances = 10
guessed_word = "-" * len(word)

print("🎮 Welcome to the Word Guessing Game! 🎯")
print("Guess the word, one letter at a time. You have 10 chances! 🔠❤️\n")

while total_chances != 0:
    print(f"\n📝 Word: {guessed_word}")

    letter = input("🔡 Guess a letter: ").upper()
    
    if letter in word:
        print("✅ Correct guess! 🎉")
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index + 1:]
    else:
        total_chances -= 1
        print("❌ Wrong guess! 😢")
        print(f"🔁 Chances left: {total_chances} 💔")

    if guessed_word == word:
        print(f"\n🎊 Congratulations! You guessed it right: {word} 🎊")
        break

if guessed_word != word:
    print("\n💀 Game Over!")
    print("😞 You lost the game!")
    print("❗ All your chances have been exhausted.")
    print(f"🕵️ The correct word was: {word}")

