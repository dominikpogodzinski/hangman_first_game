# -*- coding: utf-8 -*-
from random import randint


def new_game():
    words = ('python', 'programmer', 'hangman', 'game')
    drawn_word = words[randint(0, len(words) - 1)]
    searches_word = ['_' for i in drawn_word]
    letter_drawn_word = [drawn_letter for drawn_letter in drawn_word]
    prize = ('You Loose with nothing...', 'One houndred', 'Two houndret', 'One thousend')
    safe = f'You win {prize} dollars'
    chances = 9
    lists = []
    while True:

        def show_searched_word():
            print(' '.join(searches_word))
            print('')

        def moore_playing():
            ans = input('Maybe, do you want play one moore time?, y/n''    ')
            if ans == "y":
                new_game()
            else:
                print('Than :/, see you later...')
            exit()

        def hazard():
            question = input('If you decide to play enter p, if you stop playing and draw safe enter e.'
                             ' Your decision is p/e')
            if question == 'p':
                pass
            if question == 'e':
                prize = randint(0, len(safe) - 1)
                print(prize)
                exit()

        show_searched_word()
        print(f"You have {chances} chances")
        letter = input("Now, give me some letter: ")

        if letter == drawn_word:
            print('Huraaaaaaaaa!!!!!')
            print(f'You find right word: {drawn_word}')
            moore_playing()

        if letter in lists:
            print("This letter was used :P")

        if letter in drawn_word:
            chances += 1

        if letter in letter_drawn_word:
            tstart = 0
            for i in range(0, letter_drawn_word.count(letter)):
                index = letter_drawn_word.index(letter, tstart)
                searches_word[index] = letter
                tstart = index + 1
                lists.append(letter)
                print(lists)
                hazard()

            if '_' not in searches_word:
                print('Huraaaaaaaaa!!!!!')
                print(f'You find right word: {drawn_word}')
                moore_playing()

        if letter not in searches_word:
            lists.append(letter)
            print(lists)

        chances -= 1

        if chances == 0:
            print('You are losser :P')
            print(f'Searching word is:  {letter_drawn_word}')
            moore_playing()


new_game()
