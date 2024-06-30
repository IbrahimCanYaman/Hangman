import random

word ={"American Football": "Sport","Basketball": "Sport","Soccer": "Sport","Ford": "Car Brand","Tennis": "Sport",
             "Mercedes": "Car Brand","BMW": "Car Brand","Jaguar": "Car Brand","Baseball": "Sport"}
print("Welcome Hangman Let's start!")
print("And try to don't kill the man")
print("When you guessed ture word write end of game the word and you will get result")

def choose_random_word(word_list):
    word, category = random.choice(list(word_list.items()))
    return word.lower(), category

def word_status(secret_word, guesses):
    status = ""
    for letter in secret_word:
        if letter in guesses:
            status += letter
        else:
            status += "_"
    return status

def play_hangman():
    secret_word, category = choose_random_word(word)
    allowed_mistake = 7
    guesses = []
    done = False

    print(f"The question: {category}")

    while not done:
        status = word_status(secret_word, guesses)
        print(" ".join(status))

        guess = input(f"Allowed mistakes {allowed_mistake}, Go ahead: ").lower()
        if guess in guesses:
            print("You already guessed this .")
            continue

        guesses.append(guess)

        if guess not in secret_word:
            allowed_mistake -= 1
            print(f"Wrong guess! Remaining attempts: {allowed_mistake}")
            if allowed_mistake == 0:
                break

        done = "_" not in status

    if done:
        print(f"Bravo! You got the word: {secret_word}")
    else:
        print(f"I'm sorry. The word was: {secret_word}")

    print(f"Your total score: {len(secret_word) - allowed_mistake}")

    play_again = input("Do you want to try again? (Yes/No): ").lower()
    if play_again == 'yes':
        play_hangman()
    else:
        print("Bye")

play_hangman()
