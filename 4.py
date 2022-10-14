'''Задана натуральная степень k. Сформировать случайным образом список 
коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен 
степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''
import random
import string

k=int(input('Введите k '))
result = ""
while k>=0:
    coef = random.randint(0,100);
    if coef==0:
        k-=1
        continue
    if result!="": result+="+"
    if k==0: 
        result+=str(coef)
        k-=1
        continue
    result+=str(coef) + "x^" + str(k)
    k-=1
result += "=0"
f = open('1.txt','w') 
f.write(result)