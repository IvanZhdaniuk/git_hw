
"""
#Task first
# Напишите программу с классом Math. Создайте два атрибута — a и b. Напишите
# методы addition — сложение, multiplication — умножение, division — деление,
# subtraction — вычитание. При передаче в методы параметров a и b с ними
# нужно производить соответствующие действия и печатать ответ.


class math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)
start =math(3, 9)

print(start.addition())# Без принта не выводистся консоль
print(start.multiplication())# Без принта не выводистся консоль
start.division()# Добавил принт в сам метод
start.subtraction()# Добавил принт в сам метод
"""
"""
#Task second
#1. Создайте класс Soda (газировка). Для инициализации есть параметр,
# который определяет вкус газировки, который при создании объекта можно
# задавать, а можно не задавать. Реализуйте метод для отображения строки
# типа «У вас газировка с таким-то вкусом» в том случае, если вкус задан.
# Если не задан - выведите строку «Просто газировка"

class soda():
    def __init__(self, vkys=None):
        if vkys is None:
            self.vkys = 1
        else:
            self.vkys =vkys


    def otobrazhenie(self):
        if self.vkys == 1:
            print("у Вас газировка.")

        else:
            print(f"у вас гозировка c {self.vkys} вкусом")

a3 = soda("Liker")
a3.otobrazhenie()

a = soda()
a.otobrazhenie()
a.vkys= 'Малиновым'
a1 = soda()
a.otobrazhenie()
"""


#Task three
#5. Разработать класс SuperStr, который наследует функциональность станд
# артного типа str и содержит 2 новых метода:
# • метод is_repeatance (s), который принимает 1 аргумент s и
# возвращает True или False в зависимости от того, может ли текущая
# строку быть получена целым количеством повторов строки s.
# Вернуть False, если s не является строкой. Считать, что пустая строка
# не содержит повторов.
# • метод is_palindrom (), который возвращает True или False в
# зависимости от того, является ли строка палиндромом. Регистрами
# символов пренебрегать. Пустую строку считать палиндромом.


class SuperStr(str):#Создаем класс SuperStr и наследум стандартные методы от класа str
    def __init__(self, text):
        self.text = text
    def is_repeatanse(self):
        b  = self.text
        b = b.split()#Присваеваем список переменной
        counter = 0# Задаем счетчик для для перебора элеменов в строке
        counter_2 = 0 #Задаем счетчик для для отслеживания несовпадений

        for i in b[::-1]:# Запускаем перебор элемнтов с конца строки
            if i != b[counter]:# Сравгиваем первый и последний элемент
                counter_2 +=1# В случае несовпадения увеличивае счетчик
                counter =+ 1# Преходим к следующему элементу строки
            else:
                counter += 1# Преходим к следующему элементу строки
        if counter_2 !=0:# Проверяем на условие выполняется или нет
            return False
        else:
            return True
    def is_palidrom(self):
        b = self.text
        return b == b[::-1]
a = SuperStr("1111 1111 1111 1111 1111")
a.is_repeatanse()
a.is_palidrom()










