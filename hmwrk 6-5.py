#Задайте список из N элементов, заполненных числами из промежутка [-N, N].

n=int(input("Введите N: "))

my_list = [i for i in range(-n,n+1)]

print(my_list)
