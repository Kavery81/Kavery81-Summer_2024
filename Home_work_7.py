# Расчет наименьшего общего кратного НОК
def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)
while 1:
    try:
        x = int(input('Введите первое число: '))
        y = int(input('Введите второе число: '))
        print('НОК равно:', lcm(x, y))
    except ValueError:
        break


# Шифр Цезаря
alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' # Создаем алфавит
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' # Создаем алфавит
smeshenie = int(input('Шаг шифровки: '))  # Создаем переменную с шагом шифровки
message = input("Сообщение для ДЕшифровки: ").upper()  # Заменяем слово шифровка, на дешифровка
itog = '' # Создаем переменную для вывода итогового сообщения
lang = input('Выберите язык RU/EU: ') # Добавляем возможность выбора языка
if lang == 'RU':
    for i in message:
        mesto = alfavit_RU.find(i) # Алгоритм для шифрования сообщения на русском
        new_mesto = mesto + smeshenie  # Меняем знак + на знак -
        if i in alfavit_RU:
            itog += alfavit_RU[new_mesto]  # Задаем значения в итог
        else:
            itog += i
else:
    for i in message:
        mesto = alfavit_EU.find(i) # Алгоритм для шифрования сообщения на английском
        new_mesto = mesto + smeshenie  # Меняем знак + на знак -
        if i in alfavit_EU:
            itog += alfavit_EU[new_mesto] # Задаем значения в итог
        else:
            itog += i
print (itog)





