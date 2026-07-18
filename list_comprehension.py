# LIST COMPREHENSION --> A CONCISE WAY TO CREATE LIST IN PYTHON ...... COMPARE AND EASIER WAY TO READ THE TRADITIONAL LOOPS [EXPRESSION FOR VALUE IN ITERABLE IF CONDITION]

triple = []

for x in range (1,11):
    triple.append(x * 3)

print(triple)

triple = [x * 3 for x in range(1,11)]
print(triple)

quad = [y * 4 for y in range(1,11)]
print(quad)

fruits = ["apple" , "orange" , "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

number = [1,-2,3,-4]
po_number = [num for num in number if num >= 0]
n_number = [num for num in number if num < 0]
print(po_number)
print(n_number)