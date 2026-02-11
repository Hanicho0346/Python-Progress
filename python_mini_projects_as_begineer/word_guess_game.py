# number guess game
import random

playing=True
guess=random.randint(1,100)
while playing:
    user_input=int(input("Guess the number between 1 and 100: "))
    if not isinstance(user_input,int):
        print("Please enter a valid number")
    if user_input>guess:
        print("Too High")
    if user_input<guess:
        print("Too low")        
    if user_input==guess:
        print(f"you guess is correct it is {guess}")






