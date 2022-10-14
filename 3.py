'''Задайте последовательность чисел. Напишите программу, которая 
выведет список неповторяющихся элементов исходной последовательности'''
def unique_elements(array):
    result = []
    for i in range(0, len(array)):
        if not array[i] in result: result.append(array[i])
    return result

a = [1, 12, 13, 13, 14, 12, 14, 15]
print(unique_elements(a))
