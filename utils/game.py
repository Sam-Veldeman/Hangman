#Project Hangman
#This project will start the well known 'Hangman' game.
#Start the game with: python main.py (in ur terminal when inside the folder)
#You get 5 lives to guess the word.

#Create class hangman
import random
class Hangman:
    #declare all the attributes.
    def __init__(self):
        self.possible_words = {1:'becode',2:'learning',3:'mathematics',4:'sessions'}
        self.word_to_find = self.possible_words[random.randint(1,len(self.possible_words))].upper() #list comprehension with randomize (import)
        self.lives = 5
        self.correctly_guessed_letters = ["_" for x in self.word_to_find] #list comprehension to create list with '_' for letters in word to find
        self.wrongly_guessed_letters = []
        self.turn_count = 1
        self.error_count = 0
    #recieve input from user, restrainted to 1 letter input and check for previous use of a letter.
    def play(self,letter): #declare method
        while True: #check input untill input = ok
            letter = input(f"\nTurn {self.turn_count}:\n\n{self.lives} lives left\nLooking for: {self.correctly_guessed_letters}\n\nPlease enter your letter:").upper()
            if len(letter) != 1:
                print(f"\nPlease make sure to enter only 1 letter, please try again:")
            elif letter in self.wrongly_guessed_letters:
                print(f"\nThis letter was allready used. Please try again:")
            elif letter in self.correctly_guessed_letters:
                print(f"\nThis letter is correct, but allready used. Please try again:")
            elif letter.isalpha() == False:
                print(f"\nOnly letters allowed! Try again.")
            else:
                break
        if letter in self.word_to_find:
            for s in range(len(self.word_to_find)):
                if self.word_to_find[s] == letter:
                    self.correctly_guessed_letters[s] = letter
            self.turn_count+=1        
        else:
            self.error_count += 1
            self.turn_count += 1
            self.lives -= 1
            self.wrongly_guessed_letters.append(letter)
            print(f"\nI'm sorry, this letter is not in the word to find...")
    #start the game
    def start_game(self):
        print("Hangman game\n")
        while self.lives != 0 and "_" in self.correctly_guessed_letters:
            self.play(self)
        if self.lives == 0:
            self.game_over()
        else:
            self.well_played()
    #end the game when word is not found.
    def game_over(self):
        print(f"Game over...\nThe word to find was: {self.word_to_find}")
    #end the game when word is found.
    def well_played(self):
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")
game =Hangman()
game.start_game()