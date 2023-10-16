class Person:
    def __init__(self, Name, Age):
        self.name = Name #age is property
        self.age = Age
        
    def introduce(self): #Method [Since in class; NOT FUNCTION]
        print(f"My name is {self.name} and my age is {self.age}")
        
person1 = Person ("Lexi", 26)
person2 = Person ("Lily", 24)
print(person1.name, person1.age)

person2.introduce()