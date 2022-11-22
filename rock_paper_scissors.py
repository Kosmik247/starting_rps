class Player:
    def __init__(self, name=None):
        self.name = name
        self.choice = None
    def make_a_choice(self, choice):
        self.choice = choice


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.options_and_how_to_win = {
            'rock' : 'scissors',
            'paper' : 'rock',
            'scissors' : 'paper'
        }
        self.winner = None
        self.timer = None
        self.score = 0

    def update_score(self):
        pass

    def decide_winner(self):
        if self.player1.choice and self.player2.choice:
            if self.options_and_how_to_win[self.player1.choice] == self.player2.choice:
                self.winner = self.player1
            elif self.options_and_how_to_win[self.player2.choice] == self.player1.choice:
                self.winner = self.player2
            else:
                self.winner = None
        else:
            raise Exception('No choices to compare!')

    def start_timer(self):
        pass


class ShellApp:
    def __init__(self):
        annabel = Player('Annabel')
        bob = Player('Bob')

        my_game = Game(annabel, bob)

        while True:
            annabel.make_a_choice(input('Annabel choice:'))
            bob.make_a_choice(input('Bob choice:'))

            my_game.decide_winner()

            if my_game.winner:
                print(f'The winner was {my_game.winner.name}')
                break
            else:
                print(f'There was a draw. Play again.')

if __name__ == '__main__':
    ShellApp()


