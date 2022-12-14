import string


"""
#Task first
# Запрещенные слова
#
# Напишите программу, которая получает на вход строку с названием текстового файла,
# и выводит на экран содержимое этого файла, заменяя все запрещенные слова звездочками *
# (количество звездочек равно количеству букв в слове).
# Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt.
# Все слова в этом файле записаны в нижнем регистре.
# Программа должна заменить запрещенные слова, где бы они ни встречались,
# даже в середине другого слова. Замена производится независимо от регистра: если файл forbidden_words.txt
# содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
# Предположим, что forbidden_words.txt содержит следующие запрещенные слова:
#
# hello email python the exam wor is
#
# А текст файла, подлежащего цензуре, выглядит так:
#
# Hello, world! Python IS the programming language of thE future. My EMAIL is....
# PYTHON is awesome!!!!
#
# Тогда программа должна вывести отредактированный текст в таком виде:
#
# *****, ***ld! ****** ** *** programming language of *** future. My ***** **....
# ****** ** awesome!!!!


def sensorship(object):
    with open(object, "r") as f:
        text = f.read()
        b = text
        with open(f"farbidden_words.txt", "r") as f2:
            text_sensor = f2.read().split()
            for i in text_sensor:
                b = b.lower().replace(f"{i}", "*"*len(i))
            for i in range(len(text)):
                if b[i] =="*":
                    print("*", end="")
                else:
                    print(text[i], end="")
sensorship("task_first.txt")
"""

"""
#Task second
# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов


def averange_score_less_than_three(start):#Объявляе функцию и вводим переменну для функции
    if start == 1:#Запустили программу
        count = -1# Завели счетчик и уменьшили на один, так как нам нужно начать перебор с нулевого значения.
        with open("task_two.txt", "r") as f:#Запустили функцию чтения из файла.
            data_file = f.read().split()# прочитали файл, создали список элементов из исходного поделив по пробелам,
            # и присвоили значение переменной
            for i in range(int(len(data_file)/3)):#запустили цикл столько раз сколько строк в текстовом файле.
                count += 3#счетчик увеличиваем сразу на три для контроля оценок учеников
                if int(data_file[count]) <= 3:#отбираем учеников с оценками ниже трех
                     print(data_file[count - 2], data_file[count - 1],data_file[count])#Выводим на печать список
                     # учеников у котрых оценка ниже 3 баллов
averange_score_less_than_three(1)#Запускаем функцию
"""

"""
#Task tree
# В файле могут быть записаны десятичные цифры и все, что угодно.
# Числом назовем последовательность цифр, идущих подряд (т.е. число всегда неотрицательно).
#
# Вычислите сумму всех чисел, записанных в файле. В данной задаче удобно считывать данные посимвольно.
#
# Примеры
# входные данные
#  123
# aaa456
# 1x2y3 4 5 6
#
# выходные данные
# 600


def summa_number_in_file(object):
    with open(object, "r") as f:
        data = f.read()
        b = ""#Новый список чтобы оставить только цыфры, а все стальные элементы заменить на *
        for i in data:
            if i.isdigit():
                b +=i
            else:
                b += "*"
        c = b.split("*")# Переводим строку в список и разиваем на элементы по звездачкам
        summ_text=0
        for i in c:
            if i.isdigit():#Если число то сумеруем
                summ_text += int(i)
    print(summ_text)
summa_number_in_file("task_three.txt")


"""


