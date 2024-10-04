import random
print("Sveicināti spēlē 'Karātavas'!")

words_categories = {
    "Programmēšanas valodas" : ["python", "ruby", "javascript", "php", "pascal"],
    "Galda spēles" : ["cirks", "mahjong", "pokers", "bingo", "domino", "šahs", "dambrete"],
    "Valstis" : ["latvija", "vācija", "japāna", "amerika", "itālija", "zviedrija", "turcija"],
    }
categories = input("Izvēlies tēmu (Programmēšanas valodas), (Galda spēles), (Valstis): ")
chosen_list = words_categories[categories]

hangman = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
      +---+
      |   |
      o   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  | 
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  |
     / \  |
          |
    =========
    """
]

max_index = len(chosen_list) - 1 # saraksta garums
random_index = random.randint(0, max_index)
random_word = chosen_list[random_index] # 0 1 2 3


fails = 0
guessed_letters = [' ']

while fails < 6:

    word = "" 
    for char in random_word: 
        if char in guessed_letters: 
            word += char 
        else:
            word += "-" 

    
    print(hangman[fails])
    print("Minētie burti:", guessed_letters)
    print(word.capitalize())

    if word == random_word:
        print ("Tu vinnēji!")
        break

    letter = input("Ieraksti burtu: ").lower()
    guessed_letters.append(letter)

    if letter in random_word:
        print("Burts ir vārdā!")
    else:
        print("Burts nav vārdā!")
        fails += 1

if fails == 6:
    print(hangman[6])
    print("Tu zaudēji!")
