

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

# Как делать ссылки на другие листы с программой

class Staff:
    def __init__(self, pPosition, pName, pPay):
        self.position = pPosition
        self.name = pName
        self.pay = pPay
        print("Creating Staff object")

    def __str__(self):
         return "Position =%s, Name = %s, Pay = %d" %(self.position, self.name, self.pay)

    def calculatePay(self):
        prompt = "\n Enter number of hours worked for %s:" %(self.name)
        hours = input(prompt)
        prompt = "Enter the hourly rate for %s:" %(self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours) * int(hourlyRate)
        return self.pay

offiseStaff1 = Staff("basik", "Ivan", 0)
offiseStaff1.name = "Kirill"
offiseStaff1.position = "manage"
print(offiseStaff1.name)
print(offiseStaff1.position)



