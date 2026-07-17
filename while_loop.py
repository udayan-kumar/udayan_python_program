# WHILE LOOP --> EXECUTE SOME CODE WHILE SOME CONDITION REMAINS TRUE

num = int(input("enter your number: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("enter your number: "))

print(f"your number is: {num}")