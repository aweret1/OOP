p = float(input("Тиск "))
v = float(input("Обєм "))
t = float(input("Температура в цельсіях "))
T = t+273.15

print("Молярна маса {0:.2f}".format((p*v/1000)/(8.314*T)))

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
