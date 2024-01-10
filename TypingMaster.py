from time import time
import random as r

leaderboard = []

def mistake(paratest, usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if(paratest[i] != usertest[i]):
                error += 1
        except:
            error += 1
    return error


def speed_time(time_s, time_e, userInput):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    speed = len(userInput) / time_r
    return round(speed)


def typing_test():
    test = [
        "Hello I am Prathamesh Magar. I am from Parbhani, Maharashtra.",
        "Before you start your conversation, make sure you really know what you are going to talk about.",
        "Also, see to it that the person or people you are talking to is interested in what you are discussing."
    ]
    
    test_sentence = r.choice(test)

    print("***** Typing Master *****")
    print(test_sentence)
    print()

    time_start = time()
    user_input = input("Enter: ")
    time_end = time()

    speed = speed_time(time_start, time_end, user_input)
    error = mistake(test_sentence, user_input)

    print("Speed:", speed, "w/sec")
    print("Error:", error)

    username = input("Enter your username for the leaderboard: ")
    leaderboard.append({"Username": username, "Speed": speed, "Error": error})


def show_leaderboard():
    print("***** Leaderboard *****")
    if not leaderboard:
        print("Leaderboard is empty.")
    else:
        sorted_leaderboard = sorted(leaderboard, key=lambda x: x["Speed"], reverse=True)
        for idx, entry in enumerate(sorted_leaderboard, start=1):
            print(f"{idx}. {entry['Username']} - Speed: {entry['Speed']} w/sec, Error: {entry['Error']}")


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
        print("Invalid choice. Please enter 1, 2, or 3.")
