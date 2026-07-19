# STATIC METHOD --> A METHOD THAT BELONG TO A CLASS RATHER THAN ANY OBJECT FROM THAT CLASS (INSTANCES) .... USALLY USED FOR GENERAL UTILITY FUNCTION

# INSTANCES METHOD --> BEST FOR OPERATIONS ON INSTANCES OF THE CLASS (OBJECTS)

# STATIC METHOD --> BEST FOR UTILITY FUNCTION THAT DO NOT NEED ACCESS TO CLASS DATE


class Employee:

    def __init__(self , name , position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position = ["manager" , "cashier" , "cook" , "janitor"]
        return position in valid_position
    
print(Employee.is_valid_position("cashier"))
        
employee1 = Employee("udayan" , "manager")
employee2 = Employee("kumar" , "cashier")
employee3 = Employee("singh" , "cook")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())