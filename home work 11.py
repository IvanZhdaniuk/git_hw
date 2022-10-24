"""ДЗ: работа с модулем os
Есть папка, в которой накиданы файлы с разными расширениями:
.py, .txt. .json и всякие любые какие захотите еще
Программа должна:
1. Вывести имя вашей ОС
2. Вывести путь до папки в которой вы находитесь
3. Рассортировать файлы по расширениям: создается новая директория например
для питонских файлов, в нее закидываются все файлы .py которые есть в
текущей директории, то же самое с остальными расширениями
4. После сортировки выводится информация типа: «в папку с питонскими
файлами закинуто 5файлов, их суммарный размер равен 50 гигабайт»
5. Из питонских файлов как минимум один запустить на выполнение и
получить результат его выполнения. Например, файл делает просто
print(«Hello world»), ваша программа должна вывести что-то типа «После
запуска файла programma.py получен результат ‘Hello world’»
6. Как минимум один файл в какой-либо из получившихся подпапок
переименовать. Например был data.txt, вы заренеймили в data_renamed.txt.
Программа ваша должна вывести что-то типа «Файл data.txt успешно
переименован в data_renamed.txt»
7.  Программа по возможности не должна быть привязана к выполнению чисто
на винде - не должно быть хардкодов типа с именем диска (и вообще без
хардкода там где это можно пожалуйста если можно спасибо)"""

import os
import shutil
import subprocess, sys
import random

class Order_on_the_computer():

    def work_with_file():
        ''' Выводит на печать наименование операйионной системы'''
        print(os.name)

    def directory_path():
        """Выводит на печать текущий рабочий католог
        :return:
        """
        print(os.getcwd())

    def copi_and_sort_file():
        """ Проверяет сщдержимое католога на принадлежность к файлам, создаeт новые паки
        по раширению файлов, копируют фалы по пакам в соответвии с их расширеним"""
        data = os.listdir()
        data1 = os.getcwd()
        new_set = {}
        new_set_size ={}


        for i in data:
            if os.path.isfile(i):
                extenshion = i.split('.')
                extenshion = str(extenshion[-1::])
                extenshion = extenshion
                if os.path.exists(data1+ "/" + extenshion):
                    shutil.copyfile(data1 + "/" + i, data1 + "/" + extenshion + "/" +i)

                    new_set[extenshion] += 1
                    new_set_size[extenshion] += os.path.getsize(data1 + "/" + extenshion + "/" +i)

                else:
                    os.mkdir(data1+ "/" + extenshion)
                    new_set[extenshion] = 1
                    new_set_size[extenshion] =0
                    shutil.copyfile(data1+ "/" +i, data1+ "/" + extenshion + "/" + i)
                    new_set_size[extenshion] += os.path.getsize(data1 + "/" + extenshion + "/" + i)

        for i in new_set:
            print(f"В папку с {i} файлами закинуто {new_set[i]} файлов, их суммарный объем составляет {new_set_size[i]} байт")


    def start_file():
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, "World.py"])
        print(" File World.py is open")

    def rename_file():
        '''переименовываем случайный файл в новой диектории'''
        old_file_name = os.listdir(os.getcwd() +'/'+ "['py']")
        b =random.randint(0, len(old_file_name))
        old_file_name = old_file_name[b]

        new_file_name = "new" + old_file_name
        os.rename(old_file_name, new_file_name)
        print(f"File {old_file_name} rename in  {new_file_name}")




start = Order_on_the_computer
# start.work_with_file()
# start.directory_path()
# start.copi_and_sort_file()
#start.start_file()
start.rename_file()








