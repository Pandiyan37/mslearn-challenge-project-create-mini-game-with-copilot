# write 'Hello World' to the console
print('Hello World')
# create a minigame of rock, paper and scissors with the user
import random

def play_game():
    user = input("Enter your choice (rock/paper/scissors): ")
    global score
    score = 0
    # if user enter invalid input warn the user
    if user not in ['rock', 'paper', 'scissors']:
        return 'Invalid input!'
    computer = random.choice(['rock', 'paper', 'scissors'])
    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
        return True
print(play_game())
# end of each round, the player can choose whether to play again.
while input("Do you want to play again? (yes/no): ") == 'yes':
    print(play_game())
# display the user score at the end of the game
print('Your score is: ', score)