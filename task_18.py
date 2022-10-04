# Вычислить число pi c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

def precision_row(d: int) -> float:
    pi, sign, m = 3, 1, 2
    while abs(pi - (pi + sign*4/(m**3+3*m**2+2*m))) > 10**(-d-1):
        pi = pi + sign*4/(m**3+3*m**2+2*m)
        sign = -1*sign
        m = m+2
    return round((pi + (pi + sign*4/(m**3+3*m**2+2*m)))/2, d)

d = int(input('Задайте точность(количество знаков после запятой): '))
pi = precision_row(d)
print(f'С точностью {d}, число {pi = }; ')