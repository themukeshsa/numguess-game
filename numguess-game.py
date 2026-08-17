import random
print('Welcome to the number guessing game!')
print('Choose a number between 1 to 50...')
 
num = random.randint(1,50)
attempts = 0

while True:
    try:
        guess = int(input('Enter your number: '))
        attempts += 1
        if guess > num:
           print("Too High!")
        elif guess < num:
           print("Too Low!")
        else:
           print("That's it!")
           print("You guessed correct number in", attempts, "attempts!")
           break
    except ValueError:
       print("Invalid input. Please enter a number.")
 