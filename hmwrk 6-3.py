#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

first_string = "длор олрти нениабв лороабвнгр лорлоролаб итьиььабвн абв"
sub_string = "абв"
splitted_string = first_string.split()
result_string=[i for i in splitted_string if sub_string not in i]
result_string2=list(filter(lambda i : sub_string not in i, splitted_string))
print(result_string)
print(result_string2)