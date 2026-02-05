class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display (self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class student(Person):
    def __init__(self, name, age,rollNo):
        super().__init__(name,age)
        self.rollNo = rollNo
    def display (self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Roll No: ",self.rollNo)
    
p1 = Person("Kazi",20)
p2 = student("Ahsan",18,68491)

p1.display()
p2.display()