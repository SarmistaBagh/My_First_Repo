#Day3

#Conditional statements,logical operators,Code Blocks and Scope.
'''
water_level=50

if water_level>80:
    print("drain water")

else:
    print("Continue")

#Tickets.project

print("Welcome to the rollercoaster!")

height=int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!")

else:
    print("Sorry,you have to grow taller before you can ride.")
#Example.

number = int(input("Enter a number:"))

if number %2==0:
    print("even number")


else:
    print("odd no")


#Example.

print("Welcome to the rollercoaster!")

height=int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age <12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7.")
        
    else:
        print("Please pay $12.")

else:
    print("Sorry,you have to grow taller before you can ride.")

#Body mass index calculation.
    
weight=int(input("Enter a weight:"))

height=float(input("Enter a height:"))

bmi=weight/(height*height)

#total_bmi=int(bmi)
#print(total_bmi)

if bmi <18.5:
    print(f"Your BMI is {bmi},you are under weight.")

elif bmi < 25:
    print(f"Your BMI is {bmi},you have a normal weight.")

elif bmi <30:
    print(f"Your BMI is {bmi},you are slightly over weight.")

elif bmi <35:
    print(f"Your BMI is {bmi},you are obese")
     
else:
    print(f"Your Bmi is {bmi},you are clinically obese.")

'''
#Example of which year do you want to check?

year = int(input("Enter a number:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")               
    else:
        print("Leap year:")
else:
    print("Not leap year:")


#Example.of if,elif,else

print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm?"))

if height >=120:
    print("you can ride the rollercoaster!")
    age = int(input("what is your age?"))
    bill=0
    if age <12:
        bill =5
        print("child tickets are $5.")
    elif age <=18:
        bill =7
        print("youth tickets are $7.")
    else:
        bill=12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill +3
    print(f'Your final bill is {bill}')

else:
    print("Sorry,you have to grow taller before you can ride.")

     

    




























    

    



























































