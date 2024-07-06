class homer:
    def __init__(self,name):
        self.name=name
class Daughter(homer):
    pass
daughter1=Daughter("lisa")
print(daughter1.name)




class Shape:
    def calculate_area(self):
        pass
class Rectangle(Shape):
    pass
class Circle(Shape):
    pass
class Triangle(Shape):
    pass




class Animal:
    catt="meow"
    dogg="woof"
    birds="Я не знаю как написат чирикание птицы"
class cat(Animal):
    def make_sound(self):
        print(self.catt)
class dog(Animal):
    def make_sound(self):
        print(self.dogg)
class bird(Animal):
    def make_sound(self):
        print(self.birds)

