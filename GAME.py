import random

print("WELCOME")
print("WANNA TEST YOUR GAMING SKILLS? TRY OUR GAME!")

while True:
    print("\n1. Start Game")
    print("2. Quit Game")

    start = input("Enter your choice: ").strip().lower()

    if start == "1" or start == "yes":
        break
    elif start == "2" or start == "no":
        print("No problem, come back when you are free to play!")
        quit()
    else:
        print("Invalid input! Please enter 1 or 2.")

while True:
    print("\nChoose Difficulty:\n1. Easy\n2. Normal\n3. Hard\n4. Insane\n5. Extreme")

    difficulty = input("Enter your difficulty choice: ").strip()

    if difficulty == "1":
        limit = 100
        chances = 10
    elif difficulty == "2":
        limit = 1000
        chances = 15
    elif difficulty == "3":
        limit = 5000
        chances = 20
    elif difficulty == "4":
        limit = 10000
        chances = 25
    elif difficulty == "5":
        limit = 100000
        chances = 35
    else:
        print("Invalid difficulty! Please try again.")
        continue

    number = random.randint(1, limit)
    count = 0
    won = False

    print(f"\nChoose a number between 1-{limit}")

    while count < chances:
        print("Chances Remaining:", chances - count)

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        count += 1

        if guess < 1 or guess > limit:
            print(f"Choose a number between 1-{limit}")
        elif guess < number:
            print("A little Higher!")
        elif guess > number:
            print("A little Lower!")
        else:
            print("Congrats! You Made It!")
            print("Attempts used:", count)
            won = True
            break

    if not won:
        print("\nGame Over!")
        print("The correct number was:", number)

    while True:
        again = input("\nWill You Play Again? (yes/no): ").strip().lower()

        if again == "yes" or again == "1":
            break
        elif again == "no" or again == "2":
            print("Thank You for Trying Our Game!")
            quit()
        else:
            print("Invalid input! Please enter yes or no.")