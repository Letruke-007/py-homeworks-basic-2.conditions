# Задача 1. hackerrank - Python-If-Else

n = int(input())

if n % 2 == 1:
    print('Weird')
elif 2 <= n <=5 and n % 2 == 0:
    print('Not Weird')
elif 6 <= n <= 20 and n % 2 == 0:
    print('Weird')
elif n >= 20 and n % 2 == 0:
    print('Not Weird')

# Задача 2. Проверка для военкомата

h = int(input('Введите рост в сантиметрах: '))
age = int(input('Укажите возраст в годах: '))
kids = int(input('Укажите число детей: '))
learning = input('Учитесь ли Вы в ВУЗе в настоящее время по очной программе обучения?: ')

if h < 150 or 30 < age < 18 or kids > 2 or learning.lower() == 'да':
    print('Вы не подлежите военной обязанности')
else:
    print('Вы должны встать на воинский учет и подлежите призыву на срочную службу')
