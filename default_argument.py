# DEFAULT ARGUMENT --> A DEFAULT VALUE FOR CERTAIN PARAMETER .... DEFAULT IS USED WHEN THAT ARGUMENT IS OPTIMIZED .... MAKE YOUR FUNCTIONS MORE FLEXIBLE , REDUCES , OF ARGUMENTS
# 1.POSITIONAL, 2.DEFAULT, 3.KEYWORD, 4.ARIBITARY


def price (list_price , discount = 0 , tax = 0.05):
    return list_price * (1-discount) * (1+tax)

print(price(500))
print(price(500 , 0.1))
print(price(500 , 0.1 , 0))