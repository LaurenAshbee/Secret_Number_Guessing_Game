from random import randint

secret_num = randint(1,100)

print(f"Welcome to the Secret Number Guessing Game. Your goal is to correctly guess the secret number "
      f"in as few guesses as possible")
print(f"The Secret Number is from 1 to 100.")
print(f"If your number is within 10 of the Secret Number, then I will tell you WARM.\n"
      f"If your guess is more than 10 from the Secret Number, then I will tell you COLD.\n"
      f"If your guess is closer than your last guess, then I will tell you WARMER.\n"
      f"If your guess is farther than your last guess, then I will tell you COLDER.\n"
      f"If your guess is neither farther nor closer that your last guess, then I will tell you\n"
      f"NEITHER WARMER NOR COLDER.\n"
      f"Let's get started with your first guess.\n"
      f"Good luck!")

guess_list = [0]

while True:
    guess = int(input("Please enter a number:   "))

    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS. Please guess again.")
        continue

    if guess == secret_num:
        print(f"CONGRATULATIONS! you guessed the Secret Number in {len (guess_list)} guesses!")
        ans = input("Would you like to play again? Enter y for yes or n for no: ")

        if ans == "y" or ans == "Y":
            secret_num = randint(1, 100)
            continue
        else:
            break

    guess_list.append(guess)

    if len(guess_list) == 2:
        if abs(guess - secret_num) <= 10:
            print(f"WARM!")
        else:
            print(f"COLD!")

    else:
        if abs(guess - secret_num) < abs(guess_list[-2] - secret_num):
            print(f"WARMER!")
        elif abs(guess - secret_num) > abs(guess_list[-2] - secret_num):
            print(f"COLDER!")
        else:
            print(f"NEITHER WARMER NOR COLDER!")





