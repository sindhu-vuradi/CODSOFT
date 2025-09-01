import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    player = input("Choose rock, paper, or scissors: ").lower()
    
    if player not in ['rock', 'paper', 'scissors']:
        print("Invalid choice!")
        return
    
    computer = get_computer_choice()
    print(f"Computer chose: {computer}")
    result = determine_winner(player, computer)
    print(result)

while True:
    play_game()
    again = input("Play again? (yes/no): ").lower()
    if again != 'yes':
        break
