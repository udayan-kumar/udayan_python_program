# RETURN --> STATEMENT USED TO END A FUNCTION AND SEND A RESULT BACK TO THE CALLER



# def add(x,y):
#     z = x + y
#     return z

# def sub(x,y):
#     z = x - y
#     return z

# def multiply(x,y):
#     z = x * y
#     return z

# def divide(x,y):
#     z = x / y
#     return z

# print(add(10,29))
# print(sub(10,29))
# print(multiply(10,29))
# print(divide(10,29))


def create_name(first , last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

print(create_name("udayan" , "kumar"))
