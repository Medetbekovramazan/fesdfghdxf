#1 Длина оотрезка
#def distance(x1=6, y1=8, x2=6, y2=8):
#    dst = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
#    return dst
#x1 = int(input())
#y1 = int(input())
#x2 = int(input())
#y2 = int(input())

#res = distance(x2=x2,y2=y2,x1=x1,y1=y1)
#print(res)

#Отрицательная степень
#def power(a, n):
#    result = 1
#    for _ in range(abs(n)):
#     result *= a
#    if n < 0:
#        result = 1 / result
#    return result
#a = float(input("Введите значение a: "))
#n = int(input("Введите значение n: "))
#result = power(a, n)
#print("Результат возведения в степень:", result)

#Числа Фибоначчи
#def fib(n):
#    if n <= 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return fib(n - 1) + fib(n - 2)

#n = int(input("Введите номер числа Фибоначчи: "))

#result = fib(n)
#print("n-е число Фибоначчи:", result)

#2 Високосный год
#def is_year_leap(year):
#    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#        return True
#    else:
#        return False

#year = int(input("Введите год: "))

#result = is_year_leap(year)
#print("Является ли год високосным:", result)

#Квадрат
#def square(side):
#    perimeter = 4 * side
#    area = side ** 2
#    diagonal = math.sqrt(2) * side
#    return (perimeter, area, diagonal)

#side = float(input("Введите сторону квадрата: "))

#result = square(side)
#print("Периметр, площадь и диагональ квадрата:", result)

#Времена год
#def season (seas):
#    seas=abs(seas%12)
#    if seas >= 9:
#     return print('сейчас осень')
#    elif seas >=6:
#     return print('сейчас лето')
#    elif seas >=3:
#     return print('сейчас весна')
#    elif seas ==0:
#     return print('сейчас зима')
#    elif seas > 0:
#     return print('сейчас зима')
#season(int(input('введи номер месяца года: ')))

#Банковский вклад
#a=int(input('вклад: '))
# year=int(input('через сколько лет?: '))
# for i in range(year):
# 	a=a+a/10
# print(round(a, 3))

# простые числа
# def is_prime(is_prime):
# 	assistant=0 #для того что бы помочь вывести один результат, а не повторные
#
# 	if is_prime>1:     #что бы определить является ли число проситым
# 		for i in range(2, is_prime):  #работает пока не найдет, простое ли число
# 			if is_prime % i==0:
# 				assistant =0
# 				break
# 			else:
# 				assistant=1
# 	else:
# 		assistant = 0
#
#
# 	if assistant == 0:
# 		print(f'число {is_prime} не является простым','\n')
# 	elif assistant == 1:
# 		print(f'число {is_prime} является простым','\n')
# while True:
# 	is_prime(int(input('проверка на простоты числа: ')))


# Правильная дата
# def date(day, month, year):
# 	if day <= 0 or month <= 0 or year < 0:
# 		return False
# 	else:
# 		months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 		if year % 4 == 0:  months[1] = 29
# 		if day <= months[month - 1]:
# 			if month <= 12:
# 				return True
# 		return False
# print(date(int(input('день: ')), int(input('месяц: ')), int(input('год: '))))
