#Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки 
# Random для получения случайного int
import random
length = int(input('Введите длину массива: '))
num = []
for i in range(length):
    num.append(i + 1)
print(num)
temporary = 0
for a in range(len(num)*3):
    rnd = random.randint(0, len(num) - 1)
    temporary = num[0]
    num[0] = num[rnd]
    num[rnd] = temporary

print(num)    
   
