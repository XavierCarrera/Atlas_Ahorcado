import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'eritrea',
    'micronesia',
    'liechstenstein',
    'bangladesh',
    'luxemburgo',
    'suriname',
    'guyana',
    'botswana'
]


def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- ')


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        print('''BIENVENIDA/O A AHORCADOS MUNDIAL
Tengo unos países secretos y los tienes que adivinar
            ''')
        current_letter = str(input('Escoge una letra: '))

    letter_indexes = []
    for idx in range(len(word)):
        if word[idx] == current_letter:
            letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('¡Perdiste! El país correcto era {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('¡Eso es! El país correcto es: {}'.format(word))
            break

if __name__ == '__main__':
    run()