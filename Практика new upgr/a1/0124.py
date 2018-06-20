import math as m

s = float(input("Введіть довжину сторони "))
n = float(input("Введіть кількість сторін"))

print("Площа {0:.2f} m/sq".format((n*s**2)/4*m.tanh(m.pi/n)))


import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")

