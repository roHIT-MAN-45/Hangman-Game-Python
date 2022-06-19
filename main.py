# Hangman Game
import random

# Ascii art will be shown on every wrong guess
stages = [
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
+---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

words = ["banana", "skateboard", "fireworks", "swordsman", "icecream", "manga", "life"]

# Printing logo of the game first
print(logo)

# Choosing random word from array
random_word = random.choice(words)

# Previewing Word for testing
print(f"Chosen word is : {random_word}")

# Created an empty array with underscores
display = []
for _ in random_word :
    display += "_"


# Creating a variable with false value to keep game running until game over
game_over = False

# Player have only 6 lives
lives = 6 

while not game_over :
    # Getting input from user
    guess_letter = input("Guess the Letter : ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know
    if guess_letter in display:
      print(f"You already guessed {guess_letter}")


    # Looping through random_word and if letter matches with guess_letter then revealing its position in display array
    # Looping on length of random_word so we can easily access positions inside display list
    for position in range(len(random_word)) : 
            letter = random_word[position]
            if letter == guess_letter :
                display[position] = letter

    # Decrementing a life when user guesses a wrong letter
    if guess_letter not in random_word :
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life")
        lives -= 1        

        # Printing Ascii art here
        print(stages[lives])

        # Quiting game when lives becomes equal to 0
        if(lives == 0) :
            game_over = True
            print("You LOSE! 💔")

    # Printing display list
    print(display)

    # Quiting loop once all blank spaces are filled
    if "_" not in display :
        game_over = True
        print("You WIN! 🎉")

    
    