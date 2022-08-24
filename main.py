import random
from termcolor import colored
dictionary = ['apple', 'mango', 'berry', 'fruit', 'blade', 'guess', 'chess', 'clear', 'loath', 'cheat', 'world', 'hades', 'false', 'house', 'acute', 'angle', 'manly', 'brain', 'lucky', 'craft', 'which', 'white', 'black', 'cease', 'exist', 'mortal', 'tango', 'rapid', 'blitz', 'flash', 'error', 'grade', 'vital', 'doubt', 'laugh', 'smile', 'sight', 'widow', 'hello', 'below', 'ocean', 'shark', 'snark', 'fight', 'never', 'audio', 'beach', 'being', 'abyss', 'adapt', 'movie', 'bloat', 'great', 'flame', 'belly', 'ghost', 'thing', 'today', 'media', 'lotus', 'check', 'candy', 'viral', 'pasta', 'blimp', 'bling', 'woven', 'legit', 'fiend', 'staff']
attempts = 0
hint = 0
while True:
  ask_user = input('Play Wordle? y/n: ').lower()
  if ask_user == 'y':
    selected_word = random.choice(dictionary)
    #print(selected_word)
    #Instructions
    print('You have 6 tries to guess the 5 lettered word. Press H to get a 1 time hint. It will not count towards your attempt.')
    #Core
    while attempts < 7:
      guess = input('MAKE A GUESS: ').lower()
      if guess == selected_word:
        print(colored(guess, 'green'))
        print('Correct!')
        attempts += 1
        print('You got it in ' + str(attempts) + ' attempt(s)')
        hint = 0
        break
      if guess != selected_word and guess != 'h':
        print('Incorrect.')
        attempts += 1
      if attempts == 6:
        print('The word was: ' + selected_word)
        print('Better luck next time!')
        attempts = 0
        hint = 0
        break
      #Green, Yellow, and White positions
      for i in range(min(len(guess), 5)):
        if guess[i] == selected_word[i]:
            print(colored(guess[i], 'green'), end=' ')
        elif guess[i] in selected_word:
            print(colored(guess[i], 'yellow'), end=' ')
        else:
            print(colored(guess[i], 'white'), end=' ')
      #Hint feature
      if guess == 'h':
        if hint == 0:
          hint = 1
          print('The first letter is:', selected_word[0])
      if hint == 1:
        print('It seems you have already used your 1 hint')
      print('\n')
  if ask_user == 'n':
    print('Come back any time!')
    break