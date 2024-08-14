from math import pi
# oop home work 

# (1)
class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age


ali = Person('ali', 20)



# (2)
class Person1 :
  def __init__(self,name,age):
      self.name = name
      self.age = age
    

  def greet(self):
      print('Hello Wellcome Mr:' + self.name)

first_person1 = Person1('Ahsan', 14) 
first_person1.greet()



# (3)
class Car:
    def __init__(self,model,made,year):
        self.model = model
        self.make = made
        self.year = year


car1 = Car('Benz','made by USA', 2020)

print(car1.make)
print(car1.model)
print(car1.year)


# (4)
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        a_a = pi * (self.radius ** 2)
        print(a_a)


cri1 = Circle(5)
cri1.area()
    
# (5)

class A_P:

    def __init__(self, tool, arz):
        self.tool = tool
        self.arz = arz

    def area(self):
        a_t = self.tool * self.arz
        print(a_t)

    def enviroment(self):
        p_t = (self.tool * 2) + (self.arz * 2)
        print(p_t)


ap1 = A_P(5, 4)
ap1.area()
ap1.enviroment()








