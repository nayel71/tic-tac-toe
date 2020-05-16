#!/usr/bin/env python

import tkinter as tk
import os

class TicTacToe:
    X = "x"
    O = "o"
    BLANK = " "
    WINNING_POSITIONS = ((0, 1, 2), # first row
                         (3, 4, 5), # second row
                         (6, 7, 8), # third row
                         (0, 3, 6), # first column
                         (1, 4, 7), # second column
                         (2, 5, 8), # third column
                         (0, 4, 8), # left diagonal
                         (2, 4, 6)) # right diagonal


    def __init__(self):
        self.buttons = []
        self.first_player_turn = True

        self.board = []
        for i in range(9):
            self.board.append(TicTacToe.BLANK)

        self.window = tk.Tk()
        self.window.title("Tic Tac Toe!")
        self.window.resizable(False, False)
        self.attach_buttons()


    def add_button(self, row_frame, label):
        pos = len(self.buttons)
        self.buttons.append(
            tk.Button(row_frame, text=label,
                      width=2,
                      bg="navy", fg="white", bd=8,
                      font="Helvetica 56 bold",
                      command=lambda: self.click(pos)
            )
        )
        self.buttons[pos].pack(side="left")


    def attach_buttons(self):
        for i, label in enumerate(self.board):
            if i % 3 == 0:
                row_frame = tk.Frame(self.window)
                row_frame.pack(side="top")

            self.add_button(row_frame, label)

        self.buttons.append(
            tk.Button(self.window,
                      text="Restart",
                      bg="red", fg="white", bd=8,
                      font="Helvetica 22 bold",
                      command=lambda: self.restart()
            ).pack(fill=tk.X, side="bottom")
        )


    def start(self):
        self.window.mainloop()


    def click(self, pos):
        if self.board[pos] == TicTacToe.BLANK and not self.end():
            if self.first_player_turn:
                self.board[pos] = TicTacToe.X
            else:
                self.board[pos] = TicTacToe.O

            self.buttons[pos].config(text=self.board[pos], relief=tk.SUNKEN)
            self.first_player_turn = not self.first_player_turn

            if not self.end():
                os.system("afplay -t 0.05s click.mp3")
            else:
                os.system("afplay -t 0.05s win.mp3")


    def end(self):
        for pos in TicTacToe.WINNING_POSITIONS:
            if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] != TicTacToe.BLANK:
                for i in pos:
                    self.buttons[i].config(bg="orange")

                return True


    def restart(self):
        self.window.destroy()
        self.__init__()


if __name__ == "__main__":
    game = TicTacToe()
    game.start()
