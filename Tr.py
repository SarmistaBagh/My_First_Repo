#Tresure iland
'''
print("Welcome to the tresure island")
print("Your mission is to find the tresure.")
choice1=input('You\'re at a crossroad,where do you want to go? Type "left" or "right".').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake.There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3=input("You arrive at the island unharmed.There is a house with 3 door one red, one yellow and one blue.")
        if choice3 == "red":
            print("It's a room full of fire.Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts.Game Over.")
        else:
            print("You chose a door")
    else:
        print("You got attacked by an angry trout.Game Over.")

else:
    print("You fell into a hole Game Over.")
'''
#Example.DAY-4
#Randomisation and python lists.
'''
rock=input("Enter rock:")

pep=input("Enter a paper")

sci=input("Enter a scissores")

if rock==0:
    print("Rock")

elif pep ==1:
    print("paper")

elif sci == 2:
    print("Scissor")
    

else:
    print("not at all")
'''
#Example.
import random

random_integer = random.randint(1,10)

print(random_integer)

#Module.

random_float = random.random()
print(random_float)

random_float * 5



print(random_float)


#example.

love_score = random.randint(1,100)
print(f'Your love score is {love_score}')

#Example.

#List data structure

if __name__ == '__main__':

    n = int(input())

    student_marks = {}

    for _ in range(n):

        name, *line = input().split()

        scores = list(map(float, line))

        student_marks[name] = scores

    query_name = input()

    l1 = list(student_marks[query_name]) 

    addition = sum(l1)

    result = addition/len(l1)

    print('%.2f'% result)





















