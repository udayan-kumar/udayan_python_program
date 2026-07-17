# DICTIONARY --> A COLLECTION OF {KEY : VALUE} PAIRS ,, ORDERED AND CHANGEBALE ... NO DUBLICATE

capitals = {"usa" : "washington dc",
            "india" : "new delhi",
            "china" : "beijing",
            "russia" : "moscow"}

# print(capitals.get("india"))

capitals.update({"gemany" : "berlin"})
print(capitals)

capitals.update({"india" : "delhi"})

capitals.pop("china")
capitals.popitem()

# capitals.clear()

print(capitals)

values = capitals.values()
print(values)

for value in capitals.values():
    print(value)

# item = capitals.items()
for key , value in capitals.items():
    print(f"{key} : {value}")

