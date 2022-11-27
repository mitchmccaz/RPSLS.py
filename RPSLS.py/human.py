from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self, player):
        print('\n')
        for index in range(len(self.gestures)):
            print(f'{index} for {self.gestures[index]}')
        player_choice = input(f'\n {player} Choose your gesture ')
        while player_choice != '0' and player_choice != '1' and player_choice != '2' and player_choice != '3' and player_choice != '4':
            player_choice = input('Please enter 0-4. Choose your gesture: ')
        player_choice = int(player_choice)
        if player_choice <= 4:
            player_choice = self.gestures[player_choice]
        print(f'You chose: {player_choice} for this round!')
        return player_choice