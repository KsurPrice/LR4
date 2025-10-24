#Карась Илья
def get_sq(numbers): #функция генератора списка
    return [x**2 for x in numbers] #возращаем генератор списка
list1 = list(map(int, input("Введите числа: ").split()))#вводим числа
list2 = get_sq(list1) #записываем новый список с квадратами
print(list2) #выводим