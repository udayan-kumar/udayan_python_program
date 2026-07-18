# DUCK TYPING --> ANOTHER WAY TO ACHIVE POLYMORPHISM BESIDES INHERITANCES .... OBJECT MUST HAVE THE MINIMUM NECESSARY ATTRIBUTES/METODS .... "IF IT LOOKS LIKE A DUCK AND QUACKS LIKE A DUCK , IT MUST BE A DUCK"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("bhaoo")

class Cat(Animal):
    def speak(self):
        print("meooow")

class Car:
    alive =True

    def speak(self):
        print("horn")

animals = [Dog() , Cat() , Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)