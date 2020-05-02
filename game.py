import random

action_computer_list = ["rock", "paper", "scissors"]
action_win = {
    "rock": ["paper"],
    "paper": ["scissors"],
    "scissors": ["rock"]
}
try:
    with open("rating.txt", "r") as f:
        st = f.read()
        if st == "":
            raiting = {}
        else:
            raiting = {i[0]: int(i[1]) for i in [i.split(' ') for i in st.split('\n')]}
except FileNotFoundError:
    open("rating.txt", "w").close()
    raiting = {}

name = input("Enter your name: ")
print(f"Hello, {name}")
if name not in raiting:
    raiting[name] = 0

new_action = input()
if new_action:
    action_computer_list = new_action.split(",")
    action_win = {action_computer_list[i]: [] for i in range(len(action_computer_list))}
    for i in range(len(action_computer_list)):
        action = action_computer_list[i + 1:] + action_computer_list[:i]
        action_win[action_computer_list[i]] = action[:len(action)//2]

print("Okay, let's start")

while True:
    action_man = input()
    action_computer = random.choice(action_computer_list)
    if action_man == "!exit":
        exit("Bye!")
    elif action_man == "!rating":
        print(f'Your rating: {raiting[name]}')
    elif action_man not in action_computer_list:
        print("Invalid input")
    elif action_man == action_computer:
        print(f'There is a draw ({action_computer})')
        raiting[name] += 50
    elif action_computer in action_win[action_man]:
        print(f'Sorry, but computer chose {action_computer}')
        raiting[name] += 0
    else:
        print(f'Well done. Computer chose {action_computer} and failed')
        raiting[name] += 100
