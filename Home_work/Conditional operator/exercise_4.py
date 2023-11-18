'''
Задача 4.
Напишите программу, которая определяет пройдет коробка с размерами a*b*c в ящик с размерами x*y*z
'''

# Считываем введенное в консоли число
a,b,c = int(input('Введите размеры коробки a,b,c:')),int(input()),int(input())
x,y,z = int(input('Введите размеры коробки x,y,z:')),int(input()),int(input())
box1 = [a,b,c]
box2 = [x,y,z]
box1.sort()
box2.sort()

enter = True
for i in range(3):
    if box1[i] >= box2[i]:
        enter = False
        break
if enter:
    print('Коробка поместилась')
else:
    print('Коробка не поместилась')






