# *ARGS --> ALLOWS YOU TO PASS MULTIPLE NON-KEY ARGUMENT 

# **KWARGS --> ALLOWS YOU TO PASS MULTIPLE KEYWORD-ARGUMENT 
#       * UNPACKING OPERATOR

# 1.POSITIONAL, 2.DEFAULT, 3.KEYWORD, 4.ARIBITARY


# def add(*num):
#     total = 0
#     for arg in num:
#         total += arg
#     return total

# print(add(1,2,3,4,5,6,7,9))

# def fullname(*name):
#     for x in name:
#         print(x , end=" ")

# fullname("mr." , "udayan" , "singh")


def address(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} : {value}")

address(dis = "samastipur",
        stste = "bihar",
        village = "jitwarya") 