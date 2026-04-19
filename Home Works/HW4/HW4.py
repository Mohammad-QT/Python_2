import random

def welcome():
    print("# WELCOME TO RPS GAME #")

def get_menu_choice():
    while True:
        choice = input("1. Play Rock-Paper-Scissors\n2. Cash out\nEnter a choice [1-2]: ")
        if choice == '1' or choice == '2':
            return choice
        print("Invalid choice. Please enter 1 or 2.\n")

def get_move():
    valid_moves = ['rock', 'paper', 'scissors']
    while True:
        move = input("Enter your move [Rock, Paper, Scissors]: ")
        
        move = move.lower() 
        if move in valid_moves:
            
            if move == 'rock':
                return 'Rock'
            elif move == 'paper':
                return 'Paper'
            else:
                return 'Scissors'
        print("Invalid move. Please choose Rock, Paper, or Scissors.\n")

def get_bet(chips_now):
    while True:
        bet_input = input(f"Enter the number of chips to bet [1-{chips_now}]: ")
        
        if bet_input.isdigit(): 
            bet = int(bet_input)
            if bet >= 1 and bet <= chips_now:
                return bet
            else:
                print(f"Invalid bet. Please enter an amount between 1 and {chips_now}.\n")
        else:
            print("Invalid input. Please enter numbers only.\n")

def determine_winner(user, computer):
    
    user = user.lower()
    computer = computer.lower()
    
    if user == computer:
        return "tie"
    elif user == 'rock' and computer == 'scissors':
        return "win"
    elif user == 'scissors' and computer == 'paper':
        return "win"
    elif user == 'paper' and computer == 'rock':
        return "win"
    else:
        return "lose"

def report(chips_now):
    starting_chips = 100
    difference = chips_now - starting_chips
    
    print("\n--- Final Report ---")
    if difference > 0:
        print(f"You cashed out with {chips_now} chips. You made a profit of {difference} chips!")
    elif difference < 0:
        
        lost = difference * -1 
        print(f"You cashed out with {chips_now} chips. You lost {lost} chips.")
    else:
        print(f"You cashed out with {chips_now} chips. You broke even.")

def main():
    welcome()
    chips = 100
    
    while chips > 0:
        print(f"\nYou have {chips} chips")
        choice = get_menu_choice()
        
        if choice == '2':
            break
            
        user_move = get_move()
        bet_amount = get_bet(chips)
        
        options = ['Rock', 'Paper', 'Scissors']
        random_index = random.randint(0, 2)
        computer_move = options[random_index]
        
        print(f"Computer chose: {computer_move}")
        
        result = determine_winner(user_move, computer_move)
        
        if result == "win":
            print("Congrats, you won!")
            chips = chips + bet_amount
        elif result == "lose":
            print("Sorry, you lost this round.")
            chips = chips - bet_amount
        else:
            print("It's a tie! No chips lost or won.")
            
    if chips == 0:
        print("\nYou are out of chips! Game over.")
        
    report(chips)

main()