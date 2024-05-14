import random

word_list = ["apple"]
secret_word = random.choice(word_list)

print("You have 5 chances to guess the 5-letter word. Good luck!\n")
print("--------------------------------")

# Function for checking if guessed word is 5-lettered or not
def guess_checker(guessed):
    if len(guessed) != 5:
        print("Not enough letters, Please try again")
        print("----*----*----*----*----*")
    else:
        print(guessed)

# Main line of code
guesses = 0
while guesses < 5:
    correct_letters = 0
    guessed_word = input("Please enter your guess: ").lower()  # Convert input to lowercase
   
    guess_checker(guessed_word)
   
    if guessed_word == secret_word and len(guessed_word) == 5:
        guesses += 1
        print("Valid guess number", guesses)
        print("Correct!")
        break
    elif len(guessed_word) == 5 and secret_word != guessed_word:
        print("Incorrect, try again")
        for i in range(min(len(secret_word), len(guessed_word))):
            if secret_word[i] == guessed_word[i]:
                # If the letters at the current position match, increment the correct_letters
                print("Correct letter @ position", i+1)
                correct_letters += 1
       
        print(correct_letters, "letter(s) is/are in the correct position.\n")
       
        guesses += 1  # Move this line inside the loop but after the condition
        print("Valid guess number", guesses)
        print("--------------------------------")

print("GAME OVER")
print("Correct word was:", secret_word)