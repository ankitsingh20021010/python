import random

# Random number generate karega (1 se 100 ke beech)
secret_number = random.randint(1, 100)

print("🎮 Welcome to Number Guess Game!")
print("Guess a number between 1 and 100")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("📉 Too Low!")
    elif guess > secret_number:
        print("📈 Too High!")
    else:
        print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
        break
