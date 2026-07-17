# fruits = ["apple" , "orange" , "coconut"]
# vegetable = ["celery" , "carrots" , "potatoes"]
# meats = ["chicken" , "fish" , "turkey"]

# grocery = [fruits , vegetable , meats]

# print(fruits)
# print(vegetable)
# print(meats)

grocery = [["apple" , "orange" , "coconut"],
            ["celery" , "carrots" , "potatoes"],
               ["chicken" , "fish" , "turkey"]
            ]

# print(grocery)

for collection in grocery:
    for food in collection:
        print(food, end=" ")
    print()
