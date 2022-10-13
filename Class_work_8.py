

"""
task_1
class Auto:
    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print("Move")
    def stop(self):
        print("Stop")

    def birthday(self):
        age = self.age
        print(age)

a = Auto(1, 34, 44)
a.move()
a.stop()
a.birthday()
"""
"""

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def Start(self):
        return "Автомобиль заведен"
    def Stop(self):
        return "Автомобиль заглушен"


    def wreat_year(self, year):
         self.year = year

    def wreat_tupe(self, type):
         self.type = type
         return type


m = Car("yelow", "bet", 2022)

print(m.Start())
print(m.Stop())
print(m.wreat_year("202222"))
"""
# Как делать ссылки на другие листы с программой
"""
class Staff:
    def __init__(self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay = pPay
        print("Creating Staff object")

    def __str__(self):
         return "Position =%s, Name = %s, Pay = %d" %(self._position, self.name, self.pay)

    def calculatePay(self):
        prompt = "\n Enter number of hours worked for %s:" %(self.name)
        hours = input(prompt)
        prompt = "Enter the hourly rate for %s:" %(self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours) * int(hourlyRate)
        return self.pay

offiseStaff1 = Staff("basik", "Ivan", 0)
offiseStaff1.name = "Kirill"
offiseStaff1._position = "manage"
print(offiseStaff1.name)
print(offiseStaff1._position)


    @property
    def position(self):
        print("Getter Method")
        return self._position

    @position.setter
    def position(self, value):
        if value == "Manager" or value == "Basic":
            self._position = value
        else:
            print("Posithion is invalid. No changes made")
"""
"""
class Vehicle(object):

"""
#    Функция меняет свое имя на «method»
"""
    def __init__(self, color, doors, tires, vtype):
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype


    def brake(self):
        return "%s braking" % self.vtype
    def drive(self):
        return "I'm driving a %s %s!" % (self.color, self.vtype)


if __name__ == "__main__":
    car = Vehicle("blue", 5, 4, "car")
    print(car.brake())
    print(car.drive())



    truck = Vehicle("red", 3, 6, "truck")
    print(truck.color)
    print(truck.brake())
    
"""

"""

class A:
    def _privat(self):
        print("Это приватный метод из-за нижнего "
              "подчеркнивания перед названием")

a = A()
a._privat()
class B:
    def __privat(self):
        print("Это приватный метод из-за нижнего "
              "подчеркнивания перед названием")

b = B()
b._B__privat()


"""
"""
class Human:
    def breathe(self):
        print("Человек дышит")

    def walk(self):
        print("Человек ходит")

class Doktor(Human):
    def heal(self):
        print("Доктор лечит")

d = Doktor()
d.walk()
d.breathe()
d.heal()

"""
"""
class Cat:
    def info(self):
        print("I am a cat.")
    def make_sound(self):
        print("Meow")
class Dog:
    def info(self):
        print("I am a dog")
    def make_sound(self):
        print("Wow")


c = Cat()
d = Dog()
for annimal in (c, d):
    annimal.make_sound()
    annimal.info()
    annimal.make_sound()

"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def score(self):
        return sum(self.marks)/len(self.marks)
    def __gt__(self, other):
        return self.score() > other.score()

Vasay = Student("Vasay", [6, 7, 8])
Kolay = Student("Kolay", [7, 10, 9])
print(Vasay.score())
print(Kolay.score())
Vasay.score()
Kolay.score()
print(Vasay > Kolay)#Почему не выводится без принта!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(Kolay > Vasay)#Почему не выводится без принта!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Vasay > Kolay


from abc import abstractmethod, ABC
class ChessPiece(ABC):
    def draw(self):
        print("Drew a chess piece")
    @abstractmethod
    def move(self):
        print("Абстрактный клас")
b = ChessPiece()
b.draw()
b.move()

print("---------------")
class abstract(ChessPiece):
    def droooo(self):
        print("triiipl")

v = abstract()
v.draw()
v.move()# Примечание: мы не можем создавать экземпляры абстрактного класса. Это вызывает Error .!!!!!!!!!!!А это тогда что
v.droooo()
print(abstract.mro())









