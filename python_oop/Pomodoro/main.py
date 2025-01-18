#
#  ! Created as part of BAIL repository on 01/17
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Initializing the window and setting basic info
window = tk.Tk()
window.title("Pomodoro Counter")
photo = tk.PhotoImage(file="./tomato.png")
canvas = tk.Canvas(width=200, height=224)
canvas.create_image(100, 112, image=photo)
canvas.pack()

window.mainloop()
