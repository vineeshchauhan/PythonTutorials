#Numbers
#Strings
#Boolean
#Lists
#Dictionaries

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} is talking')




class Man(Person):
    def __init__(self, name):
        super().__init__(name)
        print("Person")

person1 = Person('Vineesh')
person1.talk()

man = Man("person1")


print(man.name)