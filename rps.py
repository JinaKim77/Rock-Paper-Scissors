import random
import subprocess
try:
    from colorama import init, Fore, Back, Style
except Exception as e:
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import init, Fore, Back, Style

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        # To keep each object's score
        self.score = 0

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


# It asks the human user what move to make.
class HumanPlayer(Player):
    def __init__(self):
        # To keep each object's score
        self.score = 0

    def move(self):
        while True:
            choice = input("Rock, Paper, Scissors?"
                           " Or Type quit to 'quit' > ").lower()
            # Validate user input
            if choice in moves:
                return choice
            elif choice in 'quit':
                print("Bye!")
                exit()
            else:
                print("\n")
        return choice

    def learn(self, my_move, their_move):
        if my_move == their_move:
            print("** TIE **")
        elif beats(my_move, their_move) is True:
            self.score += 1
            print(f"**PLAYER ONE : {self.score} WINS **")


# A player that chooses its moves randomly..
# it should return one of 'rock', 'paper', or 'scissors' at random
class RandomPlayer(Player):
    def __init__(self):
        # To keep each object's score
        self.score = 0

    def move(self):
        choice = random.choice(moves)
        return choice

    def learn(self, my_move, their_move):

        if beats(my_move, their_move) is True:
            self.score += 1
            print(f"**PLAYER TWO : {self.score} WINS **")
        return self.score


# A player that remembers and imitates
# what the human player did in the previous round.
class ReflectPlayer(Player):
    def __init__(self):
        # To keep each object's score
        self.score = 0
        self.choice = "rock"

    def move(self):
        choice = self.choice
        return choice

    def learn(self, my_move, their_move):

        if my_move == their_move:
            print("** TIE **")
        elif beats(my_move, their_move) is True:
            self.score += 1
            print(f"**PLAYER ONE : {self.score} WINS **")

        # Remembers what move the opponent played last round,
        # and plays the exact same move next round
        # This new value should be Reflect player's next move.
        self.choice = their_move


# A player that cycles through the three moves
class CyclePlayer(Player):
    def __init__(self):
        # To keep each object's score
        self.score = 0
        self.choice = moves[0]

    def move(self):
        if self.choice == moves[0]:
            self.choice = moves[1]
        elif self.choice == moves[1]:
            self.choice = moves[2]
        elif self.choice == moves[2]:
            self.choice = moves[0]
        return self.choice

    def learn(self, my_move, their_move):
        if beats(my_move, their_move) is True:
            self.score += 1
            print(f"**PLAYER TWO : {self.score} WINS **")


# It tells whether one move beats another one.
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        # The game displays the results after each round,
        # including each player's score.
        print(f"Score: Player One {self.p1.score} Player Two {self.p2.score}")

    def display_score(self):
        print(f"Final Score ->  Player One: {self.p1.score}")
        print(f"\t\tPlayer Two: {self.p2.score}")

        if self.p1.score > self.p2.score:
            print("Player 1 WON!")
        elif self.p1.score < self.p2.score:
            print("Player 2 WON!")
        else:
            print("Both Player 1 and Player 2 got the same score!")

    def play_game(self):
        init()
        print('\033[2;31;43m  Rock Paper Scissors  \033[0;0m')
        print(Fore.RED)
        count = input('How many times do you want to play?\n')
        for round in range(int(count)):
            print(Fore.WHITE)
            print(f"\nRound {round+1}")
            self.play_round()
        print("\n")
        print('\033[2;31;43m  GAME OVER  \033[0;0m')
        print("\n"+Fore.RED)
        self.display_score()


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
