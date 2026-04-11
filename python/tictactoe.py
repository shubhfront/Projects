import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("350x420")
root.config(bg="lightblue")
root.resizable(False, False)

current_player = "X"
board = [""] * 9
buttons = []

status_label = tk.Label(root, text="Player X's Turn", font=("Arial", 18, "bold"), bg="lightblue", fg="black")
status_label.pack(pady=10)

frame = tk.Frame(root, bg="lightblue")
frame.pack()

def check_winner():
    win_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for pos in win_positions:
        a, b, c = pos
        if board[a] == board[b] == board[c] != "":
            return board[a]

    if "" not in board:
        return "Draw"

    return None

def button_click(index):
    global current_player

    if board[index] != "":
        return

    board[index] = current_player
    buttons[index].config(text=current_player)

    result = check_winner()

    if result == "X" or result == "O":
        status_label.config(text=f"Player {result} wins!")
        messagebox.showinfo("Game Over", f"Player {result} wins!")
        disable_buttons()
    elif result == "Draw":
        status_label.config(text="It's a Draw!")
        messagebox.showinfo("Game Over", "It's a Draw!")
        disable_buttons()
    else:
        current_player = "O" if current_player == "X" else "X"
        status_label.config(text=f"Player {current_player}'s Turn")

def disable_buttons():
    for button in buttons:
        button.config(state="disabled")

def reset_game():
    global current_player, board
    current_player = "X"
    board = [""] * 9
    status_label.config(text="Player X's Turn")

    for button in buttons:
        button.config(text="", state="normal")

for i in range(9):
    button = tk.Button(frame, text="", font=("Arial", 24, "bold"), width=5, height=2, bg="white", fg="black", command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(button)

restart_button = tk.Button(root, text="Restart Game", font=("Arial", 14, "bold"), bg="white", fg="black", command=reset_game)
restart_button.pack(pady=20)

root.mainloop()
