from random import choice
from time import sleep

def start_game():
    options = {'R': 'ROCK', 'P': 'PAPER', 'S': 'SCISSOR'}

    computer = choice(list(options.keys()))
    user = input("Enter 'R' for ROCK, 'P' for PAPER, 'S' for SCISSOR: ").upper().strip()

    sleep(1)
    if user == computer:
        return f"\n{options[user]} against {options[computer]}: TIES !!!"
    
    if user_win(user, computer):
        return f"\n{options[user]} against {options[computer]}: USER WON!!!"
    
    return f"\n{options[user]} against {options[computer]}: USER LOST :[ !!!"


def user_win(user, computer):
    if user == 'R' and computer == 'S' or user == 'P' and computer == 'R' or user == 'S' and computer == 'P':
        return True
    else:
        return False


if __name__ == "__main__":
    result = start_game()
    print(result)