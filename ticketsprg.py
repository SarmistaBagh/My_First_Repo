#Example.of if/elif/else

print("Welcome to the rollercoaster!")

height = int(input("Enter what is your height!"))

bill = 0
if height >=120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("child tickets are $5.")

    elif age <=18:
        bill = 7
        print("Youth tickets are $7.")

    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want to photo taken? y or n")
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill} ")   

else:
    print("Sorry, you have to grow taller before you can ride")

#Example.

    

