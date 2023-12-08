import random

words = ["UMBRELLA", "COMPUTER", "PYTHON"]
word = random.choice(words)
total_chances = 7
guessed_word = "-" * len(word)

while total_chances != 0:
    print(guessed_word)
    letter = input("Guess a letter: ").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index + 1:]
        print(guessed_word)
        if guessed_word == word:
            print("Congrats you win")
            break
        else:
            total_chances -= 1
            print("Incorrect guess")
            print("the remaining chances are:", total_chances)
    else:
        print("Game over")
        print("you lose")
        print("all the chances are exhausted")
        print("the correct word is", word)
        break  # exit the loop when the game is over

            
