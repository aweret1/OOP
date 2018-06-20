a = float(input('Кількість до 1 л:'))
s = float(input('Кількість більше літру:'))
print('Доплата до літра',a*0.10,'$','\nДоплата після літра',s*0.25,'$')

import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Іщенко")
