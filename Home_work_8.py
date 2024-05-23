# 2. На ввод подается список, состоящий из списков чисел. Отсортируйте этот список по возрастанию общего числа цифр (не чисел!) в каждом списке
lst_1 = []
n = int(input("Введите требуемое количество чисел в первом списке: "))
for i in range(0, n):
    ele = float(input())
    lst_1.append(ele)
    res_1 = lst_1.sort(reverse=True)

lst_2 = []
t = int(input("Введите требуемое количество чисел во втором списке: "))
for i in range(0, t):
    ele = float(input())
    lst_2.append(ele)

lst_3 = []
j = int(input("Введите требуемое количество чисел в третьем списке: "))
for i in range(0, j):
    ele = float(input())
    lst_3.append(ele)

print(sorted(lst_1), sorted(lst_2), sorted(lst_3))




# 1. На вход программе подается строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитазин), Т (тимин). Подкорректируйте код
a = input('Введите генетический код: ')
String = 'АГЦТ'
for ind,ch in enumerate(String[:-1]):
    if ch == String[ind+1]:
        print('ГА')
    print('ГА')