# INPUT() --> A FUNCTION THAT PROMPTS THE USER TO ENTER DATA RETURNS THE ENTERED DATA AS A STRING

name = input("what is your name: ")
print(f"hii {name}")

age = input("how old are u?: ")
print(f"i am {age} year old")

age = int(age)
age = age + 1
print(f"i am going to {age} years old")


# CALCULATE AREA OF RECTANGLE

length = int( input("length: "))
breadth = int( input("breadth: "))
are = (length * breadth)
print(f"are of rectangle is: {are}sq.m")