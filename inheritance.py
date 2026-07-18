#  INHERITANCE --> ALLOWS A CLASS TO INHERIT ATTRIBUTE AND METHOD FROM ANOTHER CLASS ..... HELPS THE CODE REUSABILITY AND EXTENSIBILITY ..... CLASS CHILD(PARENT)

# MULTIPLE INHERITANCE --> INHERIT FROM MORE THAN ONE PARENT CLASS C(A,B)

# MULTILEVEL INHERITANCE --> INHERIT FROM A PARENT WHICH INHERITS FROM ANOTHER PARENT C(B) <- B(A) <- A



# class animal:
#     def __init__(self , name):
#         self.name = name
#         self.is_alive = True

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Dog(animal):
#     pass

# class Cat(animal):
#     pass

# class Mouse(animal):
#     pass

# dog = Dog("tommy")
# cat = Cat("meow")
# mouse = Mouse("chuha")

# print(dog.name)
# dog.eat()
# cat.eat()
# mouse.eat()

class animal:
    

    def eat(self):
        print("this animal is eating")

    def sleep(self):
        print("this animal is eating")

class prey(animal):
    def flee(self):
        print("this animal is fleeing")

class predator(animal):
    def hunt(self):
        print("this animal is hunting")

class Rabbit(prey):
    pass

class Hawk(predator):
    pass

class Fish(prey , predator):
    pass

rabbit = Rabbit()
rabbit.flee()
rabbit.eat()

fish = Fish()
fish.hunt()