"""
#task four
# В Государственную Думу Федерального Собрания Российской Федерации выборы производятся по партийным спискам.
# Каждый избиратель указывает одну партию, за которую он отдает свой голос.
# В Государственную Думу попадают партии, которые набрали не менее 7% от числа голосов избирателей.
#
# Дан список партий и список голосов избирателей. Выведите список партий, которые попадут в Государственную Думу.
#
# Входные данные
# В первой строке входного файла написано слово PARTIES:. Далее идет список партий, участвующих в выборах.
#
# Затем идет строка, содержащая слово VOTES:.
# За ней идут названия партий, за которые проголосовали избиратели,
# по одному названию в строке. Названия могут быть только строками из первого списка.
#
# Выходные данные
# Программа должна вывести названия партий, получивших не менее 7% от числа голосов в том порядке,
# в котором они следуют в первом списке.
#
# Примеры
# входные данные
# PARTIES:
# Party one
# Party two
# Party three
# VOTES:
# Party one
# Party one
# Party three
# Party one
# Party one
# Party three
# Party two
# Party one
# Party three
# Party three
# Party one
# Party one
# Party three
# Party three
# Party one
# выходные данные
# Party one
# Party three


def couting_of_votes(text_five):
    with open(text_five, "r") as f:
        d = {}
        counter = 0
        counter_part = 0
        for line in f:
            if counter == 1 and line != "VOTES:\n":
                d[line.replace("\n", "")] = 0
            if counter == 2:
                d[line.replace("\n", "")]= d[line.replace("\n", "")]+1
            if line == "PARTIES:\n":
                counter = 1
            if line == "VOTES:\n":
                counter = 2
        for j in d:
            counter_part +=d[j]
        for j in d:
            if d[j]/counter_part > 0.07:
                print(j)

couting_of_votes("text_five.txt")


#task five
# Z: Гистограмма
#
# Вовочка ломает систему безопасности Пентагона. Для этого ему понадобилось узнать,
# какие символы в секретных зашифрованных посланиях употребляются чаще других.
# Для удобства изучения Вовочка хочет получить графическое представление встречаемости символов.
# Поэтому он хочет построить гистограмму количества символов в сообщении.
# Гистограмма – это график, в котором каждому символу,
# встречающемуся в сообщении хотя бы один раз, соответствует столбик,
# высота которого пропорциональна количеству этих символов в сообщении.
#
# Входной файл содержит зашифрованный текст сообщения.
# Он содержит строчные и прописные латинские буквы, цифры, знаки препинания,
# пробелы и переводы строк. Текст содержит хотя бы один непробельный символ.
# Все строки входного файла не длиннее 200 символов.
#
# Для каждого символа кроме пробелов и переводов строк выведите столбик из символов «#»,
# количество которых должно быть равно количеству символов в данном тексте.
# Под каждым столбиком напишите символ, соответствующий ему.
# Отформатируйте гистограмму так, чтобы нижние концы столбиков были на одной строке,
# первая строка и первый столбец были непустыми.
# Не отделяйте столбики друг от друга.
# Отсортируйте столбики в порядке увеличения кодов символов.
#
# Ввод
# Hello, world!
#
# Вывод
#      #
#      ##
# #########
# !,Hdelorw
#
#
# Ввод
# Twas brillig, and the slithy toves
# Did gyre and gimble in the wabe;
#
# All mimsy were the borogoves,
# And the mome raths outgrabe.
#
# Вывод
#
#          #
#          #
#          #
#          #
#          #
#          #         #
#          #  #      #
#       #  # ###  ####
#       ## ###### ####
#       ##############
#       ##############  ##
# #  #  ############## ###
# ########################
# ,.;ADTabdeghilmnorstuvwy

def gistogramm(objeckt):
    with open(objeckt, "r") as f:
        data = f.read().replace("\n", "").replace(" ", "")
        d = {}
        print(data)
        for i in data:
            if i in d:
                d[i] = d[i]+1
            if i not in d:
                d[i] = 0
        print(sorted(d.items()))
        count = 0
        max_count = 0
        for i in d:
            if d[i]>max_count:
                max_count =d[i]#Нашли самое большое число, == выслте гистограммы

        print(max_count)
        b = max_count
        print("----------------------")
        n=sorted(d.items())
        print(n)
        for i in range(max_count):
            print()
            b -= 1
            for j in n:
                if b > j[1]:
                    print(" ", end='')
                if b <= j[1]:
                    print("#", end='')
        print("")
        for i in n:
            print(i[0], end='')


gistogramm("tas_gistogramma")
"""