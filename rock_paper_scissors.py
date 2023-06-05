import random

i_computer_choice = 0
i_user_choice = 0

for i in range(3):
    x = random.randint(1,3)

    if x == 1:
        computer_choice = "rock"
    elif x == 2:
        computer_choice = "paper"
    elif x == 3:
        computer_choice = "scissors"

    print("rock or paper or scissors")
    user_choice = input()

    print("💻",computer_choice)
    print("💂‍♂️",user_choice)

    if i_computer_choice == "rock" and i_user_choice == "paper":
        i_user_choice = i_user_choice + 1
    elif i_computer_choice == "paper" and i_user_choice == "rock":
        i_computer_choice = i_computer_choice + 1
    elif i_computer_choice == "scissors" and i_user_choice == "rock":
        i_user_choice = i_user_choice + 1
    elif i_computer_choice == "rock" and i_user_choice == "scissors":
        i_computer_choice = i_computer_choice + 1
    elif i_computer_choice == "scissors" and i_user_choice == "paper":
        i_computer_choice = i_computer_choice + 1
    elif i_computer_choice == "paper" and i_user_choice == "scissors":
        i_user_choice = i_user_choice + 1
    elif i_computer_choice == "rock" and i_user_choice == "rock":
        print("mosavi")
    elif i_computer_choice == "scissors" and i_user_choice == "scissors":
        print("mosavi")
    elif i_computer_choice == "paper" and i_user_choice == "paper":
        print("mosavi")

print(i_user_choice,i_computer_choice)

if i_user_choice > i_computer_choice:
    print(i_user_choice,"to baranse shodi, merci ke az bazi man estefade kardi")
elif i_computer_choice > i_user_choice:
    print("camputer barane shod, merci ke az bazi man estefade kardi")    
elif i_computer_choice == i_user_choice:
    print("mosavi shodin, merci ke az bazi man estefade kardi")    


