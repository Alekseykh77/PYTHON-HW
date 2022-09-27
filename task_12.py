# Реализовать алгоритм перемешивания списка.

import random
lst = [random.randint(0,100) for i in range(random.randint(5,20))]
print(f"Исходный список:\n{lst}")
random.shuffle(lst)
print(f"Список после перемешивания:\n{lst}")