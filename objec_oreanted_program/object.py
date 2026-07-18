# OBJECT --> A BUNDLE OF RELATED ATTRIBUTE (VARIABLES) AND METHOD (FUNCTION) 

# CLASS --> (BLUEPRINT) USED TO DESIGN THE STRUCTURE AND LAYOUT OF AN OBJECT

class car:
    def __init__(self , model , year , color , for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"you drive the {self.color} {self.model}")

    def stop(self):
        print(f"you have to stop the {self.color}{self.model}")

    def describe(self):
        print(f"{self.year} {self.model} {self.color}")

# car1 = car("BMW" , 2026 , "black" , False)
# car2 = car("bugati" , 2026 , "red" , True)

# print(car1.year)
# print(car1.model)
# print(car1.for_sale)

# print(car2.year)
# print(car2.model)
# print(car2.for_sale)


        