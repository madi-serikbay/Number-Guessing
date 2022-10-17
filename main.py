#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from replit import clear
import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
  """This function sets the difficulty of the game. If 'easy', 5 turns. If 'hard', 10 turns"""
  choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if choice == "easy":
    return EASY_LEVEL_TURNS
  elif choice == "hard":
    return HARD_LEVEL_TURNS


def check_number(guess, number, turns):
  """This function checks if the guessed number is correct or not"""
  if guess > number:
    print("Too high")
    return turns - 1
  elif guess < number:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it! The answer was {number}.")


def game():
  clear()
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  number = random.randint(1, 100)
  print(f"Pssst, the correct answer is {number}")
  turns = set_difficulty()
  guess = 0
  while guess != number:
    print(f"You have {turns} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_number(guess, number, turns)
    if turns == 0:
      print("You've run out of guesses")
      return
    if guess != number:
      print("Guess again.")

  
game()
  