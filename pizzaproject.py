#Example.
'''
print("Thank you for choosing python pizza Deliveries!")
size=input("What size pizza do you want?S,M or L:")

add_pepperoni = input("Do you want pepperoni?")

extra_chees =input("Do you want extra cheese?")                      

bill=0

if size == "s":
    bill+=15
    
elif size == "m":
    bill +=20

else:
    bill +=25

if add_pepperoni == "y":
    if size =="s":
        bill +=2
    else:
        bill +=  3
if extra_chees == "y":
    bill +=1

print(f'Your final biil is: ${bill}.')    

#Logical operators.
#not,and,or

#Love calculator.

print("The love calculator is calculating your score!")

name1=input("What is your name?")
name2=input("What is their name?")

combined_names=name1+name2

lower_names=combined_names.lower()

t=lower_names.count("t")
r=lower_names.count("r")
u=lower_names.count("u")
e=lower_names.count("e")
first_digit=t+r+u+e

l=lower_names.count("l")
o=lower_names.count("o")
v=lower_names.count("v")
e=lower_names.count("e")
second_digit=l+o+v+e

score=int(str(first_digit) + str(second_digit))
if (score <10) or (score >90):
    print(f"Your score is {score},you go together like coke and mentos")

elif (score>=40) and (score <=50):
    print(f"Your score is {score},you are alright together.")

else:
    print(f'Your score is {score}')

'''

#Example.

print("Welcome to Tresure Island")

print("Your mission is to find treasure.")

print("you're at a cross road.Where do you want to go? Type "left" or "right")






      






































    







































        
         
