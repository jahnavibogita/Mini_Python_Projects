import tkinter as tk
from tkinter import messagebox

board = [' '] * 10
player = 1  # Human player is 1 (X), AI is 2 (O)
Win = 1
Draw = -1
Running = 0
Stop = 1
Game = Running

def minimax(board, depth, is_maximizing, alpha, beta):
    score = check_winner()
    if score == Win:
        return 10 - depth
    if score == -Win:
        return depth - 10
    if score == Draw:
        return 0

    if is_maximizing:
        best = -float('inf')
        for i in range(1, 10):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(board, depth + 1, False, alpha, beta))
                board[i] = ' '
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = float('inf')
        for i in range(1, 10):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(board, depth + 1, True, alpha, beta))
                board[i] = ' '
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

def ai_move():
    best_val = -float('inf')
    best_move = -1
    for i in range(1, 10):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, False, -float('inf'), float('inf'))
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                best_move = i
    board[best_move] = 'O'
    update_board()
    check_game_over()

def check_winner():
    winning_positions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != ' ':
            return Win if board[pos[0]] == 'X' else -Win
    if ' ' not in board[1:]:
        return Draw
    return Running

def click(pos):
    global player
    if board[pos] == ' ' and Game == Running:
        board[pos] = 'X'
        update_board()
        if check_game_over():
            return
        ai_move()

def update_board():
    for i in range(1, 10):
        buttons[i].config(text=board[i])

def check_game_over():
    global Game
    result = check_winner()
    if result == Win:
        messagebox.showinfo("Tic-Tac-Toe", "You won! Congratulations!")
        reset_board()
        return True
    elif result == -Win:
        messagebox.showinfo("Tic-Tac-Toe", "AI won! Better luck next time!")
        reset_board()
        return True
    elif result == Draw:
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        reset_board()
        return True
    return False
def reset_board():
    global board, player, Game
    board = [' '] * 10
    player = 1
    Game = Running
    update_board()
    player_label.config(text="Player 1's turn")
root = tk.Tk()
root.title("Tic-Tac-Toe Game")
root.configure(bg='aqua')

buttons = [None] * 10
for i in range(1, 10):
    buttons[i] = tk.Button(root, text=' ', font=('Arial', 20), height=3, width=6, borderwidth=2, relief="solid", bg='white',
                           command=lambda i=i: click(i))
    buttons[i].grid(row=(i-1)//3, column=(i-1)%3, padx=5, pady=5)

player_label = tk.Label(root, text="Player 1's turn", font=('Arial', 15), bg='aqua')
player_label.grid(row=3, column=0, columnspan=3)

reset_button = tk.Button(root, text="Reset", font=('Arial', 15), command=reset_board, bg='white', borderwidth=2, relief="solid")
reset_button.grid(row=4, column=0, columnspan=3, pady=10)

update_board()
root.mainloop()
