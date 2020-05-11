#!/usr/bin/env python

import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.buttons = []
        self.move_count = 0
        self.game_end = False

        self.create_window()
        self.attach_buttons()


    def create_window(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe!")
        self.window.geometry("200x200")
        self.window.resizable(False, False)

        self.status = tk.StringVar()
        tk.Label(self.window, textvariable=self.status, pady=10).pack()


    def add_button(self, row_frame, label):
        pos = len(self.buttons)
        self.buttons.append(
            tk.Button(row_frame, text=label, relief=tk.GROOVE, 
                      height=2, width=2, 
                      command=lambda: self.play(pos)))
        self.buttons[pos].pack(side="left")


    def attach_buttons(self):
        for i, label in enumerate(self.board):
            if i % 3 == 0:
                row_frame = tk.Frame(self.window)
                row_frame.pack(side="top")

            self.add_button(row_frame, label)


    def start(self):
        self.status.set("X's turn")
        self.window.mainloop()


    def play(self, pos):
        if self.game_end:
            return

        if self.board[pos] == " ":
            self.move_count += 1

            if self.move_count % 2 == 1:
                self.board[pos] = "X"
                self.status.set("O's turn")
            else:
                self.board[pos] = "O"
                self.status.set("X's turn")

        self.update()
        self.end()


    def update(self):
        if self.game_end:
            return

        for i, label in enumerate(self.board):
            self.buttons[i].config(text=label)


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
            if (self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] and 
                self.board[pos[0]] in ["X", "O"]):
                self.game_end = True

                for i in pos:
                    self.buttons[i].config(bg="orange")
                    self.status.set(f"{self.board[pos[0]]} wins!")

        if not self.game_end and self.move_count == len(self.board):
            self.game_end = True
            self.status.set("Draw!")


if __name__ == "__main__":
    game = TicTacToe()
    game.start()
