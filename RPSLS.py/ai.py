from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self, player):
        random_number = random.randint(0, 4)
        computer_choice = self.gestures[random_number]
        print(f'The computer chose {computer_choice} for this round!')
        return computer_choice