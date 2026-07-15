# TYPECASTING --> THE PROCESS OF CONVERTING A VARIABLE FROM ONE DATA TYPE TO ANOTHER str() , int() , flost() , bool()....

name = "udayan singh"
age = 23
gpa = 3.2
is_student = True

# CHECK TYPE
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))


#TYPECASTING

gpa = int(gpa)
print(gpa)

age = str(age)
print(type(age))

# IF IN STRING I WROTE SOMETHING THEN BOOLEAN GIVE US TRUE..... BTUT I DON'T WRITE SOMETHING IN STRING THEN BOOLEAN GIVE US FALSE AS A RESULT
name = bool(name)
print(name)

