'''
update guess the number game: beta 0.2a from beta 0.2
added gui to guess the number beta 0.2
update guess the number game: beta 0.2a-1 from beta 0.2a
simplified hints into a function  
'''

import tkinter as tk
from tkinter import messagebox
import random

def give_hint(diff):
        if diff <= 5:
           hint = "Hint: Really Warm, range within 5 numbers"
        elif diff >= 10:
            hint = "Hint: Cold, range over 10 numbers"
        else:
            hint = "Hint: A Bit Warm, range within 10 numbers"
        return hint

class GuessTheNumberGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")
        self.difficulty = None
        self.number_to_guess = None
        self.attempts = 0
        self.max_attempts = 10

        self.setup_difficulty_screen()

    def setup_difficulty_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Select Difficulty Level:").pack(pady=10)

        tk.Button(self.root, text="Easy - Show Hints", command=lambda: self.start_game(1)).pack(pady=5)
        tk.Button(self.root, text="Normal - No Hints", command=lambda: self.start_game(2)).pack(pady=5)
        tk.Button(self.root, text="Hard - 10 Guesses Only", command=lambda: self.start_game(3)).pack(pady=5)

    def start_game(self, difficulty):
        self.difficulty = difficulty
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.clear_screen()

        tk.Label(self.root, text="Guess a number between 1 and 100:").pack(pady=10)
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.feedback = tk.Label(self.root, text="")
        self.feedback.pack(pady=10)

    


    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < 1 or guess > 100:
                self.feedback.config(text="Please guess a number between 1 and 100.")
                return

            self.attempts += 1

            if self.difficulty == 3 and self.attempts >= self.max_attempts:
                messagebox.showinfo("Game Over", f"Sorry! You've used all {self.max_attempts} attempts.\nThe number was {self.number_to_guess}.")
                self.setup_difficulty_screen()
                return

            if guess < self.number_to_guess:
                hint = ""
                if self.difficulty == 1:
                    diff = self.number_to_guess - guess
                self.feedback.config(text=f"{give_hint(diff):}\nToo low! Try again.")
            elif guess > self.number_to_guess:
                hint = ""
                if self.difficulty == 1:
                    diff = guess - self.number_to_guess
                self.feedback.config(text=f"{give_hint(diff):}\nToo high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!")
                self.setup_difficulty_screen()
        except ValueError:
            self.feedback.config(text="Invalid input. Please enter a number.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGUI(root)
    root.mainloop()