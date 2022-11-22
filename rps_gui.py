import rock_paper_scissors as rps
import tkinter as tk
import random as r

class AppRPS(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.geometry('400x300')
        self.title('Rock, Paper, Scissors')

        self.player1_choice_frame = PlayerChoiceFrame(self, self.game.player1, self.game)
        self.status_frame = StatusFrame(self, self.game)
        self.player2_choice_frame = PlayerChoiceFrame(self, self.game.player2, self.game)

        self.player1_choice_frame.grid(row=0, column=0, sticky='news')
        self.status_frame.grid(row=0, column=1, sticky='news')
        self.player2_choice_frame.grid(row=0, column=2, sticky='news')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)


class PlayerChoiceFrame(tk.Frame):
    def __init__(self, parent, player: rps.Player, game: rps.Game):
        super().__init__(parent)
        self.parent = parent
        self.player = player
        self.game = game

        self.choice = tk.StringVar()
        self.choice.set(r.choice(list(self.game.options_and_how_to_win)))

        self.name_label = tk.Label(self, text=str(self.player))
        self.name_label.grid(sticky='new')

        self.radio_buttons = []
        for choice in self.game.options_and_how_to_win:
            next_choice = tk.Radiobutton(self, text=choice, variable=self.choice, value=choice)
            next_choice.grid(sticky='w')
            self.radio_buttons.append(next_choice)


class StatusFrame(tk.Frame):
    def __init__(self, parent, game):
        super().__init__(parent)
        self.parent = parent
        self.game = game
        self.timer_value = 0
        self.timer_display = tk.StringVar()
        self.timer_display.set('0')

        self.play_button = tk.Button(self, text='Play', command=self.play_button_pressed)
        self.game_status = tk.Label(self, text='Press Play')
        self.timer_Label = tk.Label(self, textvariable=self.timer_display)

        self.play_button.grid()
        self.game_status.grid()
        self.timer_Label.grid()

    def play_button_pressed(self):
        if not self.game.timer_on:
            self.game_status.configure(text='Game on')
            self.timer_start()
        else:
            pass

    def timer_start(self):
        self.game.start_timer()
        self.timer_display.set('1:00')


anna = rps.Player('Anna')
bob = rps.Player('Bob')

my_app = AppRPS(rps.Game(anna, bob))

tk.mainloop()
