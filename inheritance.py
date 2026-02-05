class animal :
    def sound(self):
        print("Animal makes a sound")
class Dog(animal):
    def sound(self):
        print("WOOF WOOF")

d =Dog()
d.sound()