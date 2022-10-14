'''Задайте натуральное число N. Напишите программу,
 которая составит список простых множителей числа N.'''
def simple_multiplies_of_number(n):
    array = []
    while n > 1:
        i = 2
        f = 0
        while 1:
            if n%i == 0:
                n = n // i
                array.append(i)
                f = 1
                break
            else:
                i += 1
        if f == 1:
            continue

    return array

n = int(input('Введите N '))
print(f"Простые множители числа: {simple_multiplies_of_number(n)}")
