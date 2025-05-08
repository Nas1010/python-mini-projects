import random

words = ['sheila', 'eric', 'eva', 'daisy', 'inspector']

#randomly choose a word from the list

chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
print(word_display)
attempts = 8

print('Welcome to Hangman - Inspector Calls Edition!')

while attempts > 0 and '_' in word_display:
    print('\n' + ' '.join(word_display))
    guess = input('Guess the letter: ').lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word): 
            if letter == guess: 
             word_display[index] = guess
    else:
       print('That letter does not appear in the word.')
       attempts -= 1

if '_' not in word_display:
   print('You guessed the word!')
   print(' '.join(word_display))
   print('You survived!')
else:
   print('Oops, you lost. Better luck next time!')