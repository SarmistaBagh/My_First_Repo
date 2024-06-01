#Example of udemy program.

#1st input enter height in meters e.g:1.65

#BMI=weight(kg)/height2(m2) formula of body mass index.(BMI)

'''

weight_as_int=int(input("Enter a weight:"))

height_as_float=float(input("Enter a height:"))

#bmi=weight_as_int/(height_as_float * height_as_float)
#OR
bmi=weight_as_int/height_as_float**2

bmi_as_int=int(bmi)

print(bmi_as_int)


#Example

print(8/3)

print(int(8/3))

print(round(8/3))

print(round(8/3, 2))


print(round(2.66666666666, 2))

#Floor division return integer value

print(8//3)

print(type(8//3))


result = 4 / 2

result /=2

print(result)

#Example

score = 0

#user scores a point

score += 1
print(score)

#Example of f-string.

score = 0

print("Your score is " + str(score))


#Example

score = 0

height = 1.8

isWinning= True
#f-string
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

'''

# A 90 Year Human Life years.90*52=4680

age=int(input("Enter your age:"))

years= 90 - int(age)
weeks= years * 52
print(f"You have {weeks} weeks left")




















































































