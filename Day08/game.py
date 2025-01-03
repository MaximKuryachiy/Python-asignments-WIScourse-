import tkinter as tk
import random
import validator
import comparisator
from tkinter import messagebox

class NumberGuesserGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guesser Game")
        self.master.geometry("400x300")
        
        self.computer_number = random.randrange(1, 20, 1)
        self.count = 0
        
        self.label = tk.Label(master, text="Welcome to number guesser game!", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.input_label = tk.Label(master, text="Enter a number (from 1 to 20):")
        self.input_label.pack(pady=5)
        
        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.check_guess_event)  # Bind Enter key to check_guess_event
        self.master.bind("<x>", self.quit_game_event)       # Bind 'x' key to quit_game_event
        self.master.bind("<n>", self.restart_game_event)    # Bind 'n' key to restart_game_event
        self.master.bind("<s>", self.show_number_event)     # Bind 's' key to show_number_event
        
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)
        
        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)
        
        self.restart_button = tk.Button(master, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=5)
        
        self.cheat_button = tk.Button(master, text="Show Number", command=self.show_number)
        self.cheat_button.pack(pady=5)
        
        self.show_instructions()

    def show_instructions(self):
        instructions = (
            "Welcome to the Number Guesser Game!\n\n"
            "Instructions:\n"
            "- Guess a number between 1 and 20.\n"
            "- Press 'Enter' key or click the 'Guess' button to submit your guess.\n\n"
            "Keybinds:\n"
            "- Enter: Submit your guess.\n"
            "- 'x': Quit the game.\n"
            "- 'n': Restart the game.\n"
            "- 's': Show the hidden number (Don't cheat!) and restart the game.\n\n"
            "Buttons:\n"
            "- Guess: Submit your guess.\n"
            "- Restart: Start a new game.\n"
            "- Show Number: Reveal the hidden number and restart the game."
        )
        self.master.withdraw()  # Hide the main window
        messagebox.showinfo("Instructions", instructions)
        self.master.deiconify()  # Show the main window again
        self.entry.focus_set()  # Set focus to the entry widget

    def check_guess_event(self, event):
        self.check_guess()

    def quit_game_event(self, event):
        self.master.quit()

    def restart_game_event(self, event):
        self.restart_game()

    def show_number_event(self, event):
        self.show_number()

    def check_guess(self):
        player_choice = self.entry.get()
        if player_choice == 'x':
            self.quit_game_event(None)
        elif player_choice == 'n':
            self.restart_game_event(None)
        elif player_choice == 's':
            self.show_number_event(None)
        else:
            validation_result = validator.convert(player_choice)
            if not validation_result:
                self.result_label.config(text="Please enter a valid number.")
                return
            self.count += 1
            if self.computer_number < validation_result:
                self.result_label.config(text="Too high! Try again.")
            elif self.computer_number > validation_result:
                self.result_label.config(text="Too low! Try again.")
            elif self.computer_number == validation_result:
                self.result_label.config(text=f"Congratulations! You guessed it right in {self.count} attempts.")
                more_suggestion = messagebox.askyesno("Play again?", "Do you want to play more?")
                if more_suggestion:
                    self.restart_game()
                else:
                    self.master.quit()

    def restart_game(self):
        self.count = 0
        self.computer_number = random.randrange(1, 20, 1)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.label.config(text="Game restarted! Guess a number between 1 and 20.")
        self.entry.focus_set()  # Set focus to the entry widget
        
    def show_number(self):
        messagebox.showinfo("Cheat", f"Don't cheat! The number was: {self.computer_number}")
        self.restart_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuesserGame(root)
    root.mainloop()
