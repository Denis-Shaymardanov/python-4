'''Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$'''
import math
def num_after_point(d):
    s = str(d)
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1

d = float(input('Введите точность d '))
print(round(math.pi, num_after_point(d)))

