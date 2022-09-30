# Напишите программу, которая найдёт произведение пар чисел списка (CСписок создаем как в предыдущем задании). 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

n = int (input ("Введите число: "))
import random
rand_list=[]
for i in range(n):
	rand_list.append(random.randint(1,10))
print(rand_list)
result_list = []
for i in range((len(rand_list)+1)//2):
     result_list.append(rand_list[i]*rand_list[len(rand_list)-1-i])
print(result_list)