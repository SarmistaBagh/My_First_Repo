
#What do you choose? Type 0 for Roch. 1 for Paper or 2 for Scissors.
import random
user_choice = input("What do you choose? Type 0 for Roch. 1 for Paper or 2 for Scissors.?")

computer_choice = random.randint(0,2)

print(f'Computer choice {computer_choice}')

if user_choice == 0 or computer_choice == 2:
    print("You win")
    
elif computer_choice == 0 or user_choice == 2:
    print("You lose")
elif computer_choice > computer_choice:
    print("You Win!")

elif computer_choice == user_choice:
    print("It's a draw")
else:
    print("You typed an invalid number, you lose!")

    
