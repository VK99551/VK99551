import random

class GuessingGame:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.target_number = random.randint(lower_bound, upper_bound)
        self.attempts = 0

    def play(self):
        print(f"Welcome to the Guessing Game!")
        print(f"I'm thinking of a number between {self.lower_bound} and {self.upper_bound}. Can you guess what it is?")
        
        while True:
            try:
                guess = int(input("Enter your guess: "))
                self.attempts += 1
                if guess < self.target_number:
                    print("Too low! Try again.")
                elif guess > self.target_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number {self.target_number} in {self.attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input! Please enter an integer.")

# Instantiate and play the game
if __name__ == "__main__":
    game = GuessingGame(1, 100)
    game.play()
