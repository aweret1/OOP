import math as m


d = float(input('Висота з якої падає предмет '))
print('Швидкість предмета {0:.3f} м/с'.format(m.sqrt(2*9.8*d)))

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
