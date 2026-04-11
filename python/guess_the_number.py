import tkinter as tk
from tkinter import messagebox
import random
import ctypes
import os

root = tk.Tk()
root.title("Guess The Number")
root.resizable(False, False)
root.config(bg="#EDEDBD")

try:
    if os.name == "nt":
        GCL_STYLE = -26
        CS_DROPSHADOW = 0x00020000
        hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
        style = ctypes.windll.user32.GetClassLongPtrW(hwnd, GCL_STYLE)
        ctypes.windll.user32.SetClassLongPtrW(hwnd, GCL_STYLE, style | CS_DROPSHADOW)
except:
    pass

W, H = 420, 320
sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
x = int((sw - W) / 2)
y = int((sh - H) / 2)
root.geometry(f"{W}x{H}+{x}+{y}")

rand_num = random.randint(1, 100)
turns_left = 5
guess_list = []

def update_previous_guesses():
    if guess_list:
        prev_guess_label.config(text="Previous guesses: " + ", ".join(map(str, guess_list)))
    else:
        prev_guess_label.config(text="Previous guesses: None")

def check_guess():
    global turns_left

    if turns_left <= 0:
        return

    value = entry.get().strip()

    if value == "":
        messagebox.showwarning("Input Error", "Please enter a number.")
        return

    try:
        user_input = int(value)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer.")
        entry.delete(0, tk.END)
        return

    if user_input < 1 or user_input > 100:
        messagebox.showwarning("Range Error", "Please enter a number between 1 and 100.")
        entry.delete(0, tk.END)
        return

    if user_input == rand_num:
        hint_label.config(text="Correct guess!", fg="green")
        messagebox.showinfo("You Win", f"You guessed it right!\nThe number was {rand_num}.")
        submit_button.config(state="disabled")
        return

    guess_list.append(user_input)
    update_previous_guesses()

    turns_left -= 1
    turns_label.config(text=f"Remaining turns: {turns_left}")

    if user_input < rand_num:
        hint_label.config(text="Too low!", fg="orange")
    else:
        hint_label.config(text="Too high!", fg="orange")

    if turns_left == 0:
        hint_label.config(text="Game Over!", fg="red")
        messagebox.showinfo("Game Over", f"No turns left!\nThe right number was {rand_num}.")
        submit_button.config(state="disabled")

    entry.delete(0, tk.END)

def reset_game():
    global rand_num, turns_left, guess_list
    rand_num = random.randint(1, 100)
    turns_left = 5
    guess_list = []

    turns_label.config(text=f"Remaining turns: {turns_left}")
    hint_label.config(text="", fg="black")
    update_previous_guesses()
    entry.delete(0, tk.END)
    submit_button.config(state="normal")

title_label = tk.Label( root, text="Guess the Number", font=("Segoe UI", 22, "bold"), fg="#333333", bg="#EDEDBD")
title_label.place(x=75, y=25)

instruction_label = tk.Label( root, text="Enter a number between 1 and 100", font=("Arial", 11), fg="#555555", bg="#EDEDBD")
instruction_label.place(x=105, y=65)

entry = tk.Entry( root, width=25, font=("Arial", 14), bg="white", relief="solid", bd=2, justify="center")
entry.place(x=85, y=100)

hint_label = tk.Label( root, text="", font=("Arial", 12, "bold"), fg="black", bg="#EDEDBD")
hint_label.place(x=160, y=135)

prev_guess_label = tk.Label( root, text="Previous guesses: None", font=("Arial", 11), fg="#007BFF", bg="#EDEDBD", wraplength=350, justify="left")
prev_guess_label.place(x=30, y=165)

turns_label = tk.Label( root, text=f"Remaining turns: {turns_left}", font=("Arial", 13, "bold"), fg="#007BFF", bg="#EDEDBD")
turns_label.place(x=125, y=210)

submit_button = tk.Button( root, text="Submit", font=("Arial", 13, "bold"), width=10, bg="#00E5FF", fg="white", activebackground="#00C4DD", command=check_guess)
submit_button.place(x=55, y=255)

reset_button = tk.Button( root, text="New Game", font=("Arial", 13, "bold"), width=10, bg="#E1E1E1", fg="#333333", activebackground="#CCCCCC", command=reset_game)
reset_button.place(x=235, y=255)

root.mainloop()
