from random import randint

name = input('Hello what is your name? ')
print(f'Well, {name}, I am thinking of a number between 1 and 20.')

secret_number = randint(1, 20)
lives = 5


while lives > 0:

    try:
        guess = int(input('Take a guess. '))

        if guess < secret_number:
            print('Your guess is too low.')
        elif guess > secret_number:
            print('Your guess is too high.')
        else:
            print(f'Good job, {name}! You guessed my number in {secret_number} guesses!')
            break

        if guess != secret_number:
            lives -=1
            print(f'You have {lives} left.')
        
        if lives == 0:
            print(f'Nope the number I was thinking of was {secret_number}')
            
        

    except ValueError:
        print('You did not enter a number')
