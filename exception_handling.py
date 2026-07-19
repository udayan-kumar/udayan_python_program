# EXCEPTIONAL HANDLING --> AN EVENT THAT INTERUPTS  THE FLOW OF A PROGRAM ... (ZERODIVISIONERROR , TYPEERROR , VALUEERROR)

# 1.TRY  2.EXCEPT  3.FINALLY

try:
    number = int(input("enter your number: "))
    print(1 / number)

except ZeroDivisionError:
    print("chutiye divide nhii hoga")

except ValueError:
    print("only integer are allowed")

except Exception:
    print("chutiye kuchh bhii type kar raha hai")

finally:
    print("udayan singh")