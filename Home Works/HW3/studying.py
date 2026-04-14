import numpy as np

want_to_roll = input("Do you want to roll the dice? (y/n): ").lower()
total_rounds = 0
round_won = 0
round_lost = 0

while want_to_roll == 'y':
        
    d1 = np.random.randint(1,4)
    d2 = np.random.randint(1,4)
    d3 = np.random.randint(1,4)
    d4 = np.random.randint(1,4)

    print (f"\nPlayer\n{d1} {d2} {d3} {d4}")
    if d1 == d2 == d3 == d4:
        print("Congratulations! You rolled a quadruple!")
        round_won += 1
    elif d1 == d2 == d3 or d1 == d2 == d4 or d1 == d3 == d4 or d2 == d3 == d4:
        print("Congratulations! You rolled a triple!")
        round_won += 1
    elif (d1 == d2 and d3 == d4) or (d1 == d3 and d2 == d4) or (d1 == d4 and d2 == d3):
        print("Congratulations! You rolled two pairs!")
        round_won += 1
    elif (d1 == 4 and d2 == 4) or (d1 == 4 and d3 == 4) or (d1 == 4 and d4 == 4) or (d2 == 4 and d3 == 4) or (d2 == 4 and d4 == 4) or (d3 == 4 and d4 == 4):
        print("Congratulations! You rolled a high pair of 4's!")
        round_won += 1
    else:
        print("Sorry, you lost!")
        round_lost += 1

    total_rounds += 1
    want_to_roll = input("Do you want to roll again? (y/n): ").lower()

print("\nComputer Dice Results")
print(f"Total rounds played: {total_rounds}")
print(f"Rounds won: {round_won}")
print(f"Rounds lost: {round_lost}")
