class Player:
    def __init__(self, name=None):
        self.name = name
        self.choice = None
        self.score = 0

    def __repr__(self):
        return self.name

    def set_choice(self, choice):
        self.choice = choice

    def get_choice(self):
        return self.choice

    def increment_score(self):
        self.score += 1


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

        # Format here is to give the play and the plays that it will defeat

        self.plays_and_rules = {
            'rock': ['scissors'],
            'paper': ['rock'],
            'scissors': ['paper'],
            'gun': ['scissors', 'paper', 'rock'],
            'andrew': []
        }

        self.has_winner = False
        self.winning_player = None
        self.timer_on = False
        self.timer_completed = False

    def start_timer(self):
        self.timer_on = True

    def stop_timer(self):
        self.timer_on = False

    def decide_winner(self):

        if self.player1.choice and self.player2.choice:

            if self.player2.choice in self.plays_and_rules[self.player1.choice]:
                self.has_winner = True
                self.winning_player = self.player1
                self.player1.increment_score()

            elif self.player1.choice in self.plays_and_rules[self.player2.choice]:
                self.has_winner = True
                self.winning_player = self.player2
                self.player2.increment_score()

            else:
                self.has_winner = False

        else:
            raise Exception('No choices to compare!')

    def get_result(self):
        return self.has_winner, self.winning_player


class ShellApp:
    def __init__(self):
        annabel = Player('Annabel')
        bob = Player('Bob')

        my_game = Game(annabel, bob)

        while True:
            annabel.set_choice(input('Annabel choice: '))
            bob.set_choice(input('Bob choice: '))

            my_game.decide_winner()

            if my_game.has_winner:
                print(f'The winner was {my_game.winning_player}')
                break
            else:
                print(f'There was a draw. Play again.')


if __name__ == '__main__':
    ShellApp()


