name = input()

# LENGTH OF STRING
result = len(name)

# LENGTH OF FIRST WORD
result = name.find(" ")

# LENGTH OF LAST WORD
result = name.rfind(" ")

# PRINT FIRST WORD AS A CAPITALIZE
name = name.capitalize()
print(name)

# PRINT WHOLE WORD IN CAPATALIZE
name = name.upper()
print(name)

# PRINT WHOLE WORD IN LOWER CASE
name = name.lower()

# CHECK STRING HAVE ONLY DIGIT OR NOT
result = name.isdigit()

# CHECK STRING CONTAIN ONLY ALPHABET OR NOT
result = name.isalpha()

# FOR COUNTING ANY THING
result = name.count()

# FOR REPLACING ANY THING
result = name.replace("udayan sngh" , "mannu singh")



print(result)