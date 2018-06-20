import math as m


r = float(input('Радіус '))
print ("Площа {0:.2f} м/кв\nОбєм {1:.2f} м/куб".format(m.pi*r**2, (4*m.pi*r**3)/3))


import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
