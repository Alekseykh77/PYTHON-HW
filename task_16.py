# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# 45 -> 101101
# 3 -> 11
# 2 -> 10

n = int(input("Введите десятичное число: ")) 
b = bin(n)
b1 = b[2::]
print(f"Число {n} в двоичной системе это {b1}")