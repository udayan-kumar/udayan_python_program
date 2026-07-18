# VARIABLE SCOPE --> WHERE A VARIABLE IS VISIBLE AND ACCESSIBLE 

# SCOPE RESOLUTION --> (LEGB) LOCAL -> ENCLOSED -> GLOBAL -> BUILT-IN

# LOCAL SCOPE

# def func1():
#     x = 10
#     print(x)

# def func2():
#     x = 20
#     print(x)

# func1()
# func2()

# ENCLOSED SCOPE

# def func1():
#     x = 10
#     def func2():
#         print(x)
#     func2()

# func1()

# GLOBAL SCOPE

# x = 30

# def func1():
#     print(x)

# def func2():
#     print(x)

# func1()
# func2()


# BUILT-IN SCOPE
from math import e

def func1():
    print(e)

e = 40
func1()