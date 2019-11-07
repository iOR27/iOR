# Подключение модуля Colorama
from random import random
from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.BLACK) #Цвет символов 'Colorama'
print(Back.GREEN) #Цвет фона для операции what 'Colorama'
#Выбераем математическую операцию
what = input("что делаем?(+,-,*,/): ") #Вводи символа операции
print(Back.CYAN) #Цвет фона вводимых чисел 'Colorama'
#Вводим числа 
a = float (input("Введи первое число: ")) #Ввод числа 1 для обработки
b = float (input("Введи второе чиоло: ")) #Ввод числа 2 для обработки
print(Back.MAGENTA) #Цвет фона для результата 'Colorama'
#Блок математической обработки вводимых чисел
if what =="+": #Начало обработки для действия сложения
    c = a + b
    print("Результат: " + str(c))
elif what == "-": #Для отнимания
    c = a - b
    print("Результат: " + str(c))
elif what == "*": #Для умножения
    c = a * b
    print("Результат: " + str(c))
elif what == "/": #Для деления 
    c = a / b
    print("Результат: " + str(c))
else: #Если выбрано не верную операцию 
    print("Выбраная неверная операция!")
input()