import random 

def initialize_chosen_w(possible_w):
    secret_w = []
    secret_w = random.choice(possible_w)
    return list(secret_w)

def initialize_guessed_w(secret_w,g_word):
    for _ in secret_w:
        g_word.append("_")
    return

def game_over(secret_word,g_word,lives_count):
    return secret_word == g_word or lives_count == 0

def show_state(lives_count, g_letters, g_word):
    if g_letters:
        print(f"Lives: {lives_count}, Guessed letters: {g_letters }, Guessed_word_state: {g_word}") 
    else:
        print(f"Lives: {lives_count}, Guessed letters:  , Guessed_word_state: {g_word}") 

def accept_letter_choice():
    while True:
        try:
            letter = input("what is the missing letter: ")
            if letter.isalpha() and len(letter) == 1:
                return letter
            else:
                raise TypeError
        except TypeError:
            print("it must be a [single] letter")
            continue

# The function is used by "correct_guess"
def update_guessed_word(letter,guessed_w,secret_w):
    for i,char in enumerate(secret_w):
        if char == letter:
            guessed_w[i] = char
    return

def correct_guess(chosen_letter,secret_word,g_letters,g_word):
    global lives
    if chosen_letter in secret_word:
        update_guessed_word(chosen_letter,g_word,secret_word)
    else:
        lives -= 1
        g_letters.add(chosen_letter)
    return

possible_words = ["hello", "world","he", "indespensable", "rut", "hangman","over"]
chosen_word = []
lives = 10
guessed_letters = set()
guessd_word = []
letter_choice = None

def main():
    
    chosen_word = initialize_chosen_w(possible_words)
    initialize_guessed_w(chosen_word,guessd_word)
    while not game_over(chosen_word, guessd_word,lives):
        show_state(lives,guessed_letters,guessd_word)
        letter_choice = accept_letter_choice()
        correct_guess(letter_choice,chosen_word,guessed_letters,guessd_word)
    # checkes if there are any lives left: player '=' won if lives > 0 else loss
    if lives:
        print("YOU HAVE ONE!!!")
    else:
        print("GAME OVER")

if __name__=="__main__":
    main()