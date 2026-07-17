# KEYWORD ARGUMENT --> AN ARGUMENT PRECEDED BY AN IDENTIFIER .... HELPS WITH READABILITY .... ORDER OF ARGUMENT DOESNOT MATTER...
# 1.POSITIONAL, 2.DEFAULT, 3.KEYWORD, 4.ARIBITARY


def hello(greeting , title , first , last):
    print(f"{greeting} {title} {first} {last}")

hello("hello" , "mr." , "udayan" , "singh")
hello("hello" , title = "mr." ,last = "singh", first = "udayan")