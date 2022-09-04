# my_age = int(input("введите возраст"))
# print(f"Вам {my_age} лет")

# 1. Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.
    
#     *Примеры:* 
    
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

# first = int(input ("Введите число 1 "))
# sec = int(input ("введите число 2 "))

# if (sec == first*first) or (first == sec ** 2):
#     print ("да")
# else:
#     print ("нет")

my_list = [8, 'r', 7, True]



# my_list.append('END') #добавляет в конец списка
# my_list.pop(1) #удаляет символ

# print(my_list)
# print(len(my_list))

# range(5) --> от нуля до пяти
# range(1,10) --> от одного до десяти
# range(1,10,2)  --> от одного до десяти шаг 2


# for i in range(1,10,2):
#     print (i)

for i in range(len(my_list)):
    print(my_list[i])