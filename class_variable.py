# CLASS VARIABLE --> SHARED AMONG ALL INSTANCES OF A CLASS ..... DEFINE OUTSIDE THE CONSTRUCTOR .... ALLOW YOU TO SHARE THE DATA AMONG ALL THE OBJECT CREATED FROM THAT CLASS

class student:

    class_year = 2026
    num_student = 0

    def __init__(self , name , year):
        self.name = name
        self.year = year
        student.num_student += 1

student1 = student("udayan singh" , 20)
student2 = student("mannu singh" , 19)

print(student1.name)
print(student1.year)
print(student.class_year)
print(student.num_student)
        