# Countdown Timer - Python Project by Anam

import time

def countdown_timer():
    print("Welcome to the Countdown Timer ⏳")
    total_seconds = int(input("Enter the time in seconds: "))

    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print("Time left:", timer, end="\r")  # Overwrites the line
        time.sleep(1)
        total_seconds -= 1

    print("\n⏰ Time's up!")

# Run the timer
countdown_timer()
