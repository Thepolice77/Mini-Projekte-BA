import tkinter as tk
import random

class HangmanGame:
    def __init__(self):
        self.words = ["Meer","Tisch","Oktopus","Katze","Leopard","Gepard","See","Basisausbildung",""]
        self.word = ""
        self.guesses = set()
        self.max_attempts = 7
        self.attempts = 0

    def new_game(self):
        self.word = random.choice(self.words)
        self.guesses = set()
        self.attempts = 0

    def check_letter(self, letter):
        letter = letter.lower()
        if letter not in self.guesses:
            self.guesses.add(letter)
            if letter not in self.word.lower():
                self.attempts += 1
            return True
        return False

    def is_won(self):
        return all(letter.lower() in self.guesses for letter in self.word)

    def is_lost(self):
        return self.attempts >= self.max_attempts

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")

        self.game = HangmanGame()
        self.game.new_game()

        self.label = tk.Label(root, text="Welcome to Hangman!", font=("Helvetica", 16))
        self.label.pack()

        self.word_display = tk.Label(root, text="", font=("Helvetica", 24))
        self.word_display.pack()

        self.input_letter = tk.Entry(root, font=("Helvetica", 16))
        self.input_letter.pack()

        self.guess_button = tk.Button(root, text="Guess", font=("Helvetica", 16), command=self.make_guess)
        self.guess_button.pack()

        self.restart_button = tk.Button(root, text="New Game", font=("Helvetica", 16), command=self.new_game)
        self.restart_button.pack()

        self.canvas = tk.Canvas(root, width=200, height=250)
        self.canvas.pack()

        self.gallows = [
            '''
              +---+
              |   |
                  |
                  |
                  |
                  |
            =======''',
            '''
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =======''',
            '''
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =======''',
            '''
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =======''',
            '''
              +---+
              |   |
              O   |
             /|\\  |
                  |
                  |
            =======''',
            '''
              +---+
              |   |
              O   |
             /|\\  |
             /    |
                  |
            =======''',
            '''
              +---+
              |   |
              O   |
             /|\\  |
             / \\  |
                  |
            ======='''
        ]

        self.update_display()

    def make_guess(self):
        letter = self.input_letter.get()
        if len(letter) == 1 and letter.isalpha():
            if self.game.check_letter(letter):
                if self.game.is_won():
                    self.label.config(text="You won! The word was: " + self.game.word)
                elif self.game.is_lost():
                    self.label.config(text="You lost! The word was: " + self.game.word)
                else:
                    self.update_display()
            else:
                self.label.config(text="You already guessed that letter.")
        else:
            self.label.config(text="Please enter a single letter.")

    def new_game(self):
        self.game.new_game()
        self.update_display()
        self.label.config(text="New game started!")
        
    def update_display(self):
        displayed_word = ""
        for letter in self.game.word:
            if letter.lower() in self.game.guesses:
                displayed_word += letter
            else:
                displayed_word += "_ "
                
        if self.game.is_won():
            displayed_word = displayed_word.rstrip()  

        self.word_display.config(text=displayed_word)
        self.input_letter.delete(0, "end")
        self.canvas.delete("all")
        self.canvas.create_text(100, 150, text=self.gallows[self.game.attempts], anchor="s")




if __name__ == "__main__":
    root = tk.Tk()
    hangman_gui = HangmanGUI(root)
    root.mainloop()