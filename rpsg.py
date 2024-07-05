import tkinter as tk
import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"
def play_game(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)
    
    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=result)
    
    if result == "You win!":
        scores["user"] += 1
    elif result == "You lose!":
        scores["computer"] += 1
    
    user_score_label.config(text=f"Your score: {scores['user']}")
    computer_score_label.config(text=f"Computer's score: {scores['computer']}")
def reset_game():
    scores["user"] = 0
    scores["computer"] = 0
    user_choice_label.config(text="Your choice: ")
    computer_choice_label.config(text="Computer's choice: ")
    result_label.config(text="")
    user_score_label.config(text=f"Your score: {scores['user']}")
    computer_score_label.config(text=f"Computer's score: {scores['computer']}")
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x400")
root.config(bg="#ADD8E6") 
label_font = ("Helvetica", 12, "bold")
button_font = ("Helvetica", 12)
result_font = ("Helvetica", 14, "italic")
label_fg = "#2F4F4F"
button_bg = "#4682B4"
button_fg = "#FFFFFF"
result_fg = "#FF6347"
scores = {"user": 0, "computer": 0}
tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 16, "bold"), fg=label_fg, bg="#ADD8E6").pack(pady=10)
user_choice_label = tk.Label(root, text="Your choice: ", font=label_font, fg=label_fg, bg="#ADD8E6")
user_choice_label.pack(pady=5)
computer_choice_label = tk.Label(root, text="Computer's choice: ", font=label_font, fg=label_fg, bg="#ADD8E6")
computer_choice_label.pack(pady=5)
result_label = tk.Label(root, text="", font=result_font, fg=result_fg, bg="#ADD8E6")
result_label.pack(pady=10)
tk.Button(root, text="Rock", font=button_font, bg=button_bg, fg=button_fg, command=lambda: play_game("rock")).pack(pady=5)
tk.Button(root, text="Paper", font=button_font, bg=button_bg, fg=button_fg, command=lambda: play_game("paper")).pack(pady=5)
tk.Button(root, text="Scissors", font=button_font, bg=button_bg, fg=button_fg, command=lambda: play_game("scissors")).pack(pady=5)
user_score_label = tk.Label(root, text=f"Your score: {scores['user']}", font=label_font, fg=label_fg, bg="#ADD8E6")
user_score_label.pack(pady=5)
computer_score_label = tk.Label(root, text=f"Computer's score: {scores['computer']}", font=label_font, fg=label_fg, bg="#ADD8E6")
computer_score_label.pack(pady=5)
tk.Button(root, text="Reset Game", font=button_font, bg="#FF6347", fg=button_fg, command=reset_game).pack(pady=10)
root.mainloop()
