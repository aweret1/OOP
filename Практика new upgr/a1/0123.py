import math

a = float(input("Перше число "))
b = float(input("Друге число "))

print ("Сума {0:.2f}\nРізниця {1:.2f}\nДобуток {2:.2f}\nЧастка {3:.2f}\nСтепінь {4:.2f}\nОстача {5:.2f}\nЛогарифм {6:.2f}"
       .format(a+b , b-a , a*b , a/b , a**b , a%b , math.log10(a)))


import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
