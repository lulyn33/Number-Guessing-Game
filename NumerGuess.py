import random

while True:
    top_of_range = input('Type a number range: ')
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range == top_of_range and top_of_range != 0:
            print('You are ready to go ')
            break
        else:
            print('Please type a number above 0')

    else:
        print('Please type a number')

random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')

    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess <= 0:
            print('Please type a number larger than 0 ')
            continue

    if user_guess == random_number:
        print('You got it~!')
        break

    elif user_guess > random_number:
        print('You are above the number! ')
    else:
        print('You are below the number! ')

print('You got it in',guesses,'guesses')
