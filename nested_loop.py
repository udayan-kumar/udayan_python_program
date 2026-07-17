# NESTED LOOP --> A LOOP WITHIN ANOTHER LOOP (OUTER , INNER)
#       OUTER LOOP:
#               INNER LOOP:

# for x  in range (1,10):
#     print(x , end=" ")

for x in range(3):
    for y in range(1,10):
        print(y , end=" ")
    print()