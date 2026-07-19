# DECORSTOR --> A FUNCTION THAT EXTENDS THE BEHAVIOR OF ANOTHER FUNCTION ...... W/O MODIFYING THE BASE FUNCTION ...... PASS THE BASE FUNCTION AS AN ARGUMENT TO THE DECORATOR

#       @add_sprinkles
#       get_ice_cream("choclate")

def add_sprinkles(func):
    def wrapper(*args , **kwargs):
        print("you add sprinkles 😎")
        func(*args , **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args , **kwargs):
        print("you add fudge 🍫")
        func(*args , **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
   print(f"here is your {flavour} ice cream 🍨")

get_ice_cream("chocklate")