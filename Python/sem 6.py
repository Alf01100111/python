# 1. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
    
#     *Пример:* 
    
#     2+2 => 4; 
    
#     1+2*3 => 7; 
    
#     1-2*3 => -5;
    
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
        
#         *Пример:* 
        
#         1+2*3 => 7; 
        
#         (1+2)*3 => 9;
        

# 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# *Пример:* 

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# string = '1+2*35'
# s = s.replace('+',' ')
# s = s.replace('-',' ')
# s = s.replace('*',' ')
# s = s.replace('/',' ')
# lst = list(map(int, s.split()))

# a = []
# for item in s:
#     if not item.isdigit():
#         a.append(item)

# print(lst)




import random

list_0 = [random.randint(0,10) for i in range (15)]
print('Исходный список ', list_0)
new_list =[]
[new_list.append(i) for i in list_0 if i not in new_list ]
print('Список без повторных элементов ', new_list)



matrix = [[x for x in range(1, 4)] for y in range(1, 4)]