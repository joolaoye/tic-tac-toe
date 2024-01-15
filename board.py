import tkinter as tk
import random as rd


class Board:
    def __init__(self):
        self.page = tk.Tk()
        self.page.geometry("155x165")
        self.button = [[None, None, None], [None, None, None], [None, None, None]]
        self.players = ["x", "o"]
        self.current = self.players[0]
        for i in range(3):
            for j in range(3):
                self.button[i][j] = tk.Button(text=" ", width=6, height =3, command=lambda row=i, column=j: self.click(row, column))
                self.button[i][j].grid(row=i, column=j, sticky=tk.N+tk.S+tk.E+tk.W)
        self.page.mainloop()


    def click(self, row, column):
        self.button[row][column].config(text=self.current, state="disabled")
        if self.current == self.players[0]:
            self.current = self.players[1]
            available_buttons = [button for row in self.button for button in row if button.cget("state") != "disabled"]
            if available_buttons:
                random_button = rd.choice(available_buttons)
                if not self.check_win():
                    random_button.invoke()
        else:
            self.current = self.players[0]

        if self.check_win():
             self.disable_all_buttons()
        if self.check_draw():
           for i in range(3):
            for j in range(3):
                self.button[i][j].config(bg="red")



    def check_win(self):
        for i in range(3):
            if self.button[i][0].cget("text") == self.button[i][1].cget("text") == self.button[i][2].cget("text") != " ":
                self.button[i][0].config(bg="green")
                self.button[i][1].config(bg="green")
                self.button[i][2].config(bg="green")
                return True

        for j in range(3):
            if self.button[0][j].cget("text") == self.button[1][j].cget("text") == self.button[2][j].cget("text") != " ":
                self.button[0][j].config(bg="green")
                self.button[1][j].config(bg="green")
                self.button[2][j].config(bg="green")
                return True

        if self.button[0][0].cget("text") == self.button[1][1].cget("text") == self.button[2][2].cget("text") != " ":
                self.button[0][0].config(bg="green")
                self.button[1][1].config(bg="green")
                self.button[2][2].config(bg="green")
                return True

        if self.button[0][2].cget("text") == self.button[1][1].cget("text") == self.button[2][0].cget("text") != " ":
                self.button[0][2].config(bg="green")
                self.button[1][1].config(bg="green")
                self.button[2][0].config(bg="green")
                return True


    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.button[i][j]["text"] == " ":
                    return False
        return True


    def disable_all_buttons(self):
        for i in range(3):
            for j in range(3):
                self.button[i][j].config(state="disabled")
Board()
