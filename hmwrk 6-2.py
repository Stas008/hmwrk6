# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

list1=[1, 1, 2, 3, 4, 5, 5, 7, 8, 8, 9, 12]

list2=[i for i in  list1 if list1.count(i) == 1]
print(list2)
list3=list(filter(lambda i: list1.count(i) == 1, list1))
print(list3)
