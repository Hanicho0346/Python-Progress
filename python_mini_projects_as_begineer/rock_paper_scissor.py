
import random

playing=True
choice= ["r",'p','s']
emoji={"r":"rock","p":"paper","s":"scissors"}
while playing:
    user_input=str(input("Rock ,paper,scissors? (r/p/s): "))
    if user_input !="r" and  user_input !="p" and  user_input !="s":
        print("invalid input")
    if user_input not in choice:
        print("invalid choice") 
        continue
    computer_choice=random.choice(choice)
    print(f"your choice is {emoji[user_input]}")
    print(f"Compuuter choice is {emoji[computer_choice]}")
    if user_input==computer_choice:
        print("Tie")
    elif user_input=="r" and computer_choice=="s":
        print("you win")
    elif user_input=="s" and computer_choice=="p":
        print("you win")
    else:
        print('YOU LOSE')
    should_contue=input("Continue? y/n: ").lower()
    if should_contue=="n":
        break  
       



