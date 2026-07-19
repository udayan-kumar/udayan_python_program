# CLASS METHOD --> ALLOW OPERSTION RELATED TO THE CLASS ITSELF ...... TAKE (CLS) AS THE FIRST PARAMETER , WHICH REPRESENT THE CLASS ITSELF

# INSTANCE METHOD --> BEST FOR OPERATION ON INSTANCE OF THE CLASS (OBJECT)

# STATIC METHOD --> BEST FOR UTILITY FUNCTION THAT DO NOT NEED ACCESS TO CLASS DATA

# CLASS METHOD --> BEST FOR CLASS-LEVEL DATA OR REQUIRES ACCESS TO THE CLASS ITSELF

class Student:

    count = 0
    totsl_gpa = 0

    def __init__(self , name , gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.totsl_gpa += gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"totsl number of student: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.totsl_gpa / cls.count: .2f}"
    
atudent1 = Student("udayan" , 9.3)
atudent2 = Student("kumar" , 5.3)
atudent3 = Student("mannu" , 8.3)
print(Student.get_count())
print(Student.get_average_gpa())
    