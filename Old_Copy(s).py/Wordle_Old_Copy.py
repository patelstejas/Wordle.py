import random

print('You have 6 tries to guess the 5 lettered word. No copyrght infringement intended. All credits go to the original creators of Wordle.')

print('')

dictionary = ['apple', 'blade', 'clock', 'chess', 'guess', 'abiza', 'mango', 'grain', 'grill', 'south', 'world', 'brake', 'break', 'frost', 'while', 'chain', 'blood', 'acute', 'meant', 'magic', 'cream', 'charm', 'creep', 'death', 'black', 'claim', 'lives', 'aroma', 'where', 'click', 'piece', 'brail', 'enter']
selected_word = random.choice(dictionary)
print(selected_word)

while True:
  ask_user = input('MAKE A GUESS: ').lower()
  if ask_user.isnumeric == True:
    print('Please input only a word with 5 letters!')
  if len(ask_user) != 5:
    print('Please input a word with 5 letters. No more, no less.')

  if ask_user == selected_word:
    print('No way, you got it on your first try!')
    break

  for a in range(5):
    if selected_word[a].__contains__(ask_user[a]):
      print(ask_user[a] + ' is correct')
  for b in range(5):
    if ask_user[b].find(selected_word[b]) and ask_user[b] != selected_word[b]:
        print(ask_user[b] + ' is not in correct pos')

  if ask_user != selected_word:
    print('Incorrect')

  ask_user_2 = input('MAKE A GUESS: ').lower()
  if ask_user_2.isnumeric == True:
    print('Please input only a word with 5 letters!')
  if len(ask_user_2) != 5:
    print('Please input a word with 5 letters. No more, no less.')

  if ask_user_2 == selected_word:
    print('Correct!')
    print("Second attempt ain't too bad either.")
    break

  for c in range(5):
    if selected_word[c].__contains__(ask_user_2[c]):
      print(ask_user_2[c] + ' is correct')
  for d in range(5):
    if ask_user_2[d].find(selected_word[d]) and ask_user_2[d] != selected_word[d]:
        print(ask_user_2[d] + ' is not in correct pos')

  if ask_user_2 != selected_word:
    print('Incorrect')

  ask_user_3 = input('MAKE A GUESS: ').lower()
  if ask_user_3.isnumeric == True:
    print('Please input only a word with 5 letters!')
  if len(ask_user_3) != 5:
    print('Please input a word with 5 letters. No more, no less.')

  if ask_user_3 == selected_word:
    print('Third times the charm.')
    break

  for e in range(5):
    if selected_word[e].__contains__(ask_user_3[e]):
      print(ask_user_3[e] + ' is correct.')
  for f in range(5):
    if ask_user_3[f].find(selected_word[f]) and ask_user_3[f] != selected_word[f]:
        print(ask_user_3[f] + ' is not in correct pos.')

  if ask_user_3 != selected_word:
    print('Incorrect')

  ask_user_4 = input('MAKE A GUESS: ').lower()
  if ask_user_4.isnumeric == True:
    print('Please input only a word with 5 letters!')
  if len(ask_user_4) != 5:
    print('Please input a word with 5 letters. No more, no less.')

  if ask_user_4 == selected_word:
    print("Correct!")
    break

  for g in range(5):
    if selected_word[g].__contains__(ask_user_4[g]):
      print(ask_user_4[g] + ' is correct')
  for h in range(5):
    if ask_user_4[h].find(selected_word[h]) and ask_user_4[h] != selected_word[h]:
        print(ask_user_4[h] + ' is not in correct pos')

  if ask_user_4 != selected_word:
    print('Incorrect')

  ask_user_5 = input('MAKE A GUESS: ').lower()
  if ask_user_5.isnumeric == True:
    print('Please input only a word with 5 letters!')
  if len(ask_user_5) != 5:
    print('Please input a word with 5 letters. No more, no less.')

  if ask_user_5 == selected_word:
    print("Correct!")
    break

  for i in range(5):
    if selected_word[i].__contains__(ask_user_5[i]):
      print(ask_user_5[i] + ' is correct')
  for i in range(5):
    if ask_user_5[i].find(selected_word[i]) and ask_user_5[i] != selected_word[i]:
        print(ask_user_5[i] + ' is not in correct pos')

  if ask_user_5 != selected_word:
    print('Incorrect')

  ask_user_6 = input('MAKE A GUESS: ').lower()
  if ask_user_6.isnumeric == True:
    print('Please input only a word with 5 letters!')
    break
  if len(ask_user_6) != 5:
    print('Please input a word with 5 letters. No more, no less.')
    break

  if ask_user_6 == selected_word:
    print("Nice clutch!")
    break

  if ask_user_6 != selected_word:
    print('Incorrect. Better luck next time.')
    print('The word was ' + selected_word)
    break
