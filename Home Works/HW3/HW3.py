import random

# print("Welcome to Computer Dice")
# print("You will first roll your dice")
# print("Next the outcome of your roll will be determined:")
# print("any Quad and you Win")
# print("any Triple and you Win")
# print("any Two Pair and you Win")
# print("any High Pair (4's) and you Win")
# print("anything else and you Lose")

# print("Welcome to Computer Dice\n" \
# "You will first roll your dice\n" \
# "Next the outcome of your roll will be determined:\n" \
# "any Quad and you Win\nany Triple and you Win\n" \
# "any Two Pair and you Win\n" \
# "any High Pair (4's) and you Win\n" \
# "anything else and you Lose")

print("""Welcome to Computer Dice
You will first roll your dice
Next the outcome of your roll will be determined:
any Quad and you Win
any Triple and you Win
any Two Pair and you Win
any High Pair (4's) and you Win
anything else and you Lose""")

total_rounds = 0
rounds_won = 0
rounds_lost = 0

play = 'y'

play = input("\nDo you wish to play [y, n]: ").lower()

while play == 'y':
    
    d1 = random.randint(1, 4)
    d2 = random.randint(1, 4)
    d3 = random.randint(1, 4)
    d4 = random.randint(1, 4)
    
    dice = [d1, d2, d3, d4]
    
    print("\nPlayer")
    print(f"{d1} {d2} {d3} {d4}")
    
    counts = [dice.count(1), dice.count(2), dice.count(3), dice.count(4)]
    
    if 4 in counts:
        print("Quad, you win!")
        rounds_won += 1
    elif 3 in counts:
        print("Triple, you win!")
        rounds_won += 1
    elif counts.count(2) == 2:
        print("Two Pair, you win!")
        rounds_won += 1
    elif dice.count(4) == 2:
        print("High Pair, you win!")
        rounds_won += 1
    else:
        print("Sorry, you lose!")
        rounds_lost += 1
        
    total_rounds += 1
    
    while True:
        play = input("Do you wish to play again [y, n]: ").lower()
        if play in ['y', 'n']:
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

print("\nComputer Dice Results")
print(f"You played {total_rounds} rounds")
print(f"Rounds won: {rounds_won}")
print(f"Rounds lost: {rounds_lost}")