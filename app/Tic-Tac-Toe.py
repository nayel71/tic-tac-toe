#!/usr/bin/env python

import tkinter as tk
import os

class TicTacToe:
    def __init__(self):
        self.x = "x"
        self.o = "o"
        self.blank = " "

        self.board = []
        self.board_size = 9
        for i in range(self.board_size):
                self.board.append(self.blank)

        self.buttons = []
        self.move_count = 0
        self.game_end = False

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
        if self.game_end:
            return

        if self.board[pos] == self.blank:
            self.move_count += 1

            if self.move_count % 2 == 1:
                self.board[pos] = self.x
            else:
                self.board[pos] = self.o

        self.buttons[pos].config(text=self.board[pos])
        self.end()


    def end(self):
        winning_positions = [[0, 1, 2], # first row
                             [3, 4, 5], # second row
                             [6, 7, 8], # third row
                             [0, 3, 6], # first column
                             [1, 4, 7], # second column
                             [2, 5, 8], # third column
                             [0, 4, 8], # left diagonal
                             [2, 4, 6]] # right diagonal

        for pos in winning_positions:
            if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] != self.blank:
                self.game_end = True

                for i in pos:
                    self.buttons[i].config(bg="orange")

        if not self.game_end: 
            os.system("afplay -t 0.05s click.mp3")
            if self.move_count == self.board_size:
                self.game_end = True
        else:
            os.system("afplay -t 0.05s win.mp3")


    def restart(self):
        self.window.destroy()
        self.__init__()


if __name__ == "__main__":
    game = TicTacToe()
    game.start()
