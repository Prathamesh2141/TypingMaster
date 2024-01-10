from time import time
import random as r
from colorama import Fore, Style  # Import necessary modules from colorama

leaderboard = []

def mistake(paratest, usertest):
    error = 0
    min_len = min(len(paratest), len(usertest))
    
    for i in range(min_len):
        if paratest[i] != usertest[i]:
            error += 1

    error += abs(len(paratest) - len(usertest))
    
    return error

def typing_metrics(time_start, time_end, user_input):
    # Calculate time delay
    time_delay = time_end - time_start
    time_taken = round(time_delay, 2)

    # Calculate words typed
    words_typed = len(user_input.split())

    # Calculate words per minute (WPM)
    words_per_minute = round((words_typed / time_taken) * 60, 2)

    return {
        "Words Typed": words_typed,
        "Time Taken (s)": time_taken,
        "Words Per Minute (WPM)": words_per_minute
    }

def typing_test():
    test = [
        "Hello I am Prathamesh Magar. I am from Parbhani, Maharashtra.",
        "Before you start your conversation, make sure you really know what you are going to talk about.",
        "Also, see to it that the person or people you are talking to is interested in what you are discussing."
    ]
    
    test_sentence = r.choice(test)

    print(Fore.GREEN + "***** Typing Master *****" + Style.RESET_ALL)
    print(test_sentence)
    print()

    time_start = time()
    user_input = input("Enter: ")
    time_end = time()

    metrics = typing_metrics(time_start, time_end, user_input)
    error = mistake(test_sentence, user_input)

    print(Fore.CYAN + "Words Typed:" + Style.RESET_ALL, metrics["Words Typed"])
    print(Fore.CYAN + "Time Taken:" + Style.RESET_ALL, metrics["Time Taken (s)"], "seconds")
    print(Fore.CYAN + "Words Per Minute (WPM):" + Style.RESET_ALL, metrics["Words Per Minute (WPM)"])
    print(Fore.RED + "Error:" + Style.RESET_ALL, error)

    username = input("Enter your username for the leaderboard: ")
    leaderboard.append({"Username": username, "Speed": metrics["Words Per Minute (WPM)"], "Error": error})

def show_leaderboard():
    print(Fore.YELLOW + "***** Leaderboard *****" + Style.RESET_ALL)
    if not leaderboard:
        print("Leaderboard is empty.")
    else:
        sorted_leaderboard = sorted(leaderboard, key=lambda x: x["Speed"], reverse=True)
        for idx, entry in enumerate(sorted_leaderboard, start=1):
            print(f"{idx}. {entry['Username']} - Speed: {entry['Speed']} WPM, Error: {entry['Error']}")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Start Typing Test")
    print("2. Show Leaderboard")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        typing_test()
    elif choice == "2":
        show_leaderboard()
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print(Fore.RED + "Invalid choice. Please enter 1, 2, or 3." + Style.RESET_ALL)
