#  MEMEBERSHIP OPERSTOR --> USED TO TEST WHETHER A VALUE OR VARIABLE IS FOUND IN A SEQUENCES (STRING , LIST , TUPLE , SET , OR DICTIONARY)
#       1. IN
#       2. NOT IN

word = "apple"

letter = input("guess a letter in  the seceret: ")

# if letter in word:
#     print(f"there is a {letter}")
# else:
#     print(f"{letter} was not found")

if letter not in word:
    print(f"{letter} was not found")
   
else:
     print(f"there is a {letter}")

