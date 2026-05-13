
possible_words = ["hello", "world","he", "indespensable", "rut", "hangman","over"]
chosen_word = []
lives = 10
guessed_letters = set()
guessd_word = []

def game_over(secret_word,g_word,lives_count):
    return secret_word == g_word or lives_count == 0

def show_state(lives_count, g_letters, g_word):
    print(f"Lives: {lives_count}, Guessed letters: {g_letters}, Guessed_word_state: {g_word}")      
    return

def user_letter_choice():

    while True:
        try:
            letter = input("what is the missing letter: ").lower
            if letter.isalpha():
                return letter
            else:
                raise TypeError
        except TypeError:
            print(" it must be a letter")

def update_guessed_word(letter,guessed_w,secret_w):
    for i,char in secret_w:
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

if lives:
    print("YOU HAVE ONE!!!")
else:
    print("GAME OVER")