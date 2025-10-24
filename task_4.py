#Карась Илья
list1 = list(map(str, input("Введите строки: ").split())) #вводим строки
list2 = [s * 3 for s in list1] #записываем
print(list2)  # выводим