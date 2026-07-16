# LOGICAL OPERATOR --> EVALUATE MULTIPLES CONDITIONS (OR , AND , NOT)
#       OR --> AT LEAST ONE CONDITION MUST BE TRUE
#       AND --> BOTH CONDITION MUST BE TRUE
#       NOT --> INVERTS THE CONDITION (NOT FALSE , NOT TRUE)

temp = 25
is_raining = False

if temp >35 or temp <0:
    print("good temperatur")
else :
    print("not good temperature")


if temp >40 and temp <45:
    print("good")
else :
    print("not good")

    if temp >45 and not temp <23:
        print ("udaya singh")
    else:
        print("mannu")