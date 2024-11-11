import tkinter as tk
import random

# Set up the main window
root = tk.Tk()
root.title("Guess the Number Game")

# Generate a random number
random_number = random.randint(1, 100)
attempts = 0  # Track number of attempts

# Function to check the user's guess
def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        if guess < 1 or guess > 100:
            result.set("Please enter a number between 1 and 100.")
        else:
            attempts += 1
            if guess < random_number:
                result.set("Too low! Try again.")
            elif guess > random_number:
                result.set("Too high! Try again.")
            else:
                result.set(f"Congratulations! You've guessed the number in {attempts} attempts!")
                check_button.config(state="disabled")  # Disable button when guessed correctly
                restart_button.pack()  # Show restart button
    except ValueError:
        result.set("Please enter a valid number.")

# Function to restart the game
def restart_game():
    global random_number, attempts
    random_number = random.randint(1, 100)
    attempts = 0
    result.set("Game restarted! Guess a new number.")
    entry.delete(0, tk.END)  # Clear the input field
    check_button.config(state="normal")  # Re-enable check button
    restart_button.pack_forget()  # Hide restart button

# GUI Elements
tk.Label(root, text="Guess a number between 1 and 100:").pack()
entry = tk.Entry(root)
entry.pack()
check_button = tk.Button(root, text="Check Guess", command=check_guess)
check_button.pack()

# Display results
result = tk.StringVar()
tk.Label(root, textvariable=result).pack()
result.set("Start guessing!")

# Add a restart button, initially hidden
restart_button = tk.Button(root, text="Restart Game", command=restart_game)

root.mainloop()